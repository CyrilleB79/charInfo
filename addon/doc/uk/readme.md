# Character Information (Інформація про символ) #

* Автор: Cyrille Bougot
* Сумісність з NVDA: 2022.3.3 і вище
* Завантажити [стабільну версію][1]

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

Представлена інформація містить такі розділи:

* Unicode: інформація з норми Unicode, тобто назва, назва CLDR, значення,
  блок тощо.
* MS шрифт, тільки для символів, написаних власними шрифтами Microsoft
  (Symbol, Wingding 1, 2, 3 і Webding): назва та інформація про
  еквівалентний символ Unicode.
* Опис символу NVDA: інформація, що дозволяє зрозуміти, як NVDA подає опис
  символу. NVDA використовує інформацію у верхніх рядках, що містять
  доступну інформацію, для надання опису символу.
* Опис символів NVDA: інформація, що дозволяє зрозуміти, як NVDA подає опис
  символів (e.g., "альфа" для "A"). NVDA використовує інформацію у верхніх
  рядках, що містять доступну інформацію, для надання опису символу.

Інформація надається англійською мовою, так як вона є частиною норми
Unicode. Якщо для цього додатка існує локальний переклад, інформація
надається також разом з англійською мовою.

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

## Журнал змін

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

* Оновлено локалізації.

### Version 2.3

* Оновлено локалізації.

### Version 2.2

* Removed the dev channel.
* Оновлено локалізації.

### Версія 2.1

* Виправлено деякі помилки, які перешкоджали відображенню звіту з
  інформацією про символ, коли використовувалися деякі параметри.
* Оновлено локалізації.

### Версія 2.0


* Покращено інформацію про символ NVDA у звіті про символ і опис символа
  NVDA.
* Додано підтримку складних символів, наприклад, літер e.g. з діакритичними
  знаками, що складаються з двох або більше символів Unicode.
* Оновлення до Unicode 15.0
* Оновлено дані французького блоку.
* Перегляд інформації про символи заборонено на екрані блокування та
  захищених екранах.
* На екрані блокування Windows сценарій для перегляду поточного символу
  тепер може працювати в звичайному режимі (одноразове, подвійне або
  потрійне натискання).
* Сумісність з NVDA 2023.1.
* Drops compatibility with NVDA below 2022.3.3. The last version compatible
  with NVDA 2019.3 is the [1.8][3].
* Оновлення локалізації.

### Версія 1.8

* Оновлення до Unicode 14.0.
* Сумісність з NVDA 2022.1.
* Drops compatibility with NVDA below 2019.3. The last version compatible
  with NVDA 2017.3 is the [1.7][2].
* Реліз тепер виконується завдяки дії GitHub замість appVeyor.
* Оновлення локалізації.

### Версія 1.7

* Додано локалізації.

### Версія 1.6

* Сумісність з NVDA 2021.1.

### Версія 1.5

* Підготовка сумісності з NVDA 2021.1 NVDA 2021.1 (внесок Lukasz Golonka).
* Оновлення разом з останніми змінами в шаблоні додатка.

### Версія 1.4

* Додано скрипт для отримання інформації про символ в позиції каретки
  (внесок Lukasz Golonka).
* Оновлення до Unicode 13.0.

### Версія 1.3

* Виправлено помилку в NVDA 2019.3.


### Версія 1.2

* Надає додаткову інформацію про символи, написані шрифтами Microsoft.


### Версія 1.1

* Оновлення для підтримки новіших версій NVDA (сумісних з Python 2 і 3)
* Версії зараз розробляються за допомогою appveyor


### Версія 1.0

* Перша версія.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=charInfo

[2]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[3]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon

[4]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
