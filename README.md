# OpenAccessMediaImporterBot

# Kurzbeschreibung: 
Das Ziel unseres Projekts ist das Anbinden des Open Media Importers an die API und die Erweiterung der Anwendungsbereiche, um Mediendateien in Wikidata automatisiert aus wissenschaftlichen Arbeiten und Texten zu extrahieren und diese automatisch mit Tags zur besseren Zuordnung zu versehen.  
Unser minimales Projektziel ist es für dieses Semester uns in das bestehende Repository einzuarbeiten und mögliche Erweiterungen des Importers abzuwägen – dabei sollen offene Punkte und Herangehensweisen für die letztendliche Umsetzung im nächsten Semester klarer werden. Im Folgesemester soll die Hauptaufgabe sein unser eigentliches Ziel erreichen, den Importer richtig zu konfigurieren. Das bedeutet, dass gescrapte Bilder und Medien mit den dazu passenden Tags und Schlagworten versehen werden und diese dann automatisiert hochgeladen werden. Damit daraus eine Übersicht aus Knowledge Graphen entstehen kann. 
 
# Zeitplanung: 
Wir planen zum 21.12. (erstes Remotes Treffen) eine Übersicht vorstellen zu können, in der klar werden soll, wie unser genaues Projektziel aussieht, bzw. Der Weg dahin aussehen soll. Dabei soll eine realistische Planung des Machbaren entstehen und soweit möglich auch ein Austausch mit dem Ersteller des Open Access Media Importer Bot’s stattfinden. Gesetzte Deadlines sollen dabei einen reibungslosen “Fluss” des Projekts ermöglichen. 

# Geplante Arbeitsweise: 
Gearbeitet werden soll Projektübergreifend agil, durch Arbeitsaufteilung und damit einhergehende “Sprints” soll der Status des Projekts von jedem Projektmitglied nachvollziehbar sein. Dazu sollen einzelne Schritte dokumentiert, Aufgaben zugewiesen und gemeinsame Reviews von Code im Vordergrund stehen. 

#  Ziel des Projekts:
Das Ziel unseres Projekts ist die Erweiterung und Implementierung des MediaImporterBots.
Allgemeiner nehmen wir uns vor Open Science zu fördern, indem wir Daten einfacher und frei nutzbar gestalten.

# Projektmanagement: 
Das interne Projektmanagement läuft in unserem Fall über Microsoft To-Do.

# Grobe Gliederung des GitHub-Repositorium's: 
Das Repo soll neben der obligatorischen Readme Datei auch eine notwendige License Datei enthalten. Ordnerstrukturen sollen dabei für eine Nachvollziehbarkeit im Repo sorgen.  

# GitHub-Repositorium: 
Dieses GitHub Repositorium unterliegt der CC Lizens und kann somit von jedem genutzt und verändert werden.
https://github.com/mzajcev/OpenAccessMediaImporterBot 
 
# Standart Codestil unseres Projekts:
Der automatische Code-Formatter Black ersetzt in unserem Fall den PEP8 Linter. 

# Arbeitsstil:
Wir arbeiten in diesem Projekt nach den F.A.I.R Prinzipien.
F.A.I.R.-Principles:
F.: Findability
A.: Accessablity
I.: Interoperability
R.: Reproducebility

# Änderungsprotokoll:

### Datei: oa-cash

Update auf Python 3

  
#### 1. Art der Änderung: Import-Anweisungen entfernt

Was?

- Folgende Module wurden entfernt: gobject, pygst, gst
- Funktionen und Klassen, die nicht mehr verwendet werden, wurden entfernt: setup_all, create_all

  

#### 2. Art der Änderung: Import-Anweisungen aktualisiert / Hinzugefügt

Was?

- make_datestring aus helpers wurde importiert anstatt das gesamte Modul helpers zu importieren - Funktionen und Klassen wurden aktualisiert, um aus den entsprechenden Modulen zu importieren.
- sqlalchemy wurde hinzugefügt

  

#### 3. Art der Änderung: prints

Was?

- stderr.write wurde mit print ersetzt

#### 4. Art der Änderung: 'convert-media'

Was?

- materials wurde geändert (keine filter --> Alles)
- path wurde entfernt (an manchen Stellen os.path hinzugefügt)
- Zeilen 167 - 186 wurden neu hinzugefügt, weil ....

#### 5. Art der Änderung: 'find-media'

Was?

- Erster Teil des Codes wurde Auskommentiert, weil...
- skip wurde auskommentiert
- journal und artical.get_by wurde entfernt, contrib_authors wurde als eigene variable hinzugefügt
- der Code für category wurde zunächst entfernt, weil ..... dafür werden die Ergebnise geprintet

### Datei: oa-get

Update auf Python 3

#### 1. Art der Änderung: Import-Anweisungen hinzugefügt / geändert

Was?

- sqlalchemy, model, urllib

#### 2. Art der Änderung: Hinzufügen von einer database engine und einer session

Was?

- eine database engine und eine Session wurde hinzugefügt, sowie Database tabellen

#### 3. Art der Änderung: Path der source wurde hinzugefügt / try-except geändert

Was?

- Weil manuel?....

#### 4. Art der Änderung: Schreiben einer neuen Funktion

Was?

- Neue Funktion wurde geschrieben: 'check_mime_types'
- Wird benötigt, weil ....

#### 5. Art der Änderung: 'update-mimetypes'

Was?

- Beginn der if-else-Anweisung loops wurde gelöscht
- .all() wurde in die Klammer gesetzt
- hinzufügen eines for-loops, um den file-path zu kontrollieren

#### 6. Art der Änderung: 'download-media'

Was?

- materials wurde session hinzugefügt und dann geprintet, weil......

  

### Datei: model.py

update auf Python 3

#### 1. Art der Änderung: Import-Anweisungen hinzugefügt / geändert

Was?

- sqlalchemy, importlib, sys

#### 2. Art der Änderung: Neu definieren der Funktion 'set_source'

Was?

- anstatt sqllite nutzen von importlib, weil ....

#### 3. Art der Änderung: Definieren neuer Variablen

Was?

- engine --> ...
- Session --> ...
- session --> ...
- Base --> ....

#### 4. Art der Änderung: Änderung in der Klasse 'Journal'

Was?

- anderes Objekt, anstatt Entity nun Base, weil ....
- hinzufügen von 'tablename', weil ...
- deswegen müssen nun auch die Variablen in der Klasse geändert werden, einmal wird bei titel nicht mehr Field() genutzt sondern Column(), da ....
- bei articels

#### 5. Art der Änderung: Hinzufügen der Variable 'article_category'

Was?

- Hier wird nun eine Assoziationstabelle definiert mit dem Namen 'article_category'
- dadurch können Artikel und Kategorien über die Verknüpfungstabelle miteinander verbunden werden.

#### 6. Art der Änderung: Änderung in der Klasse 'Category', 'Article' & 'SupplementaryMaterial'

Was?

- Wieder anstatt Entity Base
- etc.

### Datei: config.py

update auf Python 3

#### 1. Art der Änderung: Path Änderung

Was?

- Ursprünglicher Pfad hat auf den eigenen Laptops nicht funktioniert, jeder musste diesen manuell ändern

#### 2. Art der Änderung: Hinzufügen bei der Funktion 'database_path'

Was?

- sqlite wird beim 'database_path' benötigt, weil ....