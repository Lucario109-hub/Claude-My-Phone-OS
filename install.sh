#!/usr/bin/env bash
# LucarioNet Installer für Raspberry Pi OS (Bookworm/Bullseye)
# Nutzung:  bash install.sh
set -e

DIR="$HOME/lucarionet"
PORT=8080

echo "==> Installiere LucarioNet nach $DIR"
mkdir -p "$DIR"
cp -f index.html manifest.webmanifest sw.js icon.svg icon-192.png icon-512.png lucarionet-server.py "$DIR/"

echo "==> Prüfe NetworkManager (für das WLAN-Menü)"
command -v nmcli >/dev/null 2>&1 || sudo apt-get install -y network-manager || true

echo "==> Prüfe Chromium"
if command -v chromium >/dev/null 2>&1; then
  BROWSER=chromium
elif command -v chromium-browser >/dev/null 2>&1; then
  BROWSER=chromium-browser
else
  sudo apt-get update
  sudo apt-get install -y chromium || sudo apt-get install -y chromium-browser
  BROWSER=$(command -v chromium || command -v chromium-browser)
fi

echo "==> Richte Webserver (nur lokal, Port $PORT) als Dienst ein"
sudo tee /etc/systemd/system/lucarionet.service >/dev/null <<EOF
[Unit]
Description=LucarioNet
After=network.target

[Service]
User=$USER
WorkingDirectory=$DIR
ExecStart=/usr/bin/python3 $DIR/lucarionet-server.py --port $PORT --bind 127.0.0.1
Restart=always

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now lucarionet.service

echo "==> Erstelle Startskript"
cat > "$DIR/start-kiosk.sh" <<EOF
#!/usr/bin/env bash
sleep 3
exec $BROWSER --kiosk --noerrdialogs --disable-infobars --no-first-run \\
  --disable-session-crashed-bubble --overscroll-history-navigation=0 \\
  --autoplay-policy=no-user-gesture-required \\
  --use-fake-ui-for-media-stream \\
  --app=http://localhost:$PORT/index.html
EOF
chmod +x "$DIR/start-kiosk.sh"

echo "==> Autostart einrichten"
# X11 / LXDE
mkdir -p "$HOME/.config/autostart"
cat > "$HOME/.config/autostart/lucarionet.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=LucarioNet
Exec=$DIR/start-kiosk.sh
EOF
# Wayland (labwc, Standard bei Bookworm)
mkdir -p "$HOME/.config/labwc"
grep -qs "start-kiosk.sh" "$HOME/.config/labwc/autostart" 2>/dev/null || \
  echo "$DIR/start-kiosk.sh &" >> "$HOME/.config/labwc/autostart"

echo
echo "Fertig! Starte jetzt neu mit:  sudo reboot"
echo "Ohne Neustart testen:          $DIR/start-kiosk.sh"
echo "Zum Beenden des Kiosks:        Alt+F4"
