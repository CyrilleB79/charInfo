# Merkin tiedot #

* Author: Cyrille Bougot
* NVDA compatibility: 2019.3 and beyond
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämän lisäosan avulla on mahdollista näyttää merkin tiedot, kuten
Unicode-nimi, numero, kategoria jne. selattavana viestinä.


## Komennot

* Numeroryhmän 2 (kaikki näppäimistöasettelut) tai NVDA+. (kannettavien
  asettelu): Näyttää neljästi painettaessa tietoja merkistä, jonka kohdalla
  tarkastelukohdistin on nykyisessä navigointiobjektissa.


## Huomautuksia

* This add-on provides also two gestures that are unassigned by default:

    * A script to display directly the review cursor character
      information. If you feel unconfortable with the four press gesture,
      you may assign to it a gesture in NVDA's input gesture dialog ("Text
      review" category).
    * A script to display character information for the character at the
      position of the caret (works only in places where there is a
      caret). It can be found in the "system caret" category of NVDA input
      gestures dialog.

* Näytettävät tiedot ovat englanninkielisiä, koska ne kuuluvat
  Unicode-standardiin. Mikäli tälle lisäosalle on käännös paikallisella
  kielellä, myös sitä käytetään tietojen näyttämiseen.
* Merkeistä, jotka on kirjoitettu Microsoftin omilla Symbol-, Wingding (1,
  2, 3)- tai Webding-fonteilla, näytetään merkin ja fontin nimi sekä
  vastaavan Unicode-merkin tiedot.


## Muutosloki

### Version 1.8

* Update to Unicode 14.0.
* Compatibility with NVDA 2022.1.
* Drops compatibility with NVDA below 2019.3.
* The release is now performed thanks to a GitHub action instead of
  appVeyor.
* Update localizations.

### Version 1.7

* Added localizations.

### Version 1.6

* Compatibility NVDA 2021.1.

### Version 1.5

* Prepare compatibility with NVDA 2021.1 (contribution Lukasz Golonka).
* Update along with last modifications on add-on template.

### Version 1.4

* Added a script to get information for the character at the caret position
  (contribution Lukasz Golonka).
* Update to Unicode 13.0.

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
