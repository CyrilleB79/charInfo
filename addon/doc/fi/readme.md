# Merkin tiedot #

* Tekijä: Cyrille Bougot
* Yhteensopivuus: NVDA 2022.3.3 ja uudemmat
* Lataa [vakaa versio][1]

Tämä lisäosa näyttää merkin tiedot selaustilassa. Sen avulla on myös
mahdollista mukauttaa merkistä puhuttavaa tietoa liikuttaessa merkeittäin
tarkastelukohdistinkomennoilla tai painettaessa useasti Lue
tarkastelukohdistimen kohdalla oleva merkki -komentoa.

### Ominaisuudet

* Näytä merkin yksityiskohtaiset tiedot, esim. Unicode-nimi, numero,
  CLDR-nimi, symbolin nimi jne.
* Tiedot voidaan näyttää joko tarkastelu- tai järjestelmäkohdistimen
  sijainnista.
* Mukauta ``Laskinnäppäimistön 2`` -komennolla puhuttavia tietoja.
* Käytä samoja mukautettuja tietoja siirrettäessä tarkastelukohdistinta
  merkeittäin.

## Komennot

* Laskinnäppäimistön 2 (kaikki näppäinasettelut) tai NVDA+. (kannettavien
  asettelu): Näyttää neljästi painettaessa tietoja merkistä, jonka kohdalla
  tarkastelukohdistin on nykyisessä navigointiobjektissa. Tätä komentoa
  voidaan myös mukauttaa lisäosan asetuksissa.
* Ei määritetty: Komento yksityiskohtaisten tietojen näyttämiseen
  tarkastelukohdistimen kohdalla olevasta merkistä. Mikäli neljän
  painalluksen näppäinkomento tuntuu epämukavalta, voit käyttää tätä
  komentoa sen sijaan.
* Ei määritetty: Komento, joka näyttää yksityiskohtaisia tietoja kohdistimen
  kohdalla olevasta merkistä (toimii vain paikoissa, joissa on kohdistin).
* Ei määritetty: Avaa Merkin tiedot -lisäosan asetukset.

Ei-määritetyt komennot on määritettävä Näppäinkomennot-valintaikkunasta,
jotta niitä voidaan käyttää.

## Merkin yksityiskohtaiset tiedot

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

Näytettävät tiedot ovat englanninkielisiä, koska ne kuuluvat
Unicode-standardiin. Mikäli tälle lisäosalle on käännös paikallisella
kielellä, myös sitä käytetään englannin lisäksi tietojen näyttämiseen.

## Asetukset

Tällä lisäosalla on NVDA:n asetusvalintaikkunassa oma kategoria, jossa voit
määrittää seuraavat asetukset.

### Toiminto Puhu tarkastelukohdistimen kohdalla oleva merkki -komennon useille painalluksille

Tämän ryhmän kolmesta yhdistelmäruudusta voidaan määrittää, mitä Puhu
tarkastelukohdistimen kohdalla oleva merkki -komennolla
(``Laskinnäppäimistön 2``) puhutaan kahta, kolmea tai neljää painallusta
käytettäessä. Oletusarvoisesti NVDA puhuu toisella painalluksella merkin
kuvauksen sekä sen numeerisen arvon ja kolmannella painalluksella
desimaalisen sekä heksadesimaalisen arvon. Voit määrittää, mitä tietoja
tarkastelukohdistimen kohdalla olevasta merkistä puhutaan useilla
painalluksilla. Voit esimerkiksi puhuttaa sen englanninkielisen CLDR-nimen
toisella painalluksella, Unicode-nimen kolmannella ja näyttää
yksityiskohtaiset tiedot neljännellä painalluksella.

### Muista nämä toiminnot merkeittäin liikuttaessa

Kun olet puhuttanut tiettyjä tietoja painamalla useasti Puhu
tarkastelukohdistimen kohdalla oleva merkki -komentoa (``Laskinnäppäimistön
2``), saatat haluta jatkaa samojen tietojen puhumista
tarkastelukohdistimella liikkuessasi (``Laskinnäppäimistön 1`` ja
``Laskinnäppäimistön 3``). Tämän vaihtoehdon valitseminen mahdollistaa sen,
kunhan liikut tarkastelukohdistimella merkeittäin heti usean
``Laskinnäppäimistön 2`` -painalluksen jälkeen.

## Muutosloki

### Versio 3.0

* Nyt on mahdollista määrittää ominaisuus, joka puhutaan
  tarkastelukohdistimen kohdalla olevasta merkistä ``Laskinnäppäimistön 2``
  -komennon useilla painalluksilla. Käytettyäsi tämän komennon useaa
  painallusta, viimeksi puhuttu ominaisuus voidaan myös puhua valinnaisesti,
  kunhan liikut tarkastelukohdistimella merkeittäin ``Laskinnäppäimistön
  1``- ja ``Laskinnäppäimistön 3`` -komentoja käyttäen.
* Valmisteltu yhteensopivuutta NVDA 2024.1:lle: pyydettäessä-puhetilan tuki.
* Ratkaisee mahdolliset [GHSA-xg6w-23rw-39r8][4]:aan liittyvät
  tietoturvaongelmat käytettäessä lisäosaa vanhemmilla NVDA-versioilla. On
  kuitenkin suositeltavaa käyttää NVDA 2023.3.3:ea tai sitä uudempaa
  versiota.

### Versio 2.6

* Päivitys Unicode 15.1:een.
* Lisätty tuki Python 3.11:lle NVDA 2024.1:n tukeen valmistautumiseksi.
* Huom: Tästä lähtien käännöspäivitykset eivät enää näy muutoslokissa.

### Versio 2.5

* Korjattu tuontivirhe uusimmissa NVDA:n alfaversioissa (NVDA 2023.2:n
  kehityssykli, avustanut Noelia Ruiz Martínez).

### Versio 2.4

* Lokalisointeja päivitetty.

### Versio 2.3

* Lokalisointeja päivitetty.

### Versio 2.2

* Dev-kanava poistettu.
* Lokalisointeja päivitetty.

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
  kanssa. Viimeisin NVDA 2019.3:n kanssa yhteensopiva versio on [1.8][3].
* Lokalisointeja päivitetty.

### Versio 1.8

* Päivitys Unicode 14.0:aan.
* Yhteensopivuus NVDA 2022.1:n kanssa.
* Luovuttu yhteensopivuudesta NVDA:n 2019.3:a vanhempien versioiden
  kanssa. Viimeisin NVDA 2017.3:n kanssa yhteensopiva versio on [1.7][2].
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

[1]: https://www.nvaccess.org/addonStore/legacy?file=charInfo

[2]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[3]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon

[4]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
