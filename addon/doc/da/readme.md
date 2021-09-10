# Character Information (tilføjelse ikke oversat) #

* Forfatter: Cyrille Bougot
* NVDA -kompatibilitet: 2017.3 til 2021.1
* Download [stabil version][1]
* Download [udviklingsversion][2]

Denne tilføjelse giver mulighed for at vise information om et bestemt tegn
som unicode navn, nummer, kategori osv i en dialog.


## Kommandoer

* Numpad2 (alle tastaturlayouts) eller NVDA+. (laptop-layout): Ved at udføre
  denne kommando fire gange vil der vises information om det aktuelle tegn
  der befinder sig under læsemarkøren.


## Bemærkninger

* Denne tilføjelse har også to kommandoer, der som standard ikke er tildelt:

    * Denne tilføjelse indeholder et script, der viser informationer om det
      aktuelle tegn under læsemarkøren. Hvis du ikke er i stand til at
      udføre kommandoen fire gange hurtigt, eller blot ønsker at ændre
      kommandoen, så kan du tildele en anden kommando til scriptet under
      kategorien "Tekstlæsning" i NVDA's dialog "Håndter kommandoer"
    * Et script til visning af tegninformation for tegnet ved systemmarkøren
      (fungerer kun på steder, hvor der er en markør). Dette kan findes i
      kategorien "systemmarkør" i dialogboksen "Håndter kommandoer" i
      NVDA-menuen>Opsætning.

* Den angivne information er på engelsk, da den er en del af
  Unicode-norm. Hvis der findes en lokal oversættelse til denne tilføjelse,
  findes oplysningerne også sammen med informationerne på engelsk.
* CLDR (Unicode Common Locale Data Repository) understøttes kun med NVDA
  2019.1 og derover.
* For de tegn, der er skrevet med Microsoft-proprietære skrifttyper Symbol,
  Wingding (1, 2 ,, 3) og Webding, angives yderligere oplysninger: Tegnets
  navn, skrifttype og information om det tilsvarende unicode-tegn.


## Ændringshistorik

### Version 1.6

* Kompatibilitet: NVDA 2021.1.

### Version 1.5

* Forberedt kompatibilitet med NVDA 2021.1 (bidrag Lukasz Golonka).
* Opdateret sammen med de sidste ændringer af tilføjelsesskabelonen.

### Version 1.4

* Tilføjet et script, der kan angive oplysninger om tegnet ved markørens
  position(bidrag Lukasz Golonka).
* Opdateret til Unicode 13.0.

### Version 1.3

* Retter en fejl med NVDA 2019.3.


### Version 1.2

* Angiver yderligere oplysninger om tegn, der er skrevet med
  Microsoft-skrifttyper.


### Version 1.1

* Opdateringer til understøttelse af nyere versioner af NVDA (kompatibel med
  Python 2 og 3)
* Udgivelser udføres nu med appveyor


### Version 1.0

* Første udgivelse.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
