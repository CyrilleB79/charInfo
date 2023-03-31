# Character Information #

* Autor: Cyrille Bougot
* NVDA compatibility: 2022.3.3 and beyond
* Descargar [versión estable][1]

This add-on allows to present in a message various information about a
character.

## Presented information

The presented information include the following sections:

* Unicode: information from Unicode norm, i.e. name, CLDR name, value,
  block, etc.
* MS font, only for characters written with proprietary Microsoft fonts
  (Symbol, Wingding 1, 2, 3 and Webding): name and information about the
  equivalent Unicode character.
* NVDA symbol description: information allowing to understand how NVDA
  reports the symbol description. NVDA uses the information in the top most
  rows containing available information to provide the description of a
  symbol.
* NVDA character description: information allowing to understand how NVDA
  reports the character description (e.g. "alpha" for "A"). NVDA uses the
  information in the top most rows containing available information to
  provide the description of a character.


## Ordes

* 2 do teclado numérico (todas as distribucións de teclado) ou
  NVDA+. (distribución de portátil): cando se preme catro veces, amosa
  información sobre o carácter do navegador de obxectos actual onde estea
  situado o cursor de revisión.
* Unassigned: Presents a message with detailed information on the character
  where the review cursor is situated. If you feel uncomfortable with the
  four press gesture, you may assign to it a gesture in NVDA's input gesture
  dialog ("Text review" category).
* Unassigned: Presents a message with detailed information on the character
  at the position of the caret (works only in places where there is a
  caret). It can be found in the "system caret" category of NVDA input
  gestures dialog.

## Notas

* Two commands are unassigned by default. They need to be assigned in the
  Input gestures dialog to be used.
* The provided information in the Unicode section is in English since it is
  part of Unicode norm. If a local translation exists for this add-on, the
  information is also provided alongside with English.


## Rexistro de trocos

### Version 2.1

* Fixed some bugs preventing the character information report to be
  displayed when some options were used.
* Updated localizations.

### Version 2.0


* Enhanced the character information report with information on NVDA symbol
  and NVDA character description.
* Added the support of compound character, e.g. letters with diacritic
  consisting in two or more Unicode characters.
* Update to Unicode 15.0
* Updated French block data.
* Viewing character information is not allowed on lock screen and secure
  screens.
* On Windows lock screen, the script to review the current character can now
  operate normally (single, double or triple press).
* Compatibility with NVDA 2023.1.
* Drops compatibility with NVDA below 2022.3.3. The last version compatible
  with NVDA 2019.3 is the [1.8][downloadVersion1.8].
* Actualizar traduccións.

### Versión 1.8

* Actualización a Unicode 14.0.
* Compatibilidade con NVDA 2022.1.
* Drops compatibility with NVDA below 2019.3. The last version compatible
  with NVDA 2017.3 is the [1.7][downloadVersion1.7].
* A publicación agora faise grazas a unha acción de GitHub no canto de
  appVeyor.
* Actualizar traduccións.

### Versión 1.7

* Engadidas traducións.

### Versión 1.6

* Compatibilidade NVDA 2021.1.

### Versión 1.5

* Preparar compatibilidade con NVDA 2021.1 (contribución Lukasz Golonka).
* Actualizar coas últimas modificacións na plantilla de complementos.

### Versión 1.4

* Engadido un script para obter información para o carácter na posición do
  cursor (contribución Lukasz Golonka).
* Actualización a Unicode 13.0.

### Versión 1.3

* Arranxa un erro con NVDA 2019.3.


### Versión 1.2

* Proporciona información adicional sobre os caracteres escritos con fontes
  de Microsoft.


### Versión 1.1

* Actualizacións para soportar versións máis novas do NVDA (compatible con
  Python 2 e 3)
* As liberacións realízanse agora con Appveyor


### Versión 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=charInfo

[downloadVersion1.7]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[downloadVersion1.8]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon
