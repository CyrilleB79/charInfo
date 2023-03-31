# 字符信息 #

* 作者： Cyrille Bougot
* NVDA compatibility: 2022.3.3 and beyond
* 下载 [稳定版][1]

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


## 快捷键

* 数字键盘2 （所有键盘布局）或 NVDA +句号 (.) （笔记本键盘布局）：按4次时，读出浏览光标处字符的信息。
* Unassigned: Presents a message with detailed information on the character
  where the review cursor is situated. If you feel uncomfortable with the
  four press gesture, you may assign to it a gesture in NVDA's input gesture
  dialog ("Text review" category).
* Unassigned: Presents a message with detailed information on the character
  at the position of the caret (works only in places where there is a
  caret). It can be found in the "system caret" category of NVDA input
  gestures dialog.

## 注意

* Two commands are unassigned by default. They need to be assigned in the
  Input gestures dialog to be used.
* The provided information in the Unicode section is in English since it is
  part of Unicode norm. If a local translation exists for this add-on, the
  information is also provided alongside with English.


## 更新日志

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
* 更新本地化。

### 版本1.8

* 更新到 Unicode 14.0。
* 兼容 NVDA 2022.1。
* Drops compatibility with NVDA below 2019.3. The last version compatible
  with NVDA 2017.3 is the [1.7][downloadVersion1.7].
* 现在通过 GitHub 操作而不是 appVeyor 来执行发布。
* 更新本地化。

### 版本1.7

* 添加了本地化。

### 版本1.6

* 兼容 NVDA 2021.1。

### 版本1.5

* 准备与 NVDA 2021.1兼容（贡献 lukasz golonka）。
* 随插件模板的上次修改一起更新。

### 版本1.4

* 添加了一个脚本来获取系统输入焦点处的字符信息（贡献 Lukasz Golonka）。
* 更新到 Unicode 13.0。

### 版本1.3

* 修复了 NVDA 2019.3 的一个 bug。


### 版本1.2

* 提供有关使用Microsoft字体编写的字符的附加信息。


### 版本1.1

* 更新以支持更新的版本的NVDA（兼容Python 2和3）
* 现在通过appveyor进行发布


### 版本1.0

* 发布初始版本.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=charInfo

[downloadVersion1.7]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[downloadVersion1.8]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon
