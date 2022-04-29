# Zeichen-Informationen #

* Autor: Cyrille Bougot
* NVDA compatibility: 2019.3 and beyond
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

Diese Erweiterung ermöglicht es, in einer Nachricht Zeichen-Informationen
wie Unicode-Name, Nummer, Kategorie, etc. zu präsentieren.


## Befehle

* Nummernblock2 (alle Tastaturschemata) oder NVDA +. (Tastaturschema
  Laptop): Wenn diese Tastenkombination viermal gedrückt wird, werden
  Informationen zum Zeichen des aktuellen Navigatorobjekts angezeigt, in dem
  sich der NVDA-Cursor befindet.


## Anmerkungen

* Diese Erweiterung stellt zwei Tastenkombinationen bereit, die
  standardmäßig nicht zugewiesen sind:

    * Diese Erweiterung bietet einen Befehl, um zusätzliche Informationen
      über das Zeichen am NVDA-Cursor ansagen zu lassen. Falls das 4malige
      Drücken der Tastenkombination unkomfortabel ist, können Sie im Dialog
      Tastenbefehle in der Kategorie Text betrachten eine andere
      Tastenkombination zuweisen.
    * Dieser Befehl, der zusätzliche Informationen für das Zeichen an der
      Schreibmarke anzeigt, funktioniert auch nur in Eingabefeldern, wo es
      eine Schreibmarke gibt. Dieser kann im Dialog Tastenbefehle in der
      Kategorie Systemcursor geändert werden.

* Die bereitgestellten Informationen sind auf Englisch, da sie Teil der
  Unicode-Norm sind. Wenn für diese Erweiterung eine lokale Übersetzung
  vorliegt, wird diese sowie das englische original ausgegeben.
* Für Zeichen, die mittels Microsofts proprietären Symbol-Schriftarten
  (Wingding (1, 2, 3) und Webding, geschrieben wurden, werden zusätzliche
  Informationen wie Name des Zeichens, Name der Schriftart sowie
  Informationen zum zugehörigen Unicode-Zeichen zur Verfügung gestellt.


## Änderungsprotokoll

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

* Kompatibilität NVDA 2021.1.

### Version 1.5

* Kompatibilität mit NVDA 2021.1 vorbereitet (Beitrag Lukasz Golonka).
* Aktualisierungen der Erweiterungsvorlage übernommen.

### Version 1.4

* Es wurde ein Skript hinzugefügt, um zusätzliche Informationen für das
  Zeichen an der Schreibmarke  zu erhalten (Beitrag Lukasz Golonka).
* Update auf Unicode 13.0.

### Version 1.3

* Behebt einen Fehler mit NVDA 2019.3.


### Version 1.2

* Diese Erweiterung stellt zusätzliche Informationen zur Verfügung, die mit
  Microsoft-Schriften geschrieben wurden.


### Version 1.1

* Updates zur Unterstützung neuerer Versionen von NVDA (kompatibel mit
  Python 2 und 3)
* Releases werden jetzt mit Appveyor durchgeführt


### Version 1.0

* Erste Veröffentlichung.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
