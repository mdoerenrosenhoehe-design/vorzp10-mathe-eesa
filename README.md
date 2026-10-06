# ZP10 Mathe NRW – EESA Trainer

Vollständig statische Lernwebsite zur Vorbereitung auf die **Zentrale Prüfung 10 Mathematik in Nordrhein-Westfalen auf EESA-Niveau**. Sie läuft ohne Serverlogik und kann kostenlos über GitHub Pages veröffentlicht werden.

## Enthalten

- 8 Themenbereiche
- **800 Aufgaben** (100 je Thema)
- 160 Karteikarten (20 je Thema)
- Quiz mit 20 zufälligen Fragen, zwei Versuchen, Hinweisen, Punkten, Buzzer und Konfetti
- Zuordnungsspiel mit 10 Paaren
- schwierige Aufgaben mit drei Versuchen, gestuften Hinweisen und Lösungsweg
- adaptive gemischte Karteikarten-Wiederholung
- **20 Teil-1-Prüfungsvarianten** und **20 Teil-2-Prüfungsvarianten**
- Prüfungstimer: max. 30 Minuten Teil 1, insgesamt 90 Minuten; eingesparte Teil-1-Zeit wird Teil 2 gutgeschrieben
- lokale Speicherung mit `localStorage`
- automatische Prüfungsauswertung und thematische Lernempfehlungen
- lokale Kopie der EESA-Formelsammlung
- QR-Code für die vorkonfigurierte GitHub-Pages-Adresse
- responsive Bedienung für Smartphone, Tablet und PC

## Ordnerstruktur

```text
index.html
css/style.css
js/app.js
js/config.js
data/
  themes.json
  tasks_*.json
  flashcards_*.json
  matching_*.json
  exam_part1.json
  exam_part2.json
assets/
  formelsammlung_eesa.pdf
  qr-code.png
ANALYSE_MATERIALIEN.md
README.md
```

## Vor dem Veröffentlichen: Paddy-Link eintragen

Im übermittelten Projektauftrag steht für den EESA-Agenten nur der Platzhalter `<PADDY_AGENT_LINK>`. Daher konnte kein sicherer EESA-Link eingesetzt werden.

Öffne `js/config.js` und trage dort den tatsächlichen Link ein:

```js
PADDY_AGENT_LINK: 'https://tools.paddy.app/...'
```

Sobald ein Link eingetragen ist, öffnet der Button **„KI-Lernhilfe“** den Agenten in einem neuen Tab.

## GitHub Pages veröffentlichen

1. Entpacke den Projektordner.
2. Öffne dein GitHub-Repository für die Lernwebsite.
3. Lade **den Inhalt des Ordners** `zp10_eesa_website` in die oberste Ebene des Repositories hoch. Wichtig: `index.html` muss direkt im Repository liegen.
4. Committe die Dateien.
5. Öffne **Settings → Pages**.
6. Unter **Build and deployment** wähle **Deploy from a branch**.
7. Branch: `main`, Ordner: `/ (root)`.
8. Klicke auf **Save**.
9. Nach kurzer Zeit erscheint die veröffentlichte Adresse.

Die Konfiguration enthält bereits:

`https://mayodragon.github.io/vorzp10-mathe-eesa/`

Wenn du eine andere Adresse verwendest, ändere `SITE_URL` in `js/config.js` und erzeuge den QR-Code neu.

## QR-Code neu erzeugen

Mit Python:

```bash
pip install qrcode[pil]
python make_qr.py "https://DEINE-ADRESSE.github.io/DEIN-REPO/"
```

Dadurch wird `assets/qr-code.png` ersetzt.

## Lokal testen

Wegen der JSON-Dateien sollte die Website nicht direkt per Doppelklick als `file://` geöffnet werden. Starte einen kleinen lokalen Webserver:

```bash
python -m http.server 8000
```

Dann im Browser öffnen: `http://localhost:8000`

## Speicherung

Der Lernstand wird ausschließlich im Browser des jeweiligen Gerätes unter dem Schlüssel `zp10_eesa_progress_v2` in `localStorage` gespeichert. Es werden keine Konten und keine personenbezogenen Daten benötigt. Wird der Browser-Speicher gelöscht oder ein anderes Gerät/Browser genutzt, steht dort ein eigener Lernstand zur Verfügung.

## Inhaltliche Grundlage

Die Struktur wurde aus den bereitgestellten Prüfungen, Beispiellösungen, Beispielaufgaben, Vorbereitungsunterlagen und der EESA-Formelsammlung abgeleitet. Ergänzend wurden die offiziellen NRW-Vorgaben für die ZP10 2027 berücksichtigt. Die Aufgaben sind eigenständig neu erstellt; alte Prüfungsaufgaben werden nicht einfach kopiert.

Details: `ANALYSE_MATERIALIEN.md`.

## Aktualisierung der Aufgabendaten

`build_data.py` erzeugt die statischen JSON-Dateien neu. Die fertige Website benötigt Python **nicht**; das Skript ist nur für die Pflege des Datenbestands gedacht.
