# Character Information #

* Author: Cyrille Bougot
* NVDA compatibility: 2019.3 and beyond
* Scarica [versione stabile][1]
* Scarica [versione in sviluppo][2]

Questo componente aggiuntivo consente di presentare, in un messaggio,
informazioni sui caratteri come nome unicode, numero, categoria, ecc.


## Comandi

* Numpad2 (tutti i layout di tastiera) o NVDA +. (layout laptop): se premuto
  4 volte, visualizza informazioni sul carattere dell'oggetto del navigatore
  in cui si trova il cursore di revisione.


## Note

* Questo componente aggiuntivo fornisce anche due gesti non assegnati per
  impostazione predefinita:

    * A script to display directly the review cursor character
      information. If you feel unconfortable with the four press gesture,
      you may assign to it a gesture in NVDA's input gesture dialog ("Text
      review" category).
    * A script to display character information for the character at the
      position of the caret (works only in places where there is a
      caret). It can be found in the "system caret" category of NVDA input
      gestures dialog.

* L'informazione fornita è in inglese, perché così è realizzato lo standard
  unicode. Se esiste una localizzazione per questo componente,
  l'informazione viene fornita anche nella lingua locale.
* Per i caratteri scritti con font proprietari di Microsoft, Wingding (1,
  2,, 3) e Webding, viene fornita qualche informazione in più: nome del
  carattere, nome del font e informazioni sul corrispondente carattere
  unicode.


## Novità

### Version 1.8

* Aggiornamento a Unicode 14.0.
* Compatibility with NVDA 2022.1.
* Drops compatibility with NVDA below 2019.3.
* Il rilascio viene ora eseguito grazie a un'azione GitHub anziché appVeyor.
* Aggiornate le traduzioni

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

### Novità nella versione 1.3

* Risolve un problema con NVDA 2019.3.


### Novità nella versione 1.2

* Fornisce informazioni aggiuntive sui caratteri scritti con font Microsoft.


### Novità nella versione 1.1

* Aggiornamenti per supportare le nuove versioni di NVDA (compatible con
  Python 2 e 3)
* Ora i rilasci sono effettuati con appveyor


### Novità nella versione 1.0

* Versione iniziale.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
