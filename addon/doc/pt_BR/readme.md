# Informações de Caractere (Character Information) #

* Autor: Cyrille Bougot
* NVDA compatibility: 2022.3.3 and beyond
* Baixe a [versão estável][1]

Esse complemento permite apresentar em uma mensagem várias informações sobre
um caractere.  Ele também permite personalizar as informações relatadas
sobre um caractere ao usar os comandos de navegação de caractere do cursor
de revisão ou pressionar várias vezes o comando de caractere de revisão.

### Recursos

* Exibir informações detalhadas sobre um caractere, por exemplo, nome
  Unicode, número, CLDR, nome do símbolo, etc.
* Essas informações podem ser exibidas no local do cursor de revisão ou no
  local do cursor do sistema.
* Personalize as informações relatadas ao pressionar `numpad2`.
* Use as mesmas informações personalizadas ao mover o cursor de revisão por
  caractere.

## Comandos

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
* Não atribuído: Abre as configurações do complemento Informações sobre
  caracteres.

Os comandos não atribuídos precisam primeiro ser atribuídos na caixa de
diálogo Gestos de entrada para serem usados.

## Informações detalhadas sobre um caracter

As informações apresentadas incluem as seguintes seções:

* Unicode: informações da norma Unicode, ou seja, nome, nome CLDR, valor,
  bloco, etc.
* MS font, only for characters written with proprietary Microsoft fonts
  (Symbol, Wingding 1, 2, 3 and Webding): name and information about the
  equivalent Unicode character.
* Descrição do símbolo do NVDA: informações que permitem entender como o
  NVDA relata a descrição do símbolo. o NVDA usa as informações das linhas
  superiores que contêm as informações disponíveis para fornecer a descrição
  de um símbolo.
* Descrição do caractere do NVDA: informações que permitem entender como o
  NVDA relata a descrição do caractere (por exemplo, “alfa” para “A”). O
  NVDA usa as informações das linhas superiores que contêm as informações
  disponíveis para fornecer a descrição de um caractere.

The provided information in the Unicode section is in English since it is
part of Unicode norm. If a local translation exists for this add-on, the
information is also provided alongside with English.

## Configurações

Esse complemento tem sua própria categoria na caixa de diálogo de
configurações do NVDA, onde você pode configurar as seguintes opções.

### Ação para pressionar várias vezes o comando do caractere de revisão do relatório

As três caixas de combinação desse grupo permitem personalizar o que é
relatado pelo comando reportar caractere de revisão (`numpad2`) ao usar
dois, três ou quatro toques.  Por padrão, o NVDA informa a descrição do
caractere no segundo pressionamento e seu valor numérico, decimal e
hexadecimal, no terceiro pressionamento.  Você pode alterar o que é
informado sobre o caractere na posição do cursor de revisão ao pressionar
várias vezes.  Por exemplo, você pode informar o nome CLDR em inglês no
segundo toque, o nome Unicode no terceiro toque e exibir informações
detalhadas sobre ele no quarto toque.

### Lembre-se destas ações durante a navegação do caracter

Quando você tiver relatado informações específicas com o comando reportar
caractere de revisão (`numpad2`) chamado várias vezes, talvez queira
continuar relatando as mesmas informações enquanto navega com o cursor de
revisão (`numpad1` e `numpad3`).  Ao marcar essa opção, você poderá fazer
isso, desde que navegue com o cursor de revisão por caractere logo após
pressionar várias vezes o comando `numpad2`.

## Histórico de mudanças

### Version 3.0

* Agora é possível configurar a propriedade informada para o caractere sob o
  cursor de revisão ao pressionar várias vezes o `numpad2`. Opcionalmente,
  depois de pressionar várias vezes o `numpad2`, a última propriedade
  informada também pode ser informada, desde que você navegue por caractere
  com o cursor de revisão (`numpad1` e `numpad3`).
* Prepares compatibility with NVDA 2024.1: speech on-demand support.
* Resolve possíveis problemas de segurança relacionados ao
  [GHSA-xg6w-23rw-39r8][4] ao usar o complemento com versões mais antigas do
  NVDA. No entanto, é recomendável usar o NVDA 2023.3.3 ou superior.

### Version 2.6

* Update to Unicode 15.1.
* Adiciona suporte ao Python 3.11 para preparar a compatibilidade com o NVDA
  2024.1.
* Observação: De agora em diante, as atualizações de tradução não aparecerão
  mais no registro de alterações.

### Version 2.5

* Corrigido o erro de importação com as últimas versões alfa do NVDA, ciclo
  de desenvolvimento do NVDA 2023.2 (contribuição de Noelia Ruiz Mart nez).

### Version 2.4

* Localizações atualizadas.

### Version 2.3

* Localizações atualizadas.

### Version 2.2

* Removido o canal de desenvolvimento.
* Localizações atualizadas.

### Version 2.1

* Correção de alguns erros que impediam a exibição do relatório de
  informações do caracter quando algumas opções eram usadas.
* Localizações atualizadas.

### Version 2.0


* Aprimorou o relatório de informações de caracteres com informações sobre o
  símbolo NVDA e a descrição do caractere NVDA.
* Adicionado o suporte a caracteres compostos, por exemplo, letras com
  diacríticos que consistem em dois ou mais caracteres Unicode.
* Atualiza para Unicode 15.0.
* Atualização dos dados do bloco francês.
* A visualização de informações de caracteres não é permitida na tela de
  bloqueio e nas telas seguras.
* Na tela de bloqueio do Windows, o script para revisar o caractere atual
  agora pode funcionar normalmente (pressionamento único, duplo ou triplo).
* Compatibility with NVDA 2023.1.
* Deixa de ser compatível com o NVDA abaixo de 2022.3.3. A última versão
  compatível com o NVDA 2019.3 é a [1.8][3].
* Atualizar localizações.

### Version 1.8

* Update to Unicode 14.0.
* Compatibility with NVDA 2022.1.
* Deixa de ser compatível com o NVDA abaixo de 2019.3. A última versão
  compatível com o NVDA 2017.3 é a [1.7][2].
* O lançamento agora é realizado graças a uma ação do GitHub em vez do
  appVeyor.
* Atualizar localizações.

### Version 1.7

* Adicionadas localizações.

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

* Corrigido uma falha com NVDA 2019.3.


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

[1]: https://www.nvaccess.org/addonStore/legacy?file=charInfo

[2]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[3]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon

[4]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
