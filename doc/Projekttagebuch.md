# Projekttagebuch
## Efe Yasar:
### 10.05.2026:
- Main-File erstellt und ausgebaut mit def Main_Screen(...) und def Main().
- Game_Variables erstellt

### 17.05.2026:
- Buttons eingebaut
- Hintergrundbild eingebaut
- Beenden eingebaut

### 19.05.2026:
- Play_Screen Funktion in main-Branch "Efe_main" erstellt

### 20.05.2026:
- Tagebuch-Sprites erstellt:
  - Ein Bild
  - Ein umblättern Sprite
- in main.py getestet
- diary.py und sprites.py in assets/game erstellt

### 21.05.2026:
- Diary vergrößert mithilfe von KI für die Nutzung beim Interagieren

### 22.05.2026:
- main_screen ausgelagert auf main_screen.py
- Tilemap - loader gebaut mithilfe von Hr. Bechtold
- Tagebuch Sprite erstellt mit Ausklappen

### 29.05.2026:
- Main Branch wurde aufgeräumt mit Hr. Bechtold
- Logik aufgeräumt 

### 30.05.2026:
- Main von ca. 300 Zeilen Code auf 22 Zeilen aufgeräumt. 
- Play_Screen, Main_Screen & Pause_Screen wurden ausgelagert. 
- Den Code Aufgeräumt.

### 31.05.2026:
- Background Sprites gelöscht
- Grund: nicht Top Down und schwer aus dem Tilesheet rauszulesen
- Nicht verwendet
- 1pxl Gap beim Tisch raus geschnitten
- Unnötige Charaktere gelöscht, 
- player.py aus src.assets gelöscht 
- in src.game reingetan
- player_variables auch da rein ergänzt um verwirrung vorzubeugen
- Tisch grün gemach damit das Tagebuch besser sichtbar ist
- Tagebuch interaktion in den play_screen eingefügt
- Speichern/Laden Bug gefixed

### 01.06.2026:
- Play-Screen gebaut
- Tilemap-leser angepasst
- Tagebuchlogik so gemacht, dass wenn man 'E' drückt es öffnet und wenn man nochmal 'E' drückt dann schließt es sich.
- alles etwas angepasst

### 07.06.2026:
- Play_screen sehr ausgebaut
- Map gezeichnet
- Objekte erstellt
- Haus platziert
- Aufgeräumt
- Bugs gefixed
- Häuser gebaut
- Brunnen versucht zu bauen
- Brunnen gebaut, mit transparenz
- interagieren so ausgebaut, dass es interaktiv ist
- Wand und Obstacles usw. in Play_Screen gebaut, so dass sie funktionieren
- In Medieval_Screen fehlt noch Häuser_kollisionen und Quiz

### 08.06.2026:
- gefixed dass Player nicht aus der Map rausrennen kann
- Map vergrößert, 
- verhindert dass Player in/durch Gebäude laufen kann
- großen Bug mit transparenz gelöst
- Brunnen und Castle automatisiert

### 14.06.2026:
- Interact mit Häusern gemacht 
- Funktionen für Screens für diese Funktionen gebaut

### 15.06.2026:
- Grundsturktur für Häuser gelegt

### 17.06.2026:
- Rotes Haus final ausgebaut
- Kerze als erstes Quest-Objekt platziert
- Bilder/Avatare für die Quest-Objekte platziert
- Player.move() so angepasst, dass er nicht über den Rand raus rennen kann
- Vom roten Haus wieder zurück zum Medieval Screen gebaut
- inventory.json erstellt, um das Quest-Inventar zu speichern
- Quest Gegenstände speichern und beim Neustart des Spiels die Liste löschen
- Kerze_bunt.png & Kerze_schwarz_weiß.png erstellt
- Neues UI-Pack hinzugefügt altes entfernt
- Projekttagebuch überarbeitet

### 19.06.2026:
- Im Grey_House eine Chest platziert
- in diese ein Quest-Objekt (Schild) eingefügt
- wenn man es anklickt, hat man es eingesammelt
- inventory.json logik umgeändert in Player Objekt

### 20.06.2026:
- Player-Objekt für Inventar in GameVariables platziert
- Schild_bunt.png und Schild_Schwarz_weiß erstellt
- Kerze_schwarz_weiß Rahmen in grau umgeändert
- main_screen, grey_house, medieval_screen und red_house angepasst
- Portal_Text so umgeändert, dass falls der Player noch nicht alle eingesammelt hat, der Text:
- "Collect Quest-Objects first Brudi" aufploppt
- Wenn Player die Objekte hat, kann er ins Portal
- Ein Welcome-Text in die Medieval Map eingebaut
- Dafür GOT_ALL_ITEMS in GameVariables eingebaut damit es leichter ist
- Ganze Castle Funktion gebaut
- letztes Quest-Gegenstand eingebaut (Krone im Castle)
- castle ausgeschmückt
- 3 Bilder erstellt

### 21.06.2026:
- Final fertig gebaut
- Bugs gefixed wie zum Beispiel  Zeit zurücksetzen beim neuen Spiel
- Leaderboard gebaut
- Zeitmessung

## Furkan Yildiz: