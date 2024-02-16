# Information caractère #

* Auteur : Cyrille Bougot
* Compatibilité NVDA : 2022.3.3 et ultérieure
* Télécharger [version stable][1]

Cette extension permet d'afficher dans un message diverses informations sur
un caractère. Elle permet également de personnaliser les informations
annoncées sur un caractère lors de l'utilisation des commandes de navigation
par caractère du curseur de revue ou d'appuis multiples sur la commande
d'annonce du caractère sous le curseur de revue.

### Fonctionnalités

* Afficher des informations détaillées sur un caractère, par ex. nom
  Unicode, numéro, CLDR, nom du symbole, etc.
* Ces informations peuvent être affichées soit à l'emplacement du curseur de
  revue, soit à l'emplacement du curseur système.
* Personnaliser les informations annoncées lorsque vous appuyez sur
  `pavnum2`.
* Utiliser les mêmes informations personnalisées lorsque vous déplacez le
  curseur de revue par caractère.

## Commandes

* PavNum2 (toutes les dispositions de clavier) ou NVDA+, (disposition
  ordinateur portable): un quadruple appui, affiche des informations sur le
  caractère de l'objet navigateur courant à la position du curseur de
  revue. Cette commande peut également être personnalisée dans les
  paramètres de l'extension.
* Non affecté: Affiche un message contenant des informations détaillées sur
  le caractère où se trouve le curseur de revue. Si vous n'êtes pas à l'aise
  avec le geste de commande à 4 appuis, vous pouvez utiliser cette commande
  à la place.
* Non affecté: Affiche un message avec des informations détaillées sur le
  caractère à la position du curseur système (ne fonctionne que dans les
  endroits où il y a un curseur).
* Non attribué : ouvre les paramètres de l'extension Informations Caractère.

Les commandes non affectées doivent d'abord être affectées dans la boîte de
dialogue Gestes de commandes pour être utilisées.

## Informations détaillées sur un caractère

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

Les informations fournies sont en anglais car elles font partie de la norme
unicode. Si une traduction locale existe pour cette extension les
informations sont également fournies parallèlement à l'anglais.

## Paramètres

Cette extension possède sa propre catégorie dans la boîte de dialogue des
paramètres de NVDA où vous pouvez configurer les options suivantes.

### Action pour les appuis multiples de la commande d'annonce du caractère sous le curseur de revue

Les trois listes déroulantes de ce groupe permettent de personnaliser ce qui
est annoncé par la commande de revue du caractère courant (`pavnum2`) lors
de deux, trois ou quatre appuis. Par défaut, NVDA annonce la description du
caractère au deuxième appui et sa valeur numérique, décimale et
hexadécimale, au troisième appui. Vous pouvez modifier ce qui est annoncé
sur le caractère à la position du curseur de revue en appuyant plusieurs
fois. Par exemple, vous pouvez signaler son nom anglais CLDR lors d'un
deuxième appui, son nom Unicode lors d'un troisième appui et afficher des
informations détaillées sur celui-ci lors d'un quatrième appui.

### Se souvenir de ces actions lors de la navigation par caractère

Lorsque vous avez annoncé des informations spécifiques avec la commande
d'annonce du caractère sous le curseur de revue (`pavnum2`) appelée
plusieurs fois, vous souhaiterez peut-être continuer à annoncer les mêmes
informations tout en naviguant avec le curseur de revue (`pavnum1` et
`pavnum3`). Vous pourrez le faire en cochant cette option, à condition de
naviguer avec le curseur de revue par caractère juste après un appui
multiple sur `pavnum2`.

## Journal des changements

### Version 3.0

* Il est désormais possible de configurer la propriété annoncée pour le
  caractère sous le curseur de revue lors de plusieurs appuis sur
  `pavnum2`. En option, après plusieurs appuis sur `numpad2`, la dernière
  propriété annoncée peut également être annoncée tant que vous naviguez par
  caractère avec le curseur de revue (`pavnum1` et `pavnum3`).
* Prépare la compatibilité avec NVDA 2024.1 : prise en charge de la parole à
  la demande.
* Résout des problèmes de sécurité potentiels liés à
  [GHSA-xg6w-23rw-39r8][4] lors de l'utilisation de l'extension avec des
  versions plus anciennes de NVDA. Cependant, il est recommandé d'utiliser
  NVDA 2023.3.3 ou supérieur.

### Version 2.6

* Mise à jour vers Unicode 15.1.
* Ajoute la prise en charge de Python 3.11 pour préparer la compatibilité
  avec NVDA 2024.1.
* Remarque : À partir de maintenant, les mises à jour de traduction
  n'apparaîtront plus dans le journal des modifications.

### Version 2.5

* Correction d'une erreur d'importation avec les dernières versions alpha de
  NVDA, cycle de développement NVDA 2023.2 (contribution Noelia Ruiz
  Martínez).

### Version 2.4

* Mise à jour des localisations.

### Version 2.3

* Mise à jour des localisations.

### Version 2.2

* Suppression du canal de développement.
* Mise à jour des localisations.

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
  version compatible avec NVDA 2019.3 est la [1.8][3].
* Mise à jour des localisations.

### Version 1.8

* Mise à jour vers Unicode 14.0.
* Compatibilité avec NVDA 2022.1.
* Abandon de la compatibilité avec NVDA en dessous de 2019.3. La dernière
  version compatible avec NVDA 2017.3 est la [1.7][2].
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

[2]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[3]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon

[4]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
