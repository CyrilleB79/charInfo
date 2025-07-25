# Información del carácter #

* Autor: Cyrille Bougot
* Compatibilidad con NVDA: de 2022.3.3 en adelante

Este complemento permite presentar en un mensaje información diversa sobre
un carácter. También permite personalizar la información anunciada de un
carácter al usar las órdenes de navegación del cursor de revisión o pulsar
varias veces la orden de revisar carácter.

### Características

* Mostrar información detallada de un carácter, como su nombre Unicode,
  número, CLDR, nombre de símbolo, etc.
* Esta información se puede mostrar en la posición del cursor de revisión, o
  bien en la posición del cursor del sistema.
* Personalizar la información anunciada al pulsar `2 del teclado numérico`.
* Usar la misma información personalizada al mover el cursor de revisión por
  caracteres.

## Órdenes

* `2 del teclado numérico` (todas las disposiciones de teclado) o `NVDA+.`
  (disposición portátil): si se pulsa 4 veces, muestra información del
  carácter bajo el cursor de revisión situado en el objeto actual del
  navegador de objetos. Se puede personalizar también esta orden desde las
  opciones del complemento.
* Sin asignar: presenta un mensaje con información detallada sobre el
  carácter situado bajo el cursor de revisión en el objeto donde está el
  navegador de objetos. Si no te sientes cómodo con el gesto de cuatro
  pulsaciones, puedes usar este en su lugar.
* Sin asignar: presenta un mensaje con información detallada del carácter en
  la posición del cursor (sólo funciona en lugares donde hay un cursor).
* Sin asignar: abre las opciones del complemento Información del carácter.

Se deben asignar las órdenes sin asignar primero desde el diálogo Gestos de
entrada para poder usarlas.

## Información detallada de un carácter

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

La información proporcionada en la sección Unicode está en inglés, ya que
forma parte de la norma Unicode. Si existe una traducción local para este
complemento, se proporciona esa información también aparte de la inglesa.

En cuanto a la sección de descripción de símbolos de NVDA: este complemento
todavía no soporta diccionarios de símbolos personalizados (introducidos en
NVDA 2024.4). Ya aparecen en la lista "Opciones usadas para procesar el
símbolo", pero no en la propia tabla.

## Opciones

Este complemento dispone de su propia categoría en el diálogo de opciones de
NVDA, donde se pueden configurar las siguientes opciones.

### Acción para varias pulsaciones de la orden de anunciar el carácter revisado

Los tres cuadros combinados de este grupo permiten personalizar lo que
anuncia la orden de anunciar el carácter en revisión (`2 del teclado
numérico`) al pulsarla dos, tres o cuatro veces. Por defecto, NVDA anuncia
la descripción del carácter en la segunda pulsación, y su valor numérico,
decimal y hexadecimal en la tercera. Puedes cambiar qué se anuncia del
carácter en la posición del cursor de revisión ante varias pulsaciones. Por
ejemplo, puedes anunciar su nombre CLDR en inglés en la segunda pulsación,
su nombre Unicode en la tercera y mostrar información detallada sobre él en
la cuarta.

### Recordar esta acción durante la navegación por caracteres

Cuando has anunciado información concreta con la orden de anunciar el
carácter en revisión (`2 del teclado numérico`) pulsada varias veces, puedes
querer que se siga anunciando la misma información mientras navegas con el
cursor de revisión (`1 del teclado numérico` y `3 del teclado
numérico`). Marcando esta opción podrás hacerlo, siempre que navegues con el
cursor de revisión por caracteres después de pulsar varias veces el `2 del
teclado numérico`.

## Registro de cambios

### Versión 3.5

* Implementación parcial del soporte para diccionarios personalizados
  (introducidos en NVDA 2024.4).
* Se corrige el soporte para Unicode 16.0: se actualizan los nombres de
  bloque en inglés y francés.
* Compatibilidad con NVDA 2025.1.

### Versión 3.4

* Se corrige un problema que impedía que NVDA ejecutase scripts seguros en
  la pantalla de bloqueo.

### Versión 3.3

* Se actualiza a Unicode 16.0.

### Versión 3.2

* Corrección: los caracteres para los que se ha cambiado sólo el nivel de
  puntuación ya no impiden que se muestre la información a indicar.

### Versión 3.1

* Se corrige un error cuando no había ningún valor que indicar para un
  carácter.
* Compatibilidad con NVDA 2024.1.

### Versión 3.0

* Ahora es posible configurar la propiedad anunciada para el carácter bajo
  el cursor de revisión tras varias pulsaciones del `2 del teclado
  numérico`. Opcionalmente, tras haber pulsado varias veces el `2 del
  teclado numérico`, se puede repetir la última propiedad anunciada según se
  navega por caracteres con el cursor de revisión (`1 del teclado numérico`
  y `3 del teclado numérico`).
* Prepara la compatibilidad con NVDA 2024.1: soporte para el modo de voz a
  petición.
* Soluciona posibles problemas de seguridad relacionados con
  [GHSA-xg6w-23rw-39r8][4] al usar el complemento con versiones antiguas de
  NVDA. Sin embargo, se recomienda usar NVDA 2023.3.3 o posterior.

### Versión 2.6

* Se actualiza a Unicode 15.1.
* Se añade soporte para Python 3.11 para preparar la compatibilidad con NVDA
  2024.1.
* Nota: a partir de ahora, ya no aparecerán en el registro de cambios las
  actualizaciones de traducciones.

### Versión 2.5

* Corregido error de importación en las últimas versiones alfa de NVDA,
  ciclo de desarrollo de NVDA 2023.2 (colaboración de Noelia Ruiz Martínez).

### Versión 2.4

* Traducciones actualizadas.

### Versión 2.3

* Traducciones actualizadas.

### Versión 2.2

* Se elimina el canal dev.
* Traducciones actualizadas.

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
  2022.3.3. La última versión compatible con NVDA 2019.3 es la [1.8][3].
* Traducciones actualizadas.

### Versión 1.8

* Se actualiza a Unicode 14.0.
* Compatibilidad con NVDA 2022.1.
* Se elimina la compatibilidad con versiones de NVDA inferiores a la
  2019.3. La última versión compatible con NVDA 2017.3 es la [1.7][2].
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

[2]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[3]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon

[4]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
