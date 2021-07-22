# Informações de Caractere (Character Information) #

* Autor: Cyrille Bougot
* Compatibilidade com NVDA: 2017.3 até 2021.1
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]

Este complemento possibilita apresentar numa mensagem informações do
caractere, tais como nome unicode, número, categoria etc.


## Comandos

* 2 do teclado numérico (todos os esquemas de teclado) ou NVDA+. (esquema
  para computador portátil): quando pressionado 4 vezes, exibe informações
  sobre o caractere do objeto atual de navegação onde o cursor de exploração
  está situado.


## Notas

* Este complemento também fornece dois comandos — gestos — que não são
  atribuídos por padrão:

    * Um script para exibir diretamente as informações do caractere do
      cursor de exploração. Caso você se sinta desconfortável com o comando
      de  quatro pressionamentos, pode atribuir um comando — gesto — a ele
      no diálogo Definir Comandos do NVDA (categoria "Exploração de texto").
    * Um script para exibir informações sobre o caractere na posição do
      cursor do sistema (funciona apenas em locais onde há um cursor). Ele
      pode ser encontrado na categoria "cursor do sistema" do diálogo
      definir comando do NVDA.

* A informação fornecida está em inglês, uma vez que ela é parte da norma
  Unicode. Caso exista uma tradução local para este complemento, as
  informações também são fornecidas juntamente em inglês.
* O nome CLDR (Unicode Common Locale Data Repository — Repositório de Dados
  de Localidade Comum Unicode) só é suportado em NVDA 2019.1 e superior.
* Para os caracteres escritos com fontes proprietárias da Microsoft Symbol,
  Wingding (1, 2, 3) e Webding, algumas informações adicionais são
  fornecidas: Nome do caractere, nome da fonte e informações do caractere
  unicode correspondente.


## Histórico de mudanças

### Versão 1.6

* Compatibilidade com NVDA 2021.1.

### Versão 1.5

* Prepara compatibilidade com NVDA 2021.1 (contribuição Lukasz Golonka).
* Atualização junto com as últimas modificações no modelo de complemento.

### Versão 1.4

* Adicionado um script para obter informações sobre o caractere na posição
  do cursor do sistema (contribuição Lukasz Golonka).
* Atualiza para Unicode 13.0.

### Versão 1.3

* Corrigido um bug com NVDA 2019.3.


### Versão 1.2

* Fornece informações adicionais para caracteres escritos com fontes
  Microsoft.


### Versão 1.1

* Atualizado para suportar versões mais novas do NVDA (compatíveis com
  Python 2 e 3)
* Lançamentos agora realizados com appveyor


### Versão 1.0

* Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
