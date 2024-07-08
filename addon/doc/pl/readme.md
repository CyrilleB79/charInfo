# Character Information #

* Autor: Cyrille Bougot
* Zgodność z NVDA: 2022.3.3 i nowsze
* Pobierz [wersja stabilna][1]

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

## Polecenia

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

Prezentowane informacje obejmują następujące sekcje:

* Unicode: informacje z normy Unicode, tj. nazwa, nazwa CLDR, wartość, blok
  itp.
* MS font, tylko dla znaków zapisanych zastrzeżonymi czcionkami Microsoft
  (Symbol, Wingding 1, 2, 3 i Webding): nazwa i informacje o równoważnym
  znaku Unicode.
* Opis symbolu NVDA: informacje pozwalające zrozumieć, w jaki sposób NVDA
  raportuje opis symbolu. NVDA używa informacji w najwyższych wierszach
  zawierających dostępne informacje w celu dostarczenia opisu symbolu.
* Opis znaku NVDA: informacje pozwalające zrozumieć, w jaki sposób NVDA
  zgłasza opis postaci (np. "alfa" dla "A"). NVDA wykorzystuje informacje w
  najwyższych wierszach zawierających dostępne informacje do opisu postaci.

Informacje podane w sekcji Unicode są w języku angielskim, ponieważ są
częścią normy Unicode. Jeśli istnieje lokalne tłumaczenie tego dodatku,
informacje są również dostarczane wraz z językiem angielskim.

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

## Lista zmian

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

* Zaktualizowane lokalizacje.

### Version 2.3

* Zaktualizowane lokalizacje.

### Version 2.2

* Removed the dev channel.
* Zaktualizowane lokalizacje.

### Wersja 2.1

* Naprawiono kilka błędów uniemożliwiających wyświetlanie raportu z
  informacjami o postaci, gdy niektóre opcje były używane.
* Zaktualizowane lokalizacje.

### Wersja 2.0


* Ulepszono raport informacji o postaci o informacje o symbolu NVDA i opisie
  znaku NVDA.
* Dodano obsługę znaków złożonych, np. liter ze znakami diakrytycznymi
  składającymi się z dwóch lub więcej znaków Unicode.
* Aktualizacja do standardu Unicode 15.0
* Zaktualizowano francuskie dane bloku.
* Wyświetlanie informacji o postaci nie jest dozwolone na ekranie blokady i
  bezpiecznych ekranach.
* Na ekranie blokady systemu Windows skrypt do przeglądania bieżącego znaku
  może teraz działać normalnie (pojedyncze, podwójne lub potrójne
  naciśnięcie).
* Zgodność z NVDA 2023.1
* Drops compatibility with NVDA below 2022.3.3. The last version compatible
  with NVDA 2019.3 is the [1.8][3].
* Zaktualizuj lokalizacje.

### Wersja 1.8

* Aktualizacja do Unicode 14.0.
* Kompatybilność z NVDA 2022.1.
* Drops compatibility with NVDA below 2019.3. The last version compatible
  with NVDA 2017.3 is the [1.7][2].
* Wydanie jest teraz wykonywane dzięki akcji GitHub zamiast appVeyor.
* Zaktualizuj lokalizacje.

### Wersja 1.7

* Dodano tłumaczenia.

### Wersja 1.6

* Kompatybilność NVDA 2021.1.

### Wersja 1.5

* Przygotuj kompatybilność z NVDA 2021.1 (wkład Łukasza Golonki).
* Aktualizacja wraz z ostatnimi modyfikacjami szablonu dodatku.

### Wersja 1.4

* Dodano skrypt, aby uzyskać informacje dla postaci na pozycji karetki
  (wkład Łukasza Golonki).
* Aktualizacja do Unicode 13.0.

### Wersja 1.3

* Naprawiono błąd z NVDA 2019.3.


### Wersja1.2

* Dostarcza dodatkową informację dla znaków napisanych za pomocą czcionek
  Microsoftu.


### Wersja 1.1

* Aktualizacja wsparcia dla nowych wersji  NVDA (Python 2 i 3 zgodny)
* Wersje release są kompilowane z appwejorem


### Wersja 1.0

* Wersja pierwotna.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=charInfo

[2]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[3]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon

[4]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
