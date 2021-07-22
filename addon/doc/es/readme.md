# Información del carácter #

* Autor: Cyrille Bougot
* Compatibilidad con NVDA: de 2017.3 a 2021.1
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]

Este complemento permite presentar en un mensaje información del carácter
como su nombre Unicode, número, categoría, etc.


## Órdenes

* 2 del teclado numérico (todas las disposiciones de teclado) o
  NVDA+. (disposición portátil): si se pulsa 4 veces, muestra información
  del carácter bajo el cursor de revisión situado en el objeto actual del
  navegador de objetos.


## Notas

* Este complemento también proporciona dos gestos que vienen sin asignar por
  defecto:

    * Un script para mostrar directamente información del carácter bajo el
      cursor de revisión. Si no te sientes cómodo con el gesto de cuatro
      pulsaciones, puedes asignarle un gesto desde el diálogo Gestos de
      entrada de NVDA (categoría "Revisión de texto").
    * Un script para mostrar la información del carácter en la posición del
      cursor (sólo funciona en lugares donde hay un cursor). Se puede
      encontrar en la categoría "Cursor del sistema" del diálogo Gestos de
      entrada de NVDA.

* La información proporcionada está en inglés, ya que forma parte de la
  norma Unicode. Si existiera una traducción local de este complemento, la
  información continuaría proporcionándose en inglés.
* El nombre CLDR (Unicode Common Locale Data Repository) sólo se soporta en
  NVDA 2019.1 y versiones posteriores.
* Para los caracteres escritos con el símbolo de fuentes propietarias de
  Microsoft, Wingding (1, 2, 3) y Webding, se proporciona alguna información
  adicional: nombre del carácter, nombre de la fuente e información del
  carácter Unicode correspondiente.


## Registro de cambios

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

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
