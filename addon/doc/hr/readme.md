# Informacije o znakovima (Character Information) #

* Autor: Cyrille Bougot
* NVDA compatibility: 2022.3.3 and beyond
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]

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


## Naredbe

* Numpad2 (svi tipkovnički rasporedi) ili NVDA+. (raspored prijenosnog
  računala): kad se pritisne 4 puta, prikazuje informacije o znaku
  navigacijskog objekta na kojem se nalazi pregledni pokazivač.
* Unassigned: Presents a message with detailed information on the character
  of the current navigator object where the review cursor is situated. If
  you feel uncomfortable with the four press gesture, you may assign to it a
  gesture in NVDA's input gesture dialog ("Text review" category).
* Unassigned: Presents a message with detailed information on the character
  at the position of the caret (works only in places where there is a
  caret). It can be found in the "system caret" category of NVDA input
  gestures dialog.

## Napomene

* Two commands are unassigned by default. They need to be assigned in the
  Input gestures dialog to be used.
* The provided information in the Unicode section is in English since it is
  part of Unicode norm. If a local translation exists for this add-on, the
  information is also provided alongside with English.


## Dnevnik promjena

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
* Aktualizirane lokalizacije.

### Verzija 1.8

* Aktualiziranje na Unicode 14.0.
* NVDA kompatibilnost: 2022.1.
* Drops compatibility with NVDA below 2019.3. The last version compatible
  with NVDA 2017.3 is the [1.7][downloadVersion1.7].
* Izdanje se sad izvodi zahvaljujući GitHub radnji umjesto appVeyor.
* Aktualizirane lokalizacije.

### Verzija 1.7

* Dodane su lokalizacije.

### Verzija 1.6

* NVDA kompatibilnost: 2021.1.

### Verzija 1.5

* Pripremanje kompatibilnosti s NVDA 2021.1 (doprinos: Lukasz Golonka).
* Nova verzija zajedno sa zadnjim izmjenama u predlošku dodataka.

### Verzija 1.4

* Dodana je skripta za dobivanje informacija za znak na poziciji kursora
  (doprinos: Lukasz Golonka).
* Aktualiziranje na Unicode 13.0.

### Verzija 1.3

* Ispravlja grešku za NVDA 2019.3.


### Verzija 1.2

* Pruža dodatne informacije o znakovima napisanim Microsoftovim fontovima.


### Verzija 1.1

* Nadogradnje za podršku novijih NVDA verzija (kompatibilne s Python
  verzijama 2 i 3)
* Izdanja se sada izrađuju pomoću „appveyor”


### Verzija 1.0

* Prvo izdanje.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev

[downloadVersion1.7]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[downloadVersion1.8]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon
