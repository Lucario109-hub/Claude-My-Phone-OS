# LucarioNet 5.0

Ein komplettes Handy-Betriebssystem als Web-App (eine `index.html`, installierbar als PWA).

## Was drin ist
- Start: Hell/Dunkel/Auto-Modus, Akzentfarben, eigene Hintergründe, Schnelleinstellungen (Statusleiste antippen), PIN-Sperre, Suche
- Messenger mit eigener Telefonnummer (Ende-zu-Ende verschlüsselt, Nummern nur einmal vergeben)
- E-Mail mit Konto + Passwort, Namen nur einmal vergeben
- Telefon (simulierte Anrufe), Kamera, Galerie, Browser, Musik, LucarioTube (eigene Uploads)
- Einstellungen: Konto, Verknüpfte Apps (WhatsApp, Telegram, Signal, Instagram, TikTok, Snapchat, Discord, X, Facebook, YouTube, Spotify, Gmail), Anzeige, Hintergrund, Ton, Sicherheit, Datenschutz, Speicher, Apps, Info
- Rechner, Notizen, Uhr, Kalender, Dateien, System-Manager
- App Store: Snake, 2048, Memory, Pong, Flappy, Tetris, Minesweeper, Breakout, Tic-Tac-Toe, Reaktion, 4 Gewinnt, Simon, Whack, Wetter, Aufgaben, Zeichnen, Recorder, Taschenlampe, Würfel, Einheiten

## Neu in 5.0
- Startbildschirm: Uhrzeit, WLAN-Chip, Akku, Notruf; Entsperren per Passwort oder PIN (Fehlversuch-Sperre bleibt auch nach Neustart)
- Einrichtungs-Assistent beim ersten Start (WLAN, Design, Sperre, Konto)
- WLAN-Menü: Status, Internet-Test; auf dem Raspberry Pi echte Netzwerksuche, Verbinden, Hotspot (lucarionet-server.py + NetworkManager)
- LucarioBot: Assistent (offline-Befehle) + optional KI-Server (z. B. Ollama auf dem Pi)
- Support: Tickets, automatische Antworten, E-Mail an support@lucario.net, Sofort-Hilfe bei gestohlenen Daten (Passwort ändern, Verknüpfungen trennen, Konto löschen, Gerät zurücksetzen)
- Fehler behoben: doppelte Element-IDs (Anmelden-Button, Aufgaben, Rechner-Anzeige), Spiele-Timer laufen nach dem Schließen nicht weiter

## Neu in 6.0
- **Lucario Arena**: Echtzeit-Shooter mit grafischer Oberfläche (Joystick, Auto-Zielen, Fähigkeiten-Buttons). Wellen gegen Bots, Duelle (Best of 3 gegen Computer-Spieler), Quests, Coins und Diamanten, Kisten (100 Coins / 100 Diamanten), Skin-Verkauf, Mythic-Fähigkeiten. Spielstand im Gerätespeicher.
- **Terminal**: Shell mit help, ls, cat, ps, calc, theme, open, neofetch u. a. Befehl `arena` startet das Spiel, `arena sim 200` zeigt die Balancing-Simulation.
- Tastatur am PC: Tasten wählen die gleichnamige Schaltfläche (z. B. 1, z, d, m).

## Hängt die App auf einer alten Version?
Öffne einmal `update.html` (z. B. `https://lucario109-hub.github.io/Claude-My-Phone-OS/update.html`). Die Seite entfernt nur den alten Zwischenspeicher und startet LucarioNet neu. Spielstände bleiben erhalten.

## Neu in 6.4
- Saison-Skins (App „Skins“): Halloween 🎃 und Silvester 🎆 mit animierter Szene (Geister, Fledermäuse, Kürbisse, Feuerwerk, Konfetti, Skyline).
- Leistungs-Wächter: senkt Effekte automatisch bei niedriger Bildrate; Schalter ⚡ Leistung (Auto/Voll/Sparsam/Minimal) im Schnellpanel.
- Ultra-Modus: 6 neue Effekte (Partikel-Spur, Code-Regen, Sternschnuppen, Glühwürmchen, Glitch-Öffnen, Neon-Rahmen) und 🚀-Schalter im Schnellpanel.
- Breakout 2.0 (Leben, Level, Power-Ups, Combo), Snake 2.0 (Portal-Modus, Goldapfel, Hindernisse, Tempo-Stufen), Putz Simulator: neue Mopps und Schwamm, mehr Quests, Hochglanz-Prestige.
- Spiele: Spieler-Level mit XP und Titeln, Rekord-Feier mit Konfetti, Tagesherausforderung, Hardcore-Modus (30 % schneller, doppelte XP) und 23 Spiele-Erfolge im Spielecenter.
- Fehleranzeige und Notstart für Browser, in denen etwas nicht lädt (z. B. Safari).
- Fuß Knabber: Kaufmenge ×1 / ×10 / ×100 / MAX im Fruchtschnitten-Shop.
- Putz und Fuß Knabber: Button „Alles max kaufen“ kauft alle bezahlbaren Upgrade-Stufen auf einmal.
- Fuß Knabber: Zahlen gehen jetzt weiter (Trl, Trd, Qa …) und zeigen nie mehr Infinity. Putz Simulator: Boss alle 10 Level (wirft Dreck, gibt Skins), 3 neue Welten (Vulkanhöhle, Eispalast, Zuckerfabrik), Technik-Labor mit 8 neuen Upgrades.
- Widgets auf dem Homescreen, Live-Suche (Notizen, Aufgaben, Einstellungen), Benachrichtigungsverlauf im Schnellpanel, Klick-Sounds/Haptik, 6 neue Hintergründe, Backup inkl. Spielständen, Update-Hinweis.
- Neu: Spielecenter (Tagesbelohnung, Tagesaufgaben, Rekorde), Lucario Fabrik (Idle-Spiel), Fuß Knabber: Fruchtschnitten-Sturm + Skins, Putz Simulator: Haustiere + Tag/Nacht.
- Fuß Knabber Simulator 2.0: neue Fruchtschnitten, Technik-Labor, Erfolge, Goldene Fruchtschnitte, Disco-Grafik und 💎 Super Prestige (erst nach 100 Prestiges).

- Spiele-Grafik-Upgrade: neues Spiel-Design (Sternenhintergrund, Neon-Rahmen, glänzende HUD-Anzeigen) für alle Mini-Spiele; Snake, Pong, Lucario Jump, Breakout und Tetris mit Verläufen, Leuchteffekten, Partikeln und Ball-Spuren (Tetris mit Geisterblock); 2048, Memory, Minesweeper, Tic-Tac-Toe, Vier gewinnt, Simon, Maulwurf, Reaktionstest mit 3D-/Glanz-Optik und Animationen.

- Putz Simulator 2.0: 6 Räume mit eigener Optik (Keller, Küche, Garage, Schwimmbad, Lagerhalle, Raumstation), 5 Dreck-Sorten (neu: Rost und Giftschlamm), Boss-Räume alle 5 Level, 2 neue Mopps und 2 neue Schwämme, Combo-Multiplikator, Boosts (⚡ Turbo, 💰 ×2), bis zu 5 Putzroboter, Minikarte, Seifenblasen/Glanz-Effekte, neue Putzi-Figur und 15 weitere Quests. Effekte & Minikarte sind unter Statistiken abschaltbar.

- Zwei Icon-Stile: LucarioOS bekommt Neon-Icons (Glas-Kachel, Symbol in der Farbe der App), das klassische Design die bunten Glanz-Icons.

- Mehr Grafik in den Apps: bunte, glänzende App-Icons und ein Grafik-Banner (großes Icon + Leuchten) oben in jeder App; beides in Einstellungen → Design schaltbar.

- Animationen & Effekte (Einstellungen → Animationen): 11 einzeln schaltbare Effekte (Streifen, Polarlicht, Sterne, Logo, schwebende Icons, Icon-Glanz, Uhr-Leuchten, Leuchtkarten, Tipp-Wellen, App-Zoom, Neigungseffekt) plus Presets Maximum / Leicht / Alles aus.

- Bewegte Streifen im LucarioOS-Hintergrund: Einstellungen → Design → Bewegte Streifen (standardmäßig aus).

- LucarioOS ist jetzt das Standard-Design, inklusive Sperrbildschirm (Logo, Uhr mit Akzentfarbe, leuchtende PIN-Tasten).

- Start-Animation: das Logo stürzt wie ein Asteroid mit blauem Streifen herunter. Einstellungen neu gegliedert (Allgemein, Design, Hintergrundbild, Anzeige, Akku & Leistung, WLAN, Apps, Sicherheit, Benachrichtigungen, System). Technische Apps (System, Terminal, Support, Einheiten, Rechner …) im LucarioOS-Design.

- Einstellungen im LucarioOS-Stil: Header mit Logo, Suche, Kategorien mit Icons, Detailseiten mit Zurück-Pfeil (nur im LucarioOS-Design).

- LucarioOS-Startseite: Seitenpunkte funktionieren (Antippen oder Wischen), WLAN-Karte öffnet das WLAN-Menü, Akku-Karte die Einstellungen.

- Akzentfarben in Einstellungen → Anzeige & Design: eigene Farben hinzufügen (＋ Neue Farbe), mit ✎ Bearbeiten Farben löschen (mind. 1 bleibt), ↺ Standardfarben wiederherstellen.
- **Design-Stil LucarioOS**: Einstellungen → Anzeige & Design → Design-Stil. Dunkles Glas-Design mit großer Uhr, Begrüßung, Datum, Suchleiste, Akku- und WLAN-Widget.

## Neu in 6.3
- **Putz Simulator** (geheim): Installation nur im Terminal mit `Putz Simulator 123`. Karten werden mit jedem Level größer und dreckiger, Wischmopps und Schwämme kaufen und upgraden, Quests, Teleport.
- LucarioTube: roter Löschen-Button mit Sicherheitsabfrage, Papierkorb direkt auf jedem Video.
- Lucario Arena: nach jeder Runde automatischer 3-Sekunden-Countdown.
- Spiele-Fixes: Snake, Flappy und Breakout warten auf den ersten Tipp, Pong hat eine Aufschlagpause, alle laufen unabhängig von der Bildwiederholrate.

## Neu in 6.2
- Lucario Arena ist jetzt ein echtes Echtzeit-Spiel mit Grafik: Menü, Shop mit Kisten-Animation, Inventar, Quests, Profil. Die Text-Version läuft weiter im Terminal (`arena`).

## Neu in 6.1
- **Fuß Knabber Simulator**: Klicker-Spiel mit Fruchtschnitten (acht Sorten), Fuß Knabber Münzen über die Zeit, Level, Belohnung alle 5 Minuten, Upgrades, Prestige. Klickt man eine Fruchtschnitte an, gibt es einen Jumpscare (in den Spiel-Einstellungen auf „Manchmal“ oder „Aus“ stellbar; beim ersten Start kommt ein Warnhinweis).
- Das Spiel ist **nicht im App Store**. Installation: Terminal-App öffnen und `füße knabbern` eingeben.
- Fehler behoben: Warnung des Browsers, weil der Browser-iframe zugleich Skripte und „same-origin“ erlaubte (Sandbox-Ausbruch); Sperrbildschirm, Apps und Einstellungsseiten laufen ohne Konsolenfehler (41 Apps geprüft).

## Installieren auf dem Handy
Die Dateien auf einen https-Host legen (z. B. Netlify Drop oder GitHub Pages), die Adresse im Handy-Browser öffnen, "Zur Startseite hinzufügen" / "App installieren".

## Raspberry Pi
`bash install.sh` (Kiosk-Autostart mit Chromium, eigener Server mit WLAN-Schnittstelle).

## Ehrliche Grenzen
- Keine echte Mobilfunk-Verbindung: Anrufe sind simuliert ("Echt anrufen" nutzt tel:).
- Telefon-Bestätigungscode ist eine Demo (kein SMS-Dienst).
- Eindeutige Namen/Nummern gelten pro Gerät (kein zentraler Server).
- Verknüpfte Apps öffnen nur Deep-Links, keine echte API-Anbindung.
- Kamera, Installation und Verschlüsselung brauchen https oder localhost.
- Wetter braucht Internet.
- WLAN suchen/verbinden geht nur auf dem Pi (Browser dürfen das nicht). Auf dem Handy zeigt das Menü Status und Test.
- Die Gerätesperre ist eine Software-Sperre der Oberfläche; sie schützt nicht gegen jemanden mit Zugriff auf die Gerätedateien. Konto-Inhalte sind separat verschlüsselt.
- Es gibt keinen Server und kein Support-Personal: Tickets bekommen automatische Antworten und liegen auf dem Gerät. Eine echte Support-Adresse trägst du unter Einstellungen → Support ein.
- LucarioBot ist offline regelbasiert; freie Antworten gibt es nur mit eigenem KI-Server. Ein API-Schlüssel liegt unverschlüsselt im lokalen Speicher.
- Nach einem Neustart musst du dich bei der LucarioID neu anmelden.
- Lucario Arena: Der Online-Modus ist eine Simulation (Computer-Gegner). Echtes Online-Spielen bräuchte einen Spiele-Server.

## Browser-Unterstützung
Läuft in aktuellen Chrome, Edge, Firefox, Safari (iPhone ab iOS 14), Samsung Internet. Für ältere Browser werden fehlende Funktionen nachgerüstet; ist der Browser zu alt, erscheint ein Hinweis. Auf dem iPhone: In Safari öffnen, dann Teilen → „Zum Home-Bildschirm“. Der Link funktioniert nur in dieser Schreibweise: https://lucario109-hub.github.io/Claude-My-Phone-OS/
