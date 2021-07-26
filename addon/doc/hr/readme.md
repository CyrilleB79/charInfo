# Informacije o znakovima (Character Information) #

* Autor: Cyrille Bougot
* NVDA kompatibilnost: 2017.3 do 2021.1
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]

Ovaj dodatak omogućuje predstavljanje informacija o znaku, kao što su nazivi
unikoda, brojevi, kategorije itd.


## Naredbe

* Numpad2 (svi tipkovnički rasporedi) ili NVDA+. (raspored prijenosnog
  računala): kad se pritisne 4 puta, prikazuje informacije o znaku
  navigacijskog objekta na kojem se nalazi pregledni pokazivač.


## Napomene

* Ovaj dodatak također nudi dvije geste koje nisu standardno dodijeljene:

    * Skripta za izravni prikaz informacija o znaku preglednog
      pokazivača. Ovoj skripti nije dodijeljena standardna gesta. Ako ne
      želiš koristiti gestu s četiri pritiska, možeš joj dodijeliti gestu u
      dijaloškom okviru za ulazne geste (kategorija „Pregled teksta”).
    * Skripta za prikaz podataka znaka na položaju pokazivača (radi samo na
      mjestima gdje postoji pokazivač). Može se naći u kategoriji „pokazivač
      sustava” u dijaloškom okviru NVDA čitača za unos gesta.

* Informacije su na engleskom, jer su dio Unicode norme. Ako postoji lokalni
  prijevod za ovaj dodatak, informacije se prikazuju uz engleski jezik.
* CLDR ime (Unicode Common Locale Data Repository) podržano je samo u NVDA
  verziji 2019.1 i novijoj.
* Za znakove koji su napisani s Microsoftovim fontovima Symbol, Wingding (1,
  2, 3) i Webding, pružaju se neke dodatne informacije: ime znaka, ime fonta
  i podaci odgovarajućeg unicode znaka.


## Dnevnik promjena

### Verzija 1.6

* NVDA kompatibilnost: 2021.1

### Verzija 1.5

* Prepare compatibility with NVDA 2021.1 (contribution Lukasz Golonka).
* Update along with last modifications on add-on template.

### Verzija 1.4

* Added a script to get information for the character at the caret position
  (contribution Lukasz Golonka).
* Update to Unicode 13.0.

### Verzija 1.3

* Fixes a bug with NVDA 2019.3.


### Verzija 1.2

* Provides additional information on characters written with Microsoft
  fonts.


### Verzija 1.1

* Nadogradnje za podršku novijih NVDA verzija (kompatibilne s Python
  verzijama 2 i 3)
* Izdanja se sada izrađuju pomoću „appveyor”


### Verzija 1.0

* Prvo izdanje.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
