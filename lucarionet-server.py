#!/usr/bin/env python3
"""LucarioNet-Server für den Raspberry Pi (nur Python-Standardbibliothek).

Liefert die Oberfläche aus UND stellt eine kleine, lokale API für echtes WLAN bereit
(über NetworkManager / nmcli). Lauscht standardmäßig nur auf 127.0.0.1.

Start:  python3 lucarionet-server.py [--port 8080] [--bind 127.0.0.1]
"""
import argparse, http.server, json, os, re, shutil, socketserver, subprocess, sys
from urllib.parse import urlparse, parse_qs

ROOT = os.path.dirname(os.path.abspath(__file__))
NMCLI = os.environ.get("NMCLI") or shutil.which("nmcli") or "nmcli"
BLOCKED_EXT = (".py", ".sh", ".service", ".md")


def run(args, stdin=None, timeout=20):
    """nmcli aufrufen – immer als Argumentliste (keine Shell, keine Injection)."""
    try:
        p = subprocess.run([NMCLI] + args, input=stdin, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()
    except FileNotFoundError:
        return 127, "", "nmcli nicht gefunden"
    except subprocess.TimeoutExpired:
        return 124, "", "Zeitüberschreitung"


def split_terse(line):
    """nmcli -t trennt mit ':' und maskiert ':' im Feld als '\\:'."""
    out, cur, esc = [], "", False
    for ch in line:
        if esc:
            cur += ch
            esc = False
        elif ch == "\\":
            esc = True
        elif ch == ":":
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return out


def wifi_device():
    rc, out, _ = run(["-t", "-f", "DEVICE,TYPE,STATE", "dev"])
    if rc:
        return None
    for line in out.splitlines():
        f = split_terse(line)
        if len(f) >= 2 and f[1] == "wifi":
            return f[0]
    return None


def valid_ssid(s):
    return isinstance(s, str) and 1 <= len(s.encode("utf-8")) <= 32 and not re.search(r"[\x00-\x1f]", s)


def valid_pw(s):
    return isinstance(s, str) and 8 <= len(s) <= 63 and not re.search(r"[\x00-\x1f]", s)


def api_status():
    rc, out, err = run(["-v"])
    if rc == 127:
        return {"ok": False, "error": "NetworkManager (nmcli) ist nicht installiert"}
    dev = wifi_device()
    radio = run(["radio", "wifi"])[1].strip() == "enabled"
    ssid, signal, ip = "", 0, ""
    rc, out, _ = run(["-t", "-f", "ACTIVE,SSID,SIGNAL", "dev", "wifi", "list", "--rescan", "no"])
    for line in out.splitlines() if rc == 0 else []:
        f = split_terse(line)
        if len(f) >= 3 and f[0] == "yes":
            ssid, signal = f[1], int(f[2] or 0)
            break
    rc, out, _ = run(["-g", "IP4.ADDRESS", "dev", "show", dev]) if dev else (1, "", "")
    if rc == 0 and out:
        ip = out.splitlines()[0].split("/")[0]
    rc, out, _ = run(["-t", "-f", "DEVICE,TYPE,STATE", "dev"])
    eth = any(split_terse(l)[1:3] == ["ethernet", "connected"] for l in out.splitlines() if len(split_terse(l)) >= 3) if rc == 0 else False
    return {"ok": True, "device": dev, "radio": radio, "ssid": ssid, "signal": signal, "ip": ip, "ethernet": eth}


def api_scan(rescan):
    dev = wifi_device()
    if not dev:
        return {"ok": False, "error": "Kein WLAN-Adapter gefunden"}
    rc, out, err = run(["-t", "-f", "IN-USE,SSID,SIGNAL,SECURITY", "dev", "wifi", "list", "ifname", dev,
                        "--rescan", "yes" if rescan else "no"], timeout=30)
    if rc:
        return {"ok": False, "error": err or "Suche fehlgeschlagen"}
    nets = {}
    for line in out.splitlines():
        f = split_terse(line)
        if len(f) < 4 or not f[1]:
            continue
        n = {"ssid": f[1], "signal": int(f[2] or 0), "security": f[3] or "", "active": f[0] == "*"}
        old = nets.get(n["ssid"])
        if not old or n["signal"] > old["signal"] or n["active"]:
            if old and old["active"]:
                n["active"] = True
            nets[n["ssid"]] = n
    saved = set(api_saved().get("saved", []))
    res = sorted(nets.values(), key=lambda x: (not x["active"], -x["signal"]))
    for n in res:
        n["saved"] = n["ssid"] in saved
    return {"ok": True, "networks": res}


def api_saved():
    rc, out, _ = run(["-t", "-f", "NAME,TYPE", "con", "show"])
    names = [split_terse(l)[0] for l in out.splitlines() if rc == 0 and len(split_terse(l)) >= 2 and split_terse(l)[1] == "802-11-wireless"]
    return {"ok": True, "saved": names}


def api_connect(b):
    ssid, pw = b.get("ssid"), b.get("password") or ""
    if not valid_ssid(ssid):
        return {"ok": False, "error": "Ungültiger Netzwerkname"}
    if pw and not valid_pw(pw):
        return {"ok": False, "error": "WLAN-Passwort: 8–63 Zeichen"}
    dev = wifi_device()
    args = ["--ask", "dev", "wifi", "connect", ssid] + (["ifname", dev] if dev else [])
    # Passwort über stdin (nicht in der Prozessliste sichtbar)
    rc, out, err = run(args, stdin=(pw + "\n") if pw else None, timeout=60)
    if rc:
        msg = err or out or "Verbindung fehlgeschlagen"
        if "Secrets were required" in msg or "password" in msg.lower():
            msg = "Passwort falsch oder erforderlich"
        return {"ok": False, "error": msg}
    return {"ok": True, "message": "Verbunden mit " + ssid}


def api_post(path, b):
    if path == "connect":
        return api_connect(b)
    if path == "disconnect":
        dev = wifi_device()
        rc, out, err = run(["dev", "disconnect", dev]) if dev else (1, "", "Kein WLAN-Adapter")
        return {"ok": rc == 0, "error": err} if rc else {"ok": True}
    if path == "forget":
        if not valid_ssid(b.get("ssid")):
            return {"ok": False, "error": "Ungültiger Netzwerkname"}
        rc, out, err = run(["con", "delete", "id", b["ssid"]])
        return {"ok": rc == 0, "error": err} if rc else {"ok": True}
    if path == "radio":
        rc, out, err = run(["radio", "wifi", "on" if b.get("on") else "off"])
        return {"ok": rc == 0, "error": err} if rc else {"ok": True}
    if path == "hotspot":
        if not valid_ssid(b.get("ssid")) or not valid_pw(b.get("password")):
            return {"ok": False, "error": "Hotspot: Name (1–32 Zeichen) und Passwort (8–63 Zeichen) nötig"}
        dev = wifi_device()
        if not dev:
            return {"ok": False, "error": "Kein WLAN-Adapter"}
        rc, out, err = run(["dev", "wifi", "hotspot", "ifname", dev, "ssid", b["ssid"], "password", b["password"]], timeout=30)
        return {"ok": rc == 0, "error": err or out} if rc else {"ok": True, "message": "Hotspot aktiv"}
    if path == "hotspot_off":
        rc, out, err = run(["con", "down", "Hotspot"])
        return {"ok": rc == 0, "error": err} if rc else {"ok": True}
    return {"ok": False, "error": "Unbekannte Funktion"}


class Handler(http.server.SimpleHTTPRequestHandler):
    server_version = "LucarioNet"

    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def log_message(self, *a):
        pass

    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        super().end_headers()

    def host_ok(self):
        host = (self.headers.get("Host") or "").split(":")[0].lower()
        return host in ("127.0.0.1", "localhost", "[::1]")

    def api_guard(self):
        """Nur die eigene Oberfläche darf die API nutzen (Schutz vor fremden Webseiten)."""
        if not self.host_ok() or self.headers.get("X-Lucario") != "1":
            return False
        origin = self.headers.get("Origin")
        if origin and urlparse(origin).netloc != self.headers.get("Host"):
            return False
        if self.headers.get("Sec-Fetch-Site", "same-origin") not in ("same-origin", "none"):
            return False
        return True

    def send_json(self, obj, code=200):
        data = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        u = urlparse(self.path)
        if u.path.startswith("/api/"):
            if not self.api_guard():
                return self.send_json({"ok": False, "error": "Nicht erlaubt"}, 403)
            q = parse_qs(u.query)
            p = u.path[5:]
            if p == "status":
                return self.send_json(api_status())
            if p == "scan":
                return self.send_json(api_scan(q.get("rescan", ["0"])[0] == "1"))
            if p == "saved":
                return self.send_json(api_saved())
            return self.send_json({"ok": False, "error": "Unbekannt"}, 404)
        if not self.host_ok() or u.path.lower().endswith(BLOCKED_EXT) or "/." in u.path:
            return self.send_error(404)
        return super().do_GET()

    def do_HEAD(self):
        if self.path.startswith("/api/"):
            return self.send_error(405)
        return super().do_HEAD()

    def do_POST(self):
        u = urlparse(self.path)
        if not u.path.startswith("/api/") or not self.api_guard():
            return self.send_json({"ok": False, "error": "Nicht erlaubt"}, 403)
        try:
            n = int(self.headers.get("Content-Length") or 0)
            b = json.loads(self.rfile.read(min(n, 4096)) or b"{}")
            if not isinstance(b, dict):
                raise ValueError
        except Exception:
            return self.send_json({"ok": False, "error": "Ungültige Anfrage"}, 400)
        return self.send_json(api_post(u.path[5:], b))

    def list_directory(self, path):
        self.send_error(404)
        return None


Handler.extensions_map = {**Handler.extensions_map, ".webmanifest": "application/manifest+json", ".svg": "image/svg+xml", ".js": "text/javascript"}


class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8080)
    ap.add_argument("--bind", default="127.0.0.1")
    a = ap.parse_args()
    print(f"LucarioNet läuft auf http://{a.bind}:{a.port}/", flush=True)
    try:
        Server((a.bind, a.port), Handler).serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
