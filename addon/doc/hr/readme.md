# Informacije o znakovima (Character Information) #

* Autor: Cyrille Bougot
* NVDA kompatibilnost: 2022.3.3 i novije verzije
* Preuzmi [stabilnu verziju][1]

Ovaj dodatak omogućuje predstavljanje raznih informacija o znaku u poruci.

## Prikazane informacije

Prikazane informacije uključuju sljedeće odjeljke:

* Unicode: informacije iz Unicode norme, npr. ime, CLDR ime, vrijednost,
  blok itd.
* MS font, samo za znakove koji su napisani s Microsoftovim fontovima
  (Symbol, Wingding 1, 2, 3 i Webding): ime i informacije odgovarajućeg
  unicode znaka.
* NVDA opis simbola: informacije koje omogućuju razumijevanje kako NVDA
  izvještava opis simbola. NVDA koristi informacije u najgornjim redcima
  koji sadrže dostupne informacije za pružanje opisa simbola.
* NVDA opis znakova: informacije koje omogućuju razumijevanje kako NVDA
  izvještava opis znakova (npr. „alfa” za „A”). NVDA koristi informacije u
  najgornjim redcima koji sadrže dostupne informacije za pružanje opisa
  znakova.


## Naredbe

* Numpad2 (svi tipkovnički rasporedi) ili NVDA+. (raspored prijenosnog
  računala): kad se pritisne 4 puta, prikazuje informacije o znaku
  navigacijskog objekta na kojem se nalazi pregledni pokazivač.
* Nedodijeljeno: Prikazuje poruku s detaljnim informacijama o znaku na kojem
  se nalazi pregledni kursor. Ako ne želiš koristiti gestu s četiri
  pritiska, možeš joj dodijeliti gestu u dijaloškom okviru za ulazne geste
  (kategorija „Pregled teksta”).
* Nedodijeljeno: Prikazuje poruku s detaljnim informacijama o znaku na
  mjestu kursora (radi samo na mjestima gdje postoji kursor). Može se
  pronaći u kategoriji „kursor sustava” u dijaloškom okviru NVDA čitača za
  ulazne geste.

## Napomene

* Dvije naredbe standardno nisu dodijeljene. Da bi se koristile, moraju se
  dodijeliti u dijaloškom okviru „Ulazne geste”.
* Informacije u Unicode odjeljku su na engleskom jeziku jer su dio Unicode
  norme. Ako postoji lokalni prijevod za ovaj dodatak, informacije se
  također prikazuju uz engleski jezik.


## Dnevnik promjena

### Verzija 2.1

* Fixed some bugs preventing the character information report to be
  displayed when some options were used.
* Aktualizirane lokalizacije.

### Verzija 2.0

* Enhanced the character information report with information on NVDA symbol
  and NVDA character description.
* Added the support of compound character, e.g. letters with diacritic
  consisting in two or more Unicode characters.
* Aktualiziranje na Unicode 15.0
* Updated French block data.
* Viewing character information is not allowed on lock screen and secure
  screens.
* On Windows lock screen, the script to review the current character can now
  operate normally (single, double or triple press).
* Kompatibilnost s NVDA verzijom 2023.1.
* Ukida kompatibilnost s ranijim NVDA verzijama od 2022.3.3. Zadnja verzija
  kompatibilna s NVDA 2019.3 je [1.8][preuzmi verziju 1.8].
* Aktualizirane lokalizacije.

### Verzija 1.8

* Aktualiziranje na Unicode 14.0.
* NVDA kompatibilnost: 2022.1.
* Ukida kompatibilnost s ranijim NVDA verzijama od 2019.3. Zadnja verzija
  kompatibilna s NVDA 2017.3 je [1.7][preuzmi verziju 1.7].
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

[1]: https://www.nvaccess.org/addonStore/legacy?file=charInfo

[preuzmi verziju 1.7]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[preuzmi verziju 1.8]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon
