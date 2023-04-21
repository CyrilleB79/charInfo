# Zeichen-Informationen #

* Autor: Cyrille Bougot
* NVDA compatibility: 2022.3.3 and beyond
* [Stabile Version herunterladen][1]

This add-on allows to present in a message various information about a
character.

## Presented information

The presented information include the following sections:

* Unicode: information from Unicode norm, i.e. name, CLDR name, value,
  block, etc.
* MS font, only for characters written with proprietary Microsoft fonts
  (Symbol, Wingding 1, 2, 3 and Webding): name and information about the
  equivalent Unicode character.
* NVDA symbol description: information allowing to understand how NVDA
  reports the symbol description. NVDA uses the information in the top most
  rows containing available information to provide the description of a
  symbol.
* NVDA character description: information allowing to understand how NVDA
  reports the character description (e.g. "alpha" for "A"). NVDA uses the
  information in the top most rows containing available information to
  provide the description of a character.


## Befehle

* Nummernblock2 (alle Tastaturschemata) oder NVDA +. (Tastaturschema
  Laptop): Wenn diese Tastenkombination viermal gedrückt wird, werden
  Informationen zum Zeichen des aktuellen Navigatorobjekts angezeigt, in dem
  sich der NVDA-Cursor befindet.
* Unassigned: Presents a message with detailed information on the character
  where the review cursor is situated. If you feel uncomfortable with the
  four press gesture, you may assign to it a gesture in NVDA's input gesture
  dialog ("Text review" category).
* Unassigned: Presents a message with detailed information on the character
  at the position of the caret (works only in places where there is a
  caret). It can be found in the "system caret" category of NVDA input
  gestures dialog.

## Anmerkungen

* Two commands are unassigned by default. They need to be assigned in the
  Input gestures dialog to be used.
* The provided information in the Unicode section is in English since it is
  part of Unicode norm. If a local translation exists for this add-on, the
  information is also provided alongside with English.


## Änderungsprotokoll

### Version 2.1

* Fixed some bugs preventing the character information report to be
  displayed when some options were used.
* Updated localizations.

### Version 2.0

* Enhanced the character information report with information on NVDA symbol
  and NVDA character description.
* Added the support of compound character, e.g. letters with diacritic
  consisting in two or more Unicode characters.
* Update to Unicode 15.0
* Updated French block data.
* Viewing character information is not allowed on lock screen and secure
  screens.
* On Windows lock screen, the script to review the current character can now
  operate normally (single, double or triple press).
* Compatibility with NVDA 2023.1.
* Drops compatibility with NVDA below 2022.3.3. The last version compatible
  with NVDA 2019.3 is the [1.8][downloadVersion1.8].
* Lokalisierungen aktualisiert.

### Version 1.8

* Update auf Unicode 14.0.
* Kompatibel mit NVDA 2022.1.
* Drops compatibility with NVDA below 2019.3. The last version compatible
  with NVDA 2017.3 is the [1.7][downloadVersion1.7].
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

[downloadVersion1.7]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[downloadVersion1.8]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon
