# Character information

* Author: Cyrille Bougot
* NVDA compatibility: 2022.3.3 and beyond

This add-on allows to present in a message various information about a character.
It also allows to customize the information reported on a character when using review cursor character navigation commands or multiple presses of the review character command.

### Features

* Display detailed information on a character, e.g. Unicode name, number, CLDR, symbol name, etc.
* This information can be displayed either at the location of the review cursor or at the location of the system cursor.
* Customize the reported information when pressing `numpad2`.
* Use the same custom information when moving the review cursor by character.

## Commands

* `Numpad2` (all keyboard layouts) or `NVDA+.` (laptop layout): when pressed 4 times, displays information about the character of the current navigator object where the review cursor is situated. This command can also be customized in the settings of the add-on.
* Unassigned: Presents a message with detailed information on the character where the review cursor is situated. If you feel uncomfortable with the four press gesture, you may use this command instead.
* Unassigned: Presents a message with detailed information on the character at the position of the caret (works only in places where there is a caret).
* Unassigned: Opens Character Information add-on settings.

The unassigned commands need first to be assigned in the Input gestures dialog to be used.

## Detailed information on a character

The presented information include the following sections:

* Unicode: information from Unicode norm, i.e. name, CLDR name, value, block, etc.
* MS font, only for characters written with proprietary Microsoft fonts (Symbol, Wingding 1, 2, 3 and Webding): name and information about the equivalent Unicode character.
* NVDA symbol description: information allowing to understand how NVDA reports the symbol description. NVDA uses the information in the top most rows containing available information to provide the description of a symbol.
* NVDA character description: information allowing to understand how NVDA reports the character description (e.g. "alpha" for "A"). NVDA uses the information in the top most rows containing available information to provide the description of a character.

The provided information in the Unicode section is in English since it is part of Unicode norm. If a local translation exists for this add-on, the information is also provided alongside with English.

Regarding NVDA symbol description section: This add-on does not yet support custom symbol dictionaries (introduced in NVDA 2024.4).
They already appear in the list "Options used to compute the symbol" but not in the table itself.

## Settings

This add-on has its own category in NVDA's settings dialog where you can configure the following options.

### Action for multiple presses of the report review character command

The three combo boxes of this group allow to customize what is reported by the report review character command (`numpad2`) when using two, three or four presses.
By default, NVDA reports the character description on second press and its numeric value, decimal and hexadecimal, on third press.
You can change what is reported on the character at the position of the review cursor upon multiple presses.
For example, you can report its CLDR English name on second press, its Unicode name on third press and display detailed information on it on fourth press.

### Remember these action during character navigation

When you have reported specific information with the report review character command (`numpad2`) called multiple times, you may want to continue reporting the same information while navigating with the review cursor (`numpad1` and `numpad3`).
Checking this option will allow you to do it, as long as you navigate with the review cursor by character just after a multiple press of `numpad2`.

## Change log

### Version 3.5

* Partial implementation of the support for custom dictionaries (introduced in NVDA 2024.4).
* Fixed Unicode 16.0 support: block names for English and French updated.
* Compatibility with NVDA 2025.1.

### Version 3.4

* Fixed an issue preventing NVDA to run safe scripts on lock screen.

### Version 3.3

* Update to Unicode 16.0.

### Version 3.2

* Bugfix: characters for which only the speech level has been changed do not prevent anymore the information report to be displayed.

### Version 3.1

* Fixed an error when there was no value to report for a character.
* Compatibility with NVDA 2024.1.

### Version 3.0

* It is now possible to configure the property reported for the character under the review cursor upon multiple presses on `numpad2`. Optionally, after having used multiple press on `numpad2`, the last reported property can also be reported as long as you navigate by character with the review cursor (`numpad1` and `numpad3`).
* Prepares compatibility with NVDA 2024.1: speech on-demand support.
* Addresses potential security issues related to [GHSA-xg6w-23rw-39r8][4] when using the add-on with older versions of NVDA. However, it is recommended to use NVDA 2023.3.3 or higher.

### Version 2.6

* Update to Unicode 15.1.
* Adds support for Python 3.11 to prepare compatibility with NVDA 2024.1.
* Note: From now on, translation updates will not appear anymore in the change log.

### Version 2.5

* Fixed import error with last NVDA alpha versions, NVDA 2023.2 development cycle (contribution Noelia Ruiz Martínez).

### Version 2.4

* Updated localizations.

### Version 2.3

* Updated localizations.

### Version 2.2

* Removed the dev channel.
* Updated localizations.

### Version 2.1

* Fixed some bugs preventing the character information report to be displayed when some options were used.
* Updated localizations.

### Version 2.0


* Enhanced the character information report with information on NVDA symbol and NVDA character description.
* Added the support of compound character, e.g. letters with diacritic consisting in two or more Unicode characters.
* Update to Unicode 15.0
* Updated French block data.
* Viewing character information is not allowed on lock screen and secure screens.
* On Windows lock screen, the script to review the current character can now operate normally (single, double or triple press).
* Compatibility with NVDA 2023.1.
* Drops compatibility with NVDA below 2022.3.3. The last version compatible with NVDA 2019.3 is the [1.8][3].
* Update localizations.

### Version 1.8

* Update to Unicode 14.0.
* Compatibility with NVDA 2022.1.
* Drops compatibility with NVDA below 2019.3. The last version compatible with NVDA 2017.3 is the [1.7][2].
* The release is now performed thanks to a GitHub action instead of appVeyor.
* Update localizations.

### Version 1.7

* Added localizations.

### Version 1.6

* Compatibility NVDA 2021.1.

### Version 1.5

* Prepare compatibility with NVDA 2021.1 (contribution Lukasz Golonka).
* Update along with last modifications on add-on template.

### Version 1.4

* Added a script to get information for the character at the caret position (contribution Lukasz Golonka).
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

[2]: https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[3]: https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon

[4]: https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
