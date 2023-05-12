# Zeichen-Informationen #

* Autor: Cyrille Bougot
* NVDA-Kompatibilität: 2022.3.3 und neuer
* [Stabile Version herunterladen][1]

Mit dieser NVDA-Erweiterung können Sie in einer Nachricht verschiedene
Informationen über ein bestimmtes Zeichen erfahren.

## Dargestellte Informationen

Die dargestellten Informationen umfassen die folgenden Abschnitte:

* Unicode: Informationen aus der Unicode-Norm, d. h., Name, CLDR-Name, Wert,
  Block, etc.
* Microsoft-Schriftart, nur für Zeichen, die mit proprietären
  Microsoft-Schriftarten (Symbol, Wingding 1, 2, 3 und Webding) geschrieben
  wurden: Name und Informationen über das entsprechende Unicode-Zeichen.
* Symbol-Beschreibung in NVDA: Informationen, die es ermöglichen, zu
  verstehen, wie NVDA die Symbol-Beschreibung mitteilt. NVDA verwendet die
  Informationen in den obersten Zeilen mit den verfügbaren Informationen, um
  die Beschreibung eines Symbols zu liefern.
* Zeichen-Beschreibung in NVDA: Informationen, die Aufschluss darüber geben,
  wie NVDA die Zeichen-Beschreibung wiedergibt (z. B. "Alpha" für "A"). NVDA
  verwendet die Informationen in den obersten Zeilen mit den verfügbaren
  Informationen, um die Beschreibung eines Zeichens zu liefern.


## Befehle

* Nummernblock2 (alle Tastaturschemata) oder NVDA +. (Tastaturschema
  Laptop): Wenn diese Tastenkombination viermal gedrückt wird, werden
  Informationen zum Zeichen des aktuellen Navigatorobjekts angezeigt, in dem
  sich der NVDA-Cursor befindet.
* Nicht zugewiesen: Zeigt eine Meldung mit detaillierten Informationen zu
  dem Zeichen an, auf dem sich der NVDA-Cursor befindet. Wenn Sie nicht mit
  diesem Tastenbefehl einverstanden sein sollten, können Sie ihn im
  Dialogfeld für die Tastenbefehle in NVDA diese neu zuweisen (Kategorie
  "Text betrachten").
* Nicht zugewiesen: Zeigt eine Meldung mit detaillierten Informationen über
  das Zeichen an der Position der Einfügemarke an (funktioniert nur an
  Stellen, an denen es eine Einfügemarke gibt). Sie finden diese Option in
  der Kategorie "System-Cursor" im Dialogfeld für die Tastenbefehle in NVDA.

## Anmerkungen

* Zwei Befehle sind standardmäßig nicht zugewiesen. Sie sollten diese im
  Dialogfeld für die Tastenbefehle zuweisen, falls Sie diese benutzen
  möchten.
* Die Informationen im Unicode-Abschnitt sind in Englisch, da sie Teil der
  Unicode-Norm sind. Wenn es eine lokale Übersetzung für dieser
  NVDA-Erweiterung gibt, werden die Informationen auch auf Englisch
  bereitgestellt.


## Änderungsprotokoll

### Version 2.1

* Es wurden einige Fehler behoben, die verhinderten, dass die Rückmeldung
  über die Zeichen-Informationen mitgeteilt wurden, wenn einige Optionen
  verwendet wurden.
* Aktualisierte Lokalisierungen.

### Version 2.0

* Die Rückmeldung von Zeichen-Informationen wurde um Informationen von
  Symbolen und Zeichen-Beschreibungen in NVDA erweitert.
* Unterstützung von zusammengesetzten Zeichen, z.B. Buchstaben mit
  diakritischen Zeichen, die aus zwei oder mehr Unicode-Zeichen bestehen.
* Auf Unicode 15.0 aktualisiert
* Aktualisierte französische Blockdaten.
* Die Anzeige von Zeichen-Informationen ist im Sperrbildschirmen und bei
  Sicherheitsmeldungen nicht erlaubt.
* Auf dem Sperrbildschirm von Windows kann das Skript zur Überprüfung des
  aktuellen Zeichens jetzt normal funktionieren (einfaches, doppeltes oder
  dreifaches Drücken).
* Kompatibel mit NVDA 2023.1.
* Beendet die Kompatibilität mit NVDA unter 2022.3.3. Die letzte mit NVDA
  2019.3 kompatible Version ist die [1.8][Version 1.8 direkt herunterladen].
* Lokalisierungen aktualisiert.

### Version 1.8

* Update auf Unicode 14.0.
* Kompatibel mit NVDA 2022.1.
* Beendet die Kompatibilität mit NVDA unter 2019.3. Die letzte mit NVDA
  2017.3 kompatible Version ist die [1.7][Version 1.7 direkt herunterladen].
* Die Versionsveröffentlichung erfolgt nun durch eine GitHub-Aktion anstatt
  appVeyor.
* Lokalisierungen aktualisiert.

### Version 1.7

* Lokalisierungen wurden hinzugefügt.

### Version 1.6

* Kompatibilität NVDA 2021.1.

### Version 1.5

* Kompatibilität mit NVDA 2021.1 vorbereitet (Beitrag Lukasz Golonka).
* Aktualisierungen der Erweiterungsvorlage übernommen.

### Version 1.4

* Es wurde ein Skript hinzugefügt, um zusätzliche Informationen für das
  Zeichen an der Schreibmarke  zu erhalten (Beitrag Lukasz Golonka).
* Update auf Unicode 13.0.

### Version 1.3

* Behebt einen Fehler mit NVDA 2019.3.


### Version 1.2

* Diese Erweiterung stellt zusätzliche Informationen zur Verfügung, die mit
  Microsoft-Schriften geschrieben wurden.


### Version 1.1

* Updates zur Unterstützung neuerer Versionen von NVDA (kompatibel mit
  Python 2 und 3)
* Releases werden jetzt mit Appveyor durchgeführt


### Version 1.0

* Erste Veröffentlichung.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=charInfo

[Version 1.7 direkt
herunterladen](https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon)

[Version 1.8 direkt
herunterladen](https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon)
