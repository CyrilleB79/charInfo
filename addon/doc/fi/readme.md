# Merkin tiedot #

* Tekijä: Cyrille Bougot
* Yhteensopivuus: NVDA 2022.3.3 ja uudemmat
* Lataa [vakaa versio][1]

Tämän lisäosan avulla on mahdollista näyttää merkin tiedot erillisessä
ikkunassa.

## Näytettävät tiedot

Seuraavat tiedot näytetään:

* Unicode: merkin Unicode-tiedot, esim. nimi, CLDR-nimi, arvo, lohko, jne.
* Merkeistä, jotka on kirjoitettu Microsoftin omilla fonteilla (Symbol,
  Wingding 1-3 ja Webding), näytetään merkin ja fontin nimi sekä vastaavan
  Unicode-merkin tiedot.
* NVDA:n symbolitiedot: tiedot, jotka auttavat ymmärtämään, miten NVDA
  ilmoittaa symbolin kuvauksen. NVDA käyttää ylimmillä riveilllä olevia
  tietoja symbolin kuvailuun.
* NVDA:n merkin tiedot: tiedot, jotka auttavat ymmärtämään, miten NVDA
  ilmoittaa merkin kuvauksen (esim. "A" = "Antti"). NVDA käyttää ylimmillä
  riveillä olevaa tietoa merkin kuvailuun.


## Komennot

* Numeroryhmän 2 (kaikki näppäimistöasettelut) tai NVDA+. (kannettavien
  asettelu): Näyttää neljästi painettaessa tietoja merkistä, jonka kohdalla
  tarkastelukohdistin on nykyisessä navigointiobjektissa.
* Ei määritetty: Komento tarkastelukohdistimen kohdalla olevan merkin
  tietojen näyttämiseen. Mikäli neljän painalluksen näppäinkomento tuntuu
  epämukavalta, voit määrittää sille mieleisesi komennon NVDA:n
  Näppäinkomennot-valintaikkunan "Tekstin tarkastelu" -
* Ei määritetty: Skripti, joka näyttää kohdistimen kohdalla olevan merkin
  tiedot (toimii vain paikoissa, joissa on kohdistin). Komento löytyy NVDA:n
  Näppäinkomennot-valintaikkunan "Järjestelmän kohdistin" -kategoriasta.

## Huomautuksia

* Kahta komentoa ei ole oletusarvoisesti määritetty. Ne on määritettävä
  Näppäinkomennot-valintaikkunasta, jotta niitä voidaan käyttää.
* Näytettävät tiedot ovat englanninkielisiä, koska ne kuuluvat
  Unicode-standardiin. Mikäli tälle lisäosalle on käännös paikallisella
  kielellä, myös sitä käytetään englannin lisäksi tietojen näyttämiseen.


## Muutosloki

### Versio 2.1

* Korjattu bugeja, jotka estivät merkin tietojen näyttämisen joitakin
  asetuksia käytettäessä.
* Lokalisointeja päivitetty.

### Versio 2.0


* Merkin tietojen ilmoittamista paranneltu NVDA:n symbolien ja merkkien
  kuvauksilla.
* Lisätty tuki yhdistelmämerkeille, esim. kahdesta tai useammasta merkistä
  koostuville diakriittisille kirjaimille.
* Päivitys Unicode 15.0:aan.
* Ranskankielinen lohko päivitetty.
* Merkin tietojen näyttämistä ei sallita lukitusnäytöllä tai suojatuissa
  ruuduissa.
* Nykyisen merkin lukeva skripti toimii nyt normaalisti (yksi, kaksi tai
  kolme painallusta) Windowsin lukitusnäytössä.
* Yhteensopivuus NVDA 2023.1:n kanssa.
* Luovuttu yhteensopivuudesta NVDA:n 2022.3.3:a vanhempien versioiden
  kanssa. Viimeisin NVDA 2019.3:n kanssa yhteensopiva versio on
  [1.8][downloadVersion1.8].
* Lokalisointeja päivitetty.

### Versio 1.8

* Päivitys Unicode 14.0:aan.
* Yhteensopivuus NVDA 2022.1:n kanssa.
* Luovuttu yhteensopivuudesta NVDA:n 2019.3:a vanhempien versioiden
  kanssa. Viimeisin NVDA 2017.3:n kanssa yhteensopiva versio on
  [1.7][downloadVersion1.7].
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

[1]: https://addons.nvda-project.org/files/get.php?file=charInfo

[downloadVersion1.7]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[downloadVersion1.8]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon
