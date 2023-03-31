# Información del carácter #

* Autor: Cyrille Bougot
* Compatibilidad con NVDA: de 2022.3.3 en adelante
* Descargar [versión estable][1]

Este complemento permite presentar en un mensaje diversa información sobre
un carácter.

## Información presentada

La información presentada incluye las siguientes secciones:

* Unicode: información sobre la norma Unicode como nombre, nombre CLDR,
  valor, bloque, etc.
* Fuente MS, sólo para los caracteres escritos con fuentes propietarias de
  Microsoft (símbolo, Wingding 1, 2, 3 y Webding): nombre e información
  sobre el carácter Unicode equivalente.
* Descripción de símbolo de NVDA: información que permite entender cómo
  anuncia NVDA la descripción del símbolo. NVDA utiliza la información de
  las filas superiores que contienen la información disponible para
  proporcionar la descripción de un símbolo.
* Descripción del carácter de NVDA: información que permite comprender cómo
  anuncia NVDA la descripción del carácter (por ejemplo, "alfa" para la
  "A"). NVDA usa la información de las filas superiores que contengan la
  información disponible para proporcionar la descripción de un carácter.


## Órdenes

* 2 del teclado numérico (todas las disposiciones de teclado) o
  NVDA+. (disposición portátil): si se pulsa 4 veces, muestra información
  del carácter bajo el cursor de revisión situado en el objeto actual del
  navegador de objetos.
* Sin asignar: presenta un mensaje con información detallada sobre el
  carácter situado bajo el cursor de revisión en el objeto donde está el
  navegador de objetos. Si no te sientes cómodo con el gesto de cuatro
  pulsaciones, puedes asignarle un gesto desde el diálogo Gestos de entrada
  de NVDA (categoría "Revisión de texto").
* Sin asignar: presenta un mensaje con información detallada del carácter en
  la posición del cursor (sólo funciona en lugares donde hay un cursor). Se
  puede encontrar en la categoría "Cursor del sistema" del diálogo Gestos de
  entrada de NVDA.

## Notas

* Hay dos órdenes sin asignar por defecto. Se deben asignar desde el diálogo
  Gestos de entrada para poder usarlas.
* La información proporcionada en la sección Unicode está en inglés, ya que
  forma parte de la norma Unicode. Si existe una traducción local para este
  complemento, se proporciona esa información también aparte de la inglesa.


## Registro de cambios

### Versión 2.1

* Se han corregido algunos fallos que impedían mostrar la información del
  carácter cuando se usaban ciertas opciones.
* Traducciones actualizadas.

### Versión 2.0


* Se ha mejorado la información en el anuncio de caracteres con información
  de símbolo y descripción de caracteres de NVDA.
* Se ha añadido soporte para caracteres compuestos, como letras diacríticas
  que constan de dos o más caracteres Unicode.
* Se actualiza a Unicode 15.0
* Se han actualizado los datos del bloque francés.
* No se puede visualizar información del carácter en pantallas seguras ni en
  la pantalla de bloqueo.
* En la pantalla de bloqueo de Windows, el script para revisar el carácter
  actual puede operar con normalidad (única, doble o triple pulsación).
* Compatibilidad con NVDA 2023.1.
* Se elimina la compatibilidad con versiones de NVDA inferiores a la
  2022.3.3. La última versión compatible con NVDA 2019.3 es la
  [1.8][downloadVersion1.8].
* Traducciones actualizadas.

### Versión 1.8

* Se actualiza a Unicode 14.0.
* Compatibilidad con NVDA 2022.1.
* Se elimina la compatibilidad con versiones de NVDA inferiores a la
  2019.3. La última versión compatible con NVDA 2017.3 es la
  [1.7][downloadVersion1.7].
* La liberación se hace gracias a una acción de GitHub en vez de AppVeyor.
* Traducciones actualizadas.

### Versión 1.7

* Se han añadido nuevos idiomas.

### Versión 1.6

* Compatibilidad con NVDA 2021.1.

### Versión 1.5

* Se prepara la compatibilidad con NVDA 2021.1 (contribución de Lukasz
  Golonka).
* Se incorporan las últimas modificaciones de la plantilla de complementos.

### Versión 1.4

* Añadido un script para obtener información sobre el carácter en la
  posición del cursor (contribución de Lukasz Golonka).
* Se actualiza a Unicode 13.0.

### Versión 1.3

* Corrige un fallo con NVDA 2019.3.


### Versión 1.2

* Proporciona información adicional sobre caracteres escritos con fuentes de
  Microsoft.


### Versión 1.1

* Actualizaciones para soportar versiones más nuevas de NVDA (compatible con
  Python 2 y 3)
* Las liberaciones se realizan ahora con Appveyor


### Versión 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=charInfo

[downloadVersion1.7]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[downloadVersion1.8]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon
