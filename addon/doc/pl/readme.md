# Character Information #

* Autor: Cyrille Bougot
* Zgodność z wersjami NVDA: 2019.3 i nowszych
* Pobierz [wersja stabilna][1]
* Pobierz [Wersja rozwojowa][2]

Ten dodatek umożliwia wyświetlanie informacji o znaku w oknie tekstowym
takich jak nazwa Unicode, liczba, kategoria, itd.


## Polecenia

* Numpad2 (wszystkie układy klawiatury) lub NVDA+. (układ dla komputerów
  przenośnych): Gdy jest naciśnięte czterokrotnie, wyświetla informację o
  znaku pod obiektem nawigatora gdzie się znajduje kursor przeglądu.


## Uwagi

* Ten dodatek udostępnia również dwa gesty, które domyślnie nie są
  przypisane:

    * Skrypt wyświetlający bezpośrednio informacje o znaku kursora
      recenzji. Jeśli czujesz się nieswojo z gestem czterech naciśnij,
      możesz przypisać do niego gest w oknie dialogowym gestu wejściowego
      NVDA (kategoria "Przegląd tekstu").
    * Skrypt do wyświetlania informacji o znaku dla znaku w pozycji karetki
      (działa tylko w miejscach, w których znajduje się karetka). Można go
      znaleźć w kategorii "karetka systemu" w oknie dialogowym gestów
      wejściowych NVDA.

* Informacja dostarczana jest po angielsku, gdyś jes ta informacja częścią
  normy unicode. Jeżeli istnieje lokalne tłumaczenie dla tego dodatku,
  informacja jest podawana raz z angielską jej wersją.
* Dla zkaków napisanych symbolem Microsoftowych fontów proprietarnych,
  Wingding (1, 2,, 3) i Webding, Niektóre dodatkowe informacje są
  dostarczane: nazwa znaku, nazwa fontu i informacja o aktualnym znaku
  Unicode.


## Lista zmian

### Wersja 1.8

* Aktualizacja do Unicode 14.0.
* Kompatybilność z NVDA 2022.1.
* Spada kompatybilność z NVDA poniżej 2019.3.
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

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
