# Informação de caracter #

* Autor: Cyrille Bougot
* NVDA compatibility: 2019.3 and beyond
* Baixar [versão estável][1]
* Baixar [Versão de desenvolvimento][2]

Este extra permite apresentar, numa mensagem, informações de caracteres como
nome unicode, número, categoria, etc.


## Comandos:

* Número 2 do bloco numérico (computador de secretária) ou
  NVDA+. (computador portátil): quando pressionado 4 vezes,, mostra
  informação complementar acerca do caractere sob o cursor.


## Notas:

* Este extra tem também dois atalhos que não são atribuídos por padrão:

    * Um script para mostrar directamente a informação do caracter do cursor
      de revisão. Se se sentir desconfortável com as 4 teclas , pode
      atribuir-lhe um novo atalho no diálogo "definir comandos" no menu do
      NVDA (categoria "Revisão de texto").
    * A script to display character information for the character at the
      position of the caret (works only in places where there is a
      caret). It can be found in the "system caret" category of NVDA input
      gestures dialog.

* A informação fornecida está em inglês, uma vez que faz parte da norma
  Unicode. Se existir uma tradução local para este suplemento, a informação
  é também fornecida juntamente com a língua inglesa.
* Para os caracteres escritos com as fontes proprietárias do Microsoft
  Symbol, Wingding (1, 2,, 3) e Webding, são fornecidas algumas informações
  adicionais: nome do caractere, nome da fonte e informações do caracter
  unicode correspondente.


## Registo de Alterações

### Version 1.8

* Update to Unicode 14.0.
* Compatibility with NVDA 2022.1.
* Drops compatibility with NVDA below 2019.3.
* The release is now performed thanks to a GitHub action instead of
  appVeyor.
* Update localizations.

### Version 1.7

* Added localizations.

### Versão 1.6

* Compatibilidade com o NVDA 2021.1.

### Versão 1.5

* Preparar a compatibilidade com NVDA 2021.1 (contribuição de Lukasz
  Golonka).
* Actualização juntamente com as últimas modificações no modelo do add-on.

### Versão 1.4

* Added a script to get information for the character at the caret position
  (contribution Lukasz Golonka).
* Actualização para Unicode 13.0.

### Versão 1.3

* Corrige um erro com o NVDA 2019.3.


### Versão 1.2

* Fornece informação adicional sobre caracteres escritos com fontes
  Microsoft.


### Versão 1.1

* Actualizações para suportar as versões mais recentes do NVDA
  (Compatibilidade com Python 2 e 3)
* actualizações realizadas agora com o apveyor


### Versão 1.0

* Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
