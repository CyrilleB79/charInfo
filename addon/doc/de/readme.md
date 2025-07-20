# Zeichen-Informationen #

* Autor: Cyrille Bougot
* NVDA-Kompatibilität: 2022.3.3 und neuer

This add-on allows to present in a message various information about a
character.  It also allows to customize the information reported on a
character when using review cursor character navigation commands or multiple
presses of the review character command.

### Features

* Anzeige detaillierter Informationen zu einem bestimmten Zeichen,
  z. B. Unicode-Name, Nummer, CLDR, Symbolname, etc.
* This information can be displayed either at the location of the review
  cursor or at the location of the system cursor.
* Customize the reported information when pressing `numpad2`.
* Use the same custom information when moving the review cursor by
  character.

## Befehle

* `Numpad2` (all keyboard layouts) or `NVDA+.` (laptop layout): when pressed
  4 times, displays information about the character of the current navigator
  object where the review cursor is situated. This command can also be
  customized in the settings of the add-on.
* Unassigned: Presents a message with detailed information on the character
  where the review cursor is situated. If you feel uncomfortable with the
  four press gesture, you may use this command instead.
* Unassigned: Presents a message with detailed information on the character
  at the position of the caret (works only in places where there is a
  caret).
* Unassigned: Opens Character Information add-on settings.

The unassigned commands need first to be assigned in the Input gestures
dialog to be used.

## Detaillierte Informationen über ein bestimmtes Zeichen

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

Die Informationen im Unicode-Abschnitt sind in Englisch, da sie Teil der
Unicode-Norm sind. Wenn es eine lokale Übersetzung für dieser
NVDA-Erweiterung gibt, werden die Informationen auch auf Englisch
bereitgestellt.

Regarding NVDA symbol description section: This add-on does not yet support
custom symbol dictionaries (introduced in NVDA 2024.4).  They already appear
in the list "Options used to compute the symbol" but not in the table
itself.

## Einstellungen

Diese NVDA-Erweiterung hat eine eigene Kategorie in den NVDA-Einstellungen,
in der Sie die folgenden Optionen konfigurieren können.

### Action for multiple presses of the report review character command

The three combo boxes of this group allow to customize what is reported by
the report review character command (`numpad2`) when using two, three or
four presses.  By default, NVDA reports the character description on second
press and its numeric value, decimal and hexadecimal, on third press.  You
can change what is reported on the character at the position of the review
cursor upon multiple presses.  For example, you can report its CLDR English
name on second press, its Unicode name on third press and display detailed
information on it on fourth press.

### Diese Aktionen während der Zeichen-Navigation sich merken

When you have reported specific information with the report review character
command (`numpad2`) called multiple times, you may want to continue
reporting the same information while navigating with the review cursor
(`numpad1` and `numpad3`).  Checking this option will allow you to do it, as
long as you navigate with the review cursor by character just after a
multiple press of `numpad2`.

## Änderungsprotokoll

### Version 3.5

* Partial implementation of the support for custom dictionaries (introduced
  in NVDA 2024.4).
* Fixed Unicode 16.0 support: block names for English and French updated.
* Compatibility with NVDA 2025.1.

### Version 3.4

* Fixed an issue preventing NVDA to run safe scripts on lock screen.

### Version 3.3

* Update to Unicode 16.0.

### Version 3.2

* Bugfix: characters for which only the speech level has been changed do not
  prevent anymore the information report to be displayed.

### Version 3.1

* Fixed an error when there was no value to report for a character.
* Compatibility with NVDA 2024.1.

### Version 3.0

* It is now possible to configure the property reported for the character
  under the review cursor upon multiple presses on `numpad2`. Optionally,
  after having used multiple press on `numpad2`, the last reported property
  can also be reported as long as you navigate by character with the review
  cursor (`numpad1` and `numpad3`).
* Kompatibilität mit NVDA 2024.1 vorbereitet: Unterstützung der
  Sprachausgabe bei Bedarf.
* Behebt mögliche Sicherheitsprobleme im Zusammenhang mit
  [GHSA-xg6w-23rw-39r8][4] bei der Verwendung der NVDA-Erweiterung mit
  älteren NVDA-Versionen. Es wird jedoch empfohlen, NVDA 2023.3.3 oder neuer
  zu verwenden.

### Version 2.6

* Aktualisiert auf Unicode 15.1.
* Hinzufügen von Unterstützung für Python 3.11 zur Vorbereitung der
  Kompatibilität mit NVDA 2024.1.
* Hinweis: Von nun an werden Updates von Übersetzungen nicht mehr im
  Änderungsprotokoll erscheinen.

### Version 2.5

* Fehler beim Importieren mit den letzten NVDA-Alpha-Versionen behoben, NVDA
  2023.2 Entwicklungszyklus (Beitrag Noelia Ruiz Martínez).

### Version 2.4

* Aktualisierte Lokalisierungen.

### Version 2.3

* Aktualisierte Lokalisierungen.

### Version 2.2

* Dev-Kanal entfernt.
* Aktualisierte Lokalisierungen.

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
* Beendet die Kompatibilität mit NVDA älter 2022.3.3. Die letzte mit NVDA
  2019.3 kompatible Version ist die [1.8][3].
* Lokalisierungen aktualisiert.

### Version 1.8

* Update auf Unicode 14.0.
* Kompatibel mit NVDA 2022.1.
* Beendet die Kompatibilität mit NVDA älter 2019.3. Die letzte mit NVDA
  2017.3 kompatible Version ist die [1.7][2].
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

[2]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[3]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon

[4]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
