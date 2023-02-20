# Merkin tiedot #

* Tekijä: Cyrille Bougot
* Yhteensopivuus: NVDA 2019.3 ja uudemmat
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämän lisäosan avulla on mahdollista näyttää merkin tiedot, kuten
Unicode-nimi, numero, kategoria jne. selattavana viestinä.


## Komennot

* Numeroryhmän 2 (kaikki näppäimistöasettelut) tai NVDA+. (kannettavien
  asettelu): Näyttää neljästi painettaessa tietoja merkistä, jonka kohdalla
  tarkastelukohdistin on nykyisessä navigointiobjektissa.


## Huomautuksia

* Tämä lisäosa tarjoaa myös kaksi näppäinkomentoa, joita ei ole
  oletusarvoisesti määritetty:

    * Komento suoraan tarkastelukohdistimen kohdalla olevan merkin tietojen
      näyttämiseen. Komennolle ei ole määritetty oletusarvoista
      näppäinkomentoa. Mikäli neljän painalluksen näppäinkomento tuntuu
      epämukavalta, voit määrittää sille mieleisesi näppäinkomennon NVDA:n
      Näppäinkomennot-valintaikkunan "Tekstin tarkastelu" -kategoriasta.
    * Skripti, joka näyttää kohdalla olevan merkin tiedot (toimii vain
      paikoissa, joissa on kohdistin). Komento löytyy NVDA:n
      Näppäinkomennot-valintaikkunan "Järjestelmän kohdistin" -kategoriasta.

* Näytettävät tiedot ovat englanninkielisiä, koska ne kuuluvat
  Unicode-standardiin. Mikäli tälle lisäosalle on käännös paikallisella
  kielellä, myös sitä käytetään tietojen näyttämiseen.
* Merkeistä, jotka on kirjoitettu Microsoftin omilla Symbol-, Wingding (1,
  2, 3)- tai Webding-fonteilla, näytetään merkin ja fontin nimi sekä
  vastaavan Unicode-merkin tiedot.


## Muutosloki

### Versio 1.8

* Päivitys Unicode 14.0:aan.
* Yhteensopivuus NVDA 2022.1:n kanssa.
* NVDA 2019.3:a vanhempia versioita ei enää tueta.
* Julkaisu suoritetaan nyt appVeyorin sijasta GitHub-toiminnolla.
* Lokalisointeja päivitetty.

### Versio 1.7

* Lokalisointeja lisätty.

### Versio 1.6

* Yhteensopiva NVDA 2021.1:n kanssa.

### Versio 1.5

* Yhteensopivuus NVDA 2021.1:n kanssa (avustanut Lukasz Golonka).
* Päivitys viimeisimmillä lisäosamallin muutoksilla.

### Versio 1.4

* Lisätty skripti kohdistimen kohdalla olevan merkin tietojen saamiseen
  (avustanut Lukasz Golonka).
* Päivitys Unicode 13.0:aan.

### Versio 1.3

* Korjattu NVDA 2019.3:a käytettäessä ilmennyt bugi.


### Versio 1.2

* Näyttää lisätietoa Microsoft-fonteilla kirjoitetuista merkeistä.


### Versio 1.1

* Päivityksiä uudempien NVDA-versioiden tukemiseksi (Python 2- ja 3
  -yhteensopiva)
* Julkaisut suoritetaan nyt appveyorilla


### Versio 1.0

* Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
