# Information caractère #

* Auteur : Cyrille Bougot
* Compatibilité NVDA : 2022.3.3 et ultérieure
* Télécharger [version stable][1]

Cette extension permet d'afficher dans un message des informations sur un
caractère.

## Informations affichées

Les informations affichées comprennent les sections suivantes :

* Unicode : informations issues de la norme Unicode, c'est-à-dire nom, nom
  CLDR, valeur, bloc, etc.
* Police MS, uniquement pour les caractères écrits avec des polices
  propriétaires Microsoft (Symbol, Wingding 1, 2, 3 et Webding) : nom et
  informations sur le caractère Unicode équivalent.
* Description de symbole NVDA : informations permettant de comprendre
  comment NVDA annonce la description d'un symbole. NVDA utilise les
  informations des premières lignes contenant les informations disponibles
  pour fournir la description d'un symbole.
* Description de caractère NVDA : information permettant de comprendre
  comment NVDA annonce la description d'un caractère (par exemple "alpha"
  pour "A"). NVDA utilise les informations des premières lignes contenant
  les informations disponibles pour fournir la description d'un caractère.


## Commandes

* PavNum2 (toutes les dispositions de clavier) ou NVDA+, (disposition
  ordinateur portable): un quadruple appui, affiche des informations sur le
  caractère de l'objet navigateur courant à la position du curseur de revue.
* Non assigné: Affiche un message contenant des informations détaillées sur
  le caractère où se trouve le curseur de revue. Si vous n'êtes pas à l'aise
  avec le geste de commande à 4 appuis, vous pouvez lui assigner un geste de
  commande dans la boîte de dialogue de geste de commande de NVDA (catégorie
  "Revue de texte").
* Non assigné: Affiche un message avec des informations détaillées sur le
  caractère à la position du curseur (ne fonctionne que dans les endroits où
  il y a un curseur). Il se trouve dans la catégorie "Curseur système" de la
  boîte de dialogue des gestes de commande NVDA.

## Notes

* Deux commandes sont non affectées par défaut. elles doivent être affectées
  dans la boîte de dialogue Gestes de commande pour être utilisés.
* Les informations fournies sont en anglais car elles font partie de la
  norme unicode. Si une traduction locale existe pour cette extension les
  informations sont également fournies parallèlement à l'anglais.


## Journal des changements

### Version 2.1

* Correction de bugs empêchant l'affichage du message d'informations
  caractère lorsque certaines options étaient utilisées.
* Mise à jour des localisations.

### Version 2.0

* Amélioration de l'affichage d'informations caractères avec des
  informations sur le symbole NVDA et la description de caractère NVDA.
* Ajout de la prise en charge des caractères composés, par ex. lettres avec
  diacritique composées de deux caractères Unicode ou plus.
* Mise à jour vers Unicode 15.0.
* Données des blocs en français mises à jour.
* L'affichage d'informations caractère n'est pas autorisé sur l'écran de
  verrouillage et les écrans sécurisés.
* Sur l'écran de verrouillage de Windows, le script permettant la revue du
  caractère courant peut désormais fonctionner normalement (simple, double
  ou triple appui).
* Compatibilité avec NVDA 2023.1.
* Abandon de la compatibilité avec NVDA en dessous de 2022.3.3. La dernière
  version compatible avec NVDA 2019.3 est la [1.8][downloadVersion1.8].
* Mise à jour des localisations.

### Version 1.8

* Mise à jour vers Unicode 14.0.
* Compatibilité avec NVDA 2022.1.
* Abandon de la compatibilité avec NVDA en dessous de 2019.3. La dernière
  version compatible avec NVDA 2017.3 est la [1.7][downloadVersion1.7].
* La publication est maintenant effectuée grâce à une action GitHub plutôt
  qu'avec appVeyor.
* Mise à jour des localisations.

### Version 1.7

* Ajout des Localisations.

### Version 1.6

* Compatibilité NVDA 2021.1.

### Version 1.5

* Prépare la compatibilité avec NVDA 2021.1 (contribution Łukasz Golonka).
* Mise à jour avec les dernières modifications faites sur le modèle
  d'extension.

### Version 1.4

* Ajout d'un script pour obtenir des informations sur le caractère à la
  position du curseur système (contribution Łukasz Golonka).
* Mise à jour vers Unicode 13.0.

### Version 1.3

* Corrige un bug avec NVDA 2019.3.


### Version 1.2

* Fournit des informations supplémentaires sur les caractères écrits avec
  les polices Microsoft.


### Version 1.1

* Mise à jour pour supporter les nouvelles versions de NVDA (compatible
  Python 2 et 3)
* Publication maintenant effectuée avec Appveyor


### Version 1.0

* Version initiale.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=charInfo

[downloadVersion1.7]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[downloadVersion1.8]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon
