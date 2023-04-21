# Character Information #

* Autor: Cyrille Bougot
* Zgodność z NVDA: 2022.3.3 i nowsze
* Pobierz [wersja stabilna][1]

Dodatek ten pozwala na przedstawienie w wiadomości różnych informacji o
postaci.

## Prezentowane informacje

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


## Polecenia

* Numpad2 (wszystkie układy klawiatury) lub NVDA+. (układ dla komputerów
  przenośnych): Gdy jest naciśnięte czterokrotnie, wyświetla informację o
  znaku pod obiektem nawigatora gdzie się znajduje kursor przeglądu.
* Nieprzypisane: Wyświetla komunikat ze szczegółowymi informacjami o znaku,
  na którym znajduje się kursor recenzji. Jeśli czujesz się niekomfortowo z
  czterema gestami naciśnięcia, możesz przypisać do niego gest w oknie
  dialogowym gestów wejściowych NVDA (kategoria "Przegląd tekstu").
* Nieprzypisany: Wyświetla komunikat ze szczegółowymi informacjami o postaci
  w pozycji daszka (działa tylko w miejscach, w których znajduje się
  daszek). Można go znaleźć w kategorii "kaseta systemowa" w oknie
  dialogowym gestów wejściowych NVDA.

## Uwagi

* Domyślnie dwa polecenia nie są przypisane. Muszą być przypisane w oknie
  dialogowym Gesty wejściowe, które mają być używane.
* Informacje podane w sekcji Unicode są w języku angielskim, ponieważ są
  częścią normy Unicode. Jeśli istnieje lokalne tłumaczenie tego dodatku,
  informacje są również dostarczane wraz z językiem angielskim.


## Lista zmian

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
* Spada kompatybilność z NVDA poniżej 2022.3.3. Ostatnia wersja kompatybilna
  z NVDA 2019.3 to [1.8][downloadVersion1.8].
* Zaktualizuj lokalizacje.

### Wersja 1.8

* Aktualizacja do Unicode 14.0.
* Kompatybilność z NVDA 2022.1.
* Spada kompatybilność z NVDA poniżej 2019.3. Ostatnia wersja kompatybilna z
  NVDA 2017.3 to [1.7][downloadVersion1.7].
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

[downloadVersion1.7]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[downloadVersion1.8]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon
