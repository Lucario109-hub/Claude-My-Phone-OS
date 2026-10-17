# LucarioNet 2.0 – Raspberry-Pi-Paket

## Inhalt
- `index.html` – das komplette System (alle Apps)
- `manifest.webmanifest`, `sw.js`, `icon*.png/svg` – machen LucarioNet installierbar und offline-fähig
- `install.sh` – richtet alles auf dem Raspberry Pi ein

## Auf den Raspberry Pi packen
1. Raspberry Pi OS (mit Desktop) installieren und mit WLAN verbinden.
2. Den Ordner auf den Pi kopieren (USB-Stick oder `scp -r lucarionet-pi pi@<IP>:~`).
3. Im Terminal:
   ```
   cd lucarionet-pi
   bash install.sh
   sudo reboot
   ```
4. Nach dem Neustart startet LucarioNet automatisch im Vollbild.

## Als App installieren (ohne Pi-Skript)
- Starte einen Webserver im Ordner: `python3 -m http.server 8080`
- Öffne in Chrome `http://localhost:8080` → Menü ⋮ → **App installieren**
  (oder in LucarioNet: Einstellungen → Installieren).
- Wichtig: Installation und Kamera funktionieren nur über `localhost` oder HTTPS, nicht über `file://`.

## Apps
Spiele (Snake, 2048, Memory, Pong, Lucario Jump), Kamera, Galerie, Browser, Musik,
LucarioTube (eigene Videos hochladen, liken, kommentieren), LucarioMail (eigenes Postfach),
App Store (Tetris, Minesweeper, Breakout, Tic-Tac-Toe, Reaktionstest), eigene Hintergründe.

## Gut zu wissen
- Alles (Videos, Fotos, Mails, Musik, Hintergründe) liegt **lokal** im Browser-Speicher des Geräts
  (IndexedDB). Es gibt keinen Server und keine Synchronisation zwischen Geräten.
- LucarioTube und LucarioMail sind lokale Apps. Mails an andere Adressen werden über „Extern senden“
  in deiner E-Mail-App geöffnet. Echter E-Mail-Versand bräuchte einen Mailserver.
- Browser-Daten nicht löschen, sonst sind Uploads weg.
- Updates: neue `index.html` kopieren und in `sw.js` die Version (`lucarionet-v2` → `v3`) erhöhen.
