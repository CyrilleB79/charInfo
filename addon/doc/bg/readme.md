# Информация за знаците (Character information) #

* Автор: Cyrille Bougot
* Съвместимост с NVDA: от 2022.3.3 и по-нови версии

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

## Команди

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

Представената информация включва следните раздели:

* Уникод: информация от Уникод стандарта, т.е. име, CLDR име, стойност, блок
  и т.н.
* MS шрифт, само за знаци, написани със собствени шрифтове на Microsoft
  (Symbol, Wingding 1, 2, 3 и Webding): име и информация за еквивалентния
  Уникод знак.
* Описание на символа от NVDA: информация, позволяваща да се разбере как
  NVDA докладва описанието на символа. NVDA използва информацията в
  най-горните редове, съдържащи налична информация, за да предостави
  описание на символа.
* Описание на знака от NVDA: информация, позволяваща да се разбере как NVDA
  докладва описанието на знака (напр. "алфа" за "A"). NVDA използва
  информацията в най-горните редове, съдържащи налична информация, за да
  предостави описание на знака.

Предоставената информация в Уникод раздела е на английски език, тъй като е
част от Уникод стандарта. Ако за тази добавка съществува местен превод,
информацията се предоставя и на местния език заедно с тази на английски.

Regarding NVDA symbol description section: This add-on does not yet support
custom symbol dictionaries (introduced in NVDA 2024.4).  They already appear
in the list "Options used to compute the symbol" but not in the table
itself.

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

## Списък с промените

### Version 3.5

* Partial implementation of the support for custom dictionaries (introduced
  in NVDA 2024.4).
* Fixed Unicode 16.0 support: block names for English and French updated.
* Compatibility with NVDA 2025.1.

### Version 3.4

* Fixed an issue preventing NVDA to run safe scripts on lock screen.

### Version 3.3

* Update to Unicode 16.0.

### Version 3.2

* Bugfix: characters for which only the speech level has been changed do not
  prevent anymore the information report to be displayed.

### Version 3.1

* Fixed an error when there was no value to report for a character.
* Compatibility with NVDA 2024.1.

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

* Обновени преводи.

### Version 2.3

* Обновени преводи.

### Version 2.2

* Removed the dev channel.
* Обновени преводи.

### Версия 2.1

* Поправени са някои грешки, които пречат на показването на доклада с
  информация за знаците, когато са използвани някои опции.
* Обновени преводи.

### Версия 2.0


* Подобрено е докладването с информация за символи с информация за символа
  от NVDA и описанието на знака от NVDA.
* Добавена е поддръжка за съставни знаци, напр. букви с диакритика, състоящ
  се от два или повече Unicode знака.
* Обновено до Уникод 15.0
* Обновени са френските блок данни.
* Преглеждането на информация за символи бива забранено на заключен екран и
  защитени екрани.
* На заключения екран на Windows скриптът за преглед на текущия знак вече
  може да работи нормално (еднократно, двукратно или трикратно натискане).
* Съвместимост с NVDA 2023.1.
* Drops compatibility with NVDA below 2022.3.3. The last version compatible
  with NVDA 2019.3 is the [1.8][3].
* Обновени преводи.

### Версия 1.8

* Обновено до Unicode 14.0.
* Съвместимост с NVDA 2022.1.
* Drops compatibility with NVDA below 2019.3. The last version compatible
  with NVDA 2017.3 is the [1.7][2].
* Издаването вече се изпълнява посредством действие на GitHub вместо
  AppVeyor.
* Обновени преводи.

### Версия 1.7

* Добавени преводи.

### Версия 1.6

* Съвместимост с NVDA 2021.1.

### Версия 1.5

* Подготовка за съвместимост с NVDA 2021.1 (принос от Lukasz Golonka).
* Обновяване заедно с последните промени в шаблона за добавки.

### Версия 1.4

* Добавен е скрипт за получаване на информация за знака в позицията на
  каретката (принос от Lukasz Golonka).
* Обновено до Unicode 13.0.

### Версия 1.3

* Отстранена е грешка с NVDA 2019.3.


### Версия 1.2

* Предоставя допълнителна информация за знаци, написани с шрифтове на
  Microsoft.


### Версия 1.1

* Обновления с цел поддръжка на по-нови версии на NVDA (съвместимост с
  Python 2 и 3)
* Изданията вече се изпълняват посредством appveyor


### Версия 1.0

* Първо издание.

[[!tag dev stable]]

[2]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[3]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon

[4]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
