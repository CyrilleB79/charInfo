# Informacije o znakovima (Character Information) #

* Autor: Cyrille Bougot
* NVDA kompatibilnost: 2019.3 i novije verzije
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
* Za znakove koji su napisani s Microsoftovim fontovima Symbol, Wingding (1,
  2, 3) i Webding, pružaju se neke dodatne informacije: ime znaka, ime fonta
  i podaci odgovarajućeg unicode znaka.


## Dnevnik promjena

### Verzija 1.8

* Aktualiziranje na Unicode 14.0.
* NVDA kompatibilnost: 2022.1.
* Nepodržavanje NVDA kompatibilnosti za verziju  2019.3.
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
