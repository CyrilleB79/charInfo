# Merkin tiedot #

* Tekijä: Cyrille Bougot
* Yhteensopivuus: NVDA 2022.3.3 ja uudemmat
* Lataa [vakaa versio][1]

This add-on allows to present in a message various information about a
character.  It also allows to customize the information reported on a
character when using review cursor character navigation commands or multiple
presses of the review character command.

### Features

* Display detailed information on a character, e.g. Unicode name, number,
  CLDR, symbol name, etc.
* This information can be displayed either at the location of the review
  cursor or at the location of the system cursor.
* Customize the reported information when pressing `numpad2`.
* Use the same custom information when moving the review cursor by
  character.

## Komennot

* `Numpad2` (all keyboard layouts) or `NVDA+.` (laptop layout): when pressed
  4 times, displays information about the character of the current navigator
  object where the review cursor is situated. This command can also be
  customized in the settings of the add-on.
* Unassigned: Presents a message with detailed information on the character
  where the review cursor is situated. If you feel uncomfortable with the
  four press gesture, you may use this command instead.
* Unassigned: Presents a message with detailed information on the character
  at the position of the caret (works only in places where there is a
  caret).
* Unassigned: Opens Character Information add-on settings.

The unassigned commands need first to be assigned in the Input gestures
dialog to be used.

## Detailed information on a character

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

## Settings

This add-on has its own category in NVDA's settings dialog where you can
configure the following options.

### Action for multiple presses of the report review character command

The three combo boxes of this group allow to customize what is reported by
the report review character command (`numpad2`) when using two, three or
four presses.  By default, NVDA reports the character description on second
press and its numeric value, decimal and hexadecimal, on third press.  You
can change what is reported on the character at the position of the review
cursor upon multiple presses.  For example, you can report its CLDR English
name on second press, its Unicode name on third press and display detailed
information on it on fourth press.

### Remember these action during character navigation

When you have reported specific information with the report review character
command (`numpad2`) called multiple times, you may want to continue
reporting the same information while navigating with the review cursor
(`numpad1` and `numpad3`).  Checking this option will allow you to do it, as
long as you navigate with the review cursor by character just after a
multiple press of `numpad2`.

## Muutosloki

### Version 3.0

* It is now possible to configure the property reported for the character
  under the review cursor upon multiple presses on `numpad2`. Optionally,
  after having used multiple press on `numpad2`, the last reported property
  can also be reported as long as you navigate by character with the review
  cursor (`numpad1` and `numpad3`).
* Prepares compatibility with NVDA 2024.1: speech on-demand support.
* Addresses potential security issues related to [GHSA-xg6w-23rw-39r8][4]
  when using the add-on with older versions of NVDA. However, it is
  recommended to use NVDA 2023.3.3 or higher.

### Version 2.6

* Update to Unicode 15.1.
* Adds support for Python 3.11 to prepare compatibility with NVDA 2024.1.
* Note: From now on, translation updates will not appear anymore in the
  change log.

### Version 2.5

* Fixed import error with last NVDA alpha versions, NVDA 2023.2 development
  cycle (contribution Noelia Ruiz Mart�nez).

### Version 2.4

* Lokalisointeja päivitetty.

### Version 2.3

* Lokalisointeja päivitetty.

### Version 2.2

* Removed the dev channel.
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
* Drops compatibility with NVDA below 2022.3.3. The last version compatible
  with NVDA 2019.3 is the [1.8][3].
* Lokalisointeja päivitetty.

### Versio 1.8

* Päivitys Unicode 14.0:aan.
* Yhteensopivuus NVDA 2022.1:n kanssa.
* Drops compatibility with NVDA below 2019.3. The last version compatible
  with NVDA 2017.3 is the [1.7][2].
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
