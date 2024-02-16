# Zeichen-Informationen #

* Autor: Cyrille Bougot
* NVDA-Kompatibilität: 2022.3.3 und neuer
* [Stabile Version herunterladen][1]

This add-on allows to present in a message various information about a
character.  It also allows to customize the information reported on a
character when using review cursor character navigation commands or multiple
presses of the review character command.

### Features

* Display detailed information on a character, e.g. Unicode name, number,
  CLDR, symbol name, etc.
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

## Detailed information on a character

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

## Settings

This add-on has its own category in NVDA's settings dialog where you can
configure the following options.

### Action for multiple presses of the report review character command

The three combo boxes of this group allow to customize what is reported by
the report review character command (`numpad2`) when using two, three or
four presses.  By default, NVDA reports the character description on second
press and its numeric value, decimal and hexadecimal, on third press.  You
can change what is reported on the character at the position of the review
cursor upon multiple presses.  For example, you can report its CLDR English
name on second press, its Unicode name on third press and display detailed
information on it on fourth press.

### Remember these action during character navigation

When you have reported specific information with the report review character
command (`numpad2`) called multiple times, you may want to continue
reporting the same information while navigating with the review cursor
(`numpad1` and `numpad3`).  Checking this option will allow you to do it, as
long as you navigate with the review cursor by character just after a
multiple press of `numpad2`.

## Änderungsprotokoll

### Version 3.0

* It is now possible to configure the property reported for the character
  under the review cursor upon multiple presses on `numpad2`. Optionally,
  after having used multiple press on `numpad2`, the last reported property
  can also be reported as long as you navigate by character with the review
  cursor (`numpad1` and `numpad3`).
* Prepares compatibility with NVDA 2024.1: speech on-demand support.
* Addresses potential security issues related to [GHSA-xg6w-23rw-39r8][4]
  when using the add-on with older versions of NVDA. However, it is
  recommended to use NVDA 2023.3.3 or higher.

### Version 2.6

* Update to Unicode 15.1.
* Adds support for Python 3.11 to prepare compatibility with NVDA 2024.1.
* Note: From now on, translation updates will not appear anymore in the
  change log.

### Version 2.5

* Fixed import error with last NVDA alpha versions, NVDA 2023.2 development
  cycle (contribution Noelia Ruiz Mart�nez).

### Version 2.4

* Aktualisierte Lokalisierungen.

### Version 2.3

* Aktualisierte Lokalisierungen.

### Version 2.2

* Removed the dev channel.
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
* Drops compatibility with NVDA below 2022.3.3. The last version compatible
  with NVDA 2019.3 is the [1.8][3].
* Lokalisierungen aktualisiert.

### Version 1.8

* Update auf Unicode 14.0.
* Kompatibel mit NVDA 2022.1.
* Drops compatibility with NVDA below 2019.3. The last version compatible
  with NVDA 2017.3 is the [1.7][2].
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

[2]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[3]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon

[4]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
