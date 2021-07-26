# Character Information #

* Author: Cyrille Bougot
* NVDA compatibility: 2017.3 to 2021.1
* Pobierz [wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]

Ten dodatek umożliwia wyświetlanie informacji o znaku w oknie tekstowym
takich jak nazwa Unicode, liczba, kategoria, itd.


## Polecenia

* Numpad2 (wszystkie układy klawiatury) lub NVDA+. (układ dla komputerów
  przenośnych): Gdy jest naciśnięte czterokrotnie, wyświetla informację o
  znaku pod obiektem nawigatora gdzie się znajduje kursor przeglądu.


## Uwagi

* This add-on provides also two gestures that are unassigned by default:

    * A script to display directly the review cursor character
      information. If you feel unconfortable with the four press gesture,
      you may assign to it a gesture in NVDA's input gesture dialog ("Text
      review" category).
    * A script to display character information for the character at the
      position of the caret (works only in places where there is a
      caret). It can be found in the "system caret" category of NVDA input
      gestures dialog.

* Informacja dostarczana jest po angielsku, gdyś jes ta informacja częścią
  normy unicode. Jeżeli istnieje lokalne tłumaczenie dla tego dodatku,
  informacja jest podawana raz z angielską jej wersją.
* CLDR name (współdzielone repozytorium znaków unicode) jest wspierane tylko
  od wersji NVDA 2019.1 i wyższych.
* Dla zkaków napisanych symbolem Microsoftowych fontów proprietarnych,
  Wingding (1, 2,, 3) i Webding, Niektóre dodatkowe informacje są
  dostarczane: nazwa znaku, nazwa fontu i informacja o aktualnym znaku
  Unicode.


## Lista zmian

### Version 1.6

* Compatibility NVDA 2021.1.

### Version 1.5

* Prepare compatibility with NVDA 2021.1 (contribution Lukasz Golonka).
* Update along with last modifications on add-on template.

### Version 1.4

* Added a script to get information for the character at the caret position
  (contribution Lukasz Golonka).
* Update to Unicode 13.0.

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

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
