# Character information

* Author: Cyrille Bougot
* NVDA compatibility: 2017.3 to 2021.1
* Download [stable version][1]
* Download [development version][2]

This add-on allows to present in a message character information such as unicode name, number, category, etc.


## Commands

* Numpad2 (all keyboard layouts) or NVDA+. (laptop layout): when pressed 4 times, displays information about the character of the current navigator object where the review cursor is situated.


## Notes

* This add-on provides also two gestures that are unassigned by default:

    * A script to display directly the review cursor character information. If you feel unconfortable with the four press gesture, you may assign to it a gesture in NVDA's input gesture dialog ("Text review" category).
    * A script to display character information for the character at the position of the caret (works only in places where there is a caret). It can be found in the "system caret" category of NVDA input gestures dialog.

* The provided information is in english since it is part of Unicode norm. If a local translation exists for this add-on, the information is also provided alongside with english.
* The CLDR name (Unicode Common Locale Data Repository) is only supported with NVDA 2019.1 and above.
* For the characters written with Microsoft proprietary fonts Symbol, Wingding (1, 2,, 3) and Webding, some additional information is provided: character name, font name and information of the corresponding unicode character.


## Change log

### Version 1.7

* Added localizations.

### Version 1.6

* Compatibility NVDA 2021.1.

### Version 1.5

* Prepare compatibility with NVDA 2021.1 (contribution Łukasz Golonka).
* Update along with last modifications on add-on template.

### Version 1.4

* Added a script to get information for the character at the caret position (contribution Łukasz Golonka).
* Update to Unicode 13.0.

### Version 1.3

* Fixes a bug with NVDA 2019.3.


### Version 1.2

* Provides additional information on characters written with Microsoft fonts.


### Version 1.1

* Updates to support newer versions of NVDA (Python 2 and 3 compatible)
* Releases performed now with appveyor


### Version 1.0

* Initial release.

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
