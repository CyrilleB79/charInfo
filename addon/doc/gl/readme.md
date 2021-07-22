# Character Information #

* Autor: Cyrille Bougot
* Compatibilidade con NVDA: da 2017.3 á 2021.1
* Descargar [versión estable][1]
* Descargar [versión de desenvolvemento][2]

Este complemento permite presentar nunha mensaxe información de carácter
como nome, número, categoría, etc. unicode.


## Ordes

* 2 do teclado numérico (todas as distribucións de teclado) ou
  NVDA+. (distribución de portátil): cando se preme catro veces, amosa
  información sobre o carácter do navegador de obxectos actuais onde estea
  situado o cursor de revisión.


## Notas

* Este complemento tamén fornece dous xestos que están sen asignar por
  defecto:

    * Un script para amosar directamente a información do carácter no cursor
      de revisión. Se te sentes incómodo co xesto de catro pulsacións, podes
      asignarlle un xesto no diálogo de xestos de entrada de NVDA (categoría
      "Revisión de texto").
    * Un script para amosar información de carácter para o carácter na
      posición do cursor (só funciona en sitios onde hai un cursor). Pódese
      atopar na categoría "Cursor do sistema" do diálogo de xestos de
      entrada de NVDA.

* A información proporcionada está en inglés xa que é parte da norma
  Unicode. Se existe unha tradución local para este complemento, a
  información tamén se proporciona xunto co inglés.
* O nome CLDR (Unicode Common Locale Data Repository) sopórtase so en NVDA
  2019.1 e superior.
* Para os caracteres escritos coas fontes propietarias de Microsoft Symbol,
  Wingding (1, 2,, 3) e Webding, proporciónase algunha información
  adicional: nome do carácter, nome da fonte e información do carácter
  unicode correspondente.


## Rexistro de trocos

### Versión 1.6

* Compatibilidade NVDA 2021.1

### Versión 1.5

* Preparar compatibilidade con NVDA 2021.1 (contribución Lukasz Golonka).
* Actualizar coas últimas modificacións na plantilla de complementos.

### Versión 1.4

* Engadido un script para obter información para o carácter na posición do
  cursor (contribución Lukasz Golonka).
* Actualización a Unicode 13.0.

### Versión 1.3

* Arranxa un erro con NVDA 2019.3.


### Versión 1.2

* Proporciona información adicional sobre os caracteres escritos con fontes
  de Microsoft.


### Versión 1.1

* Actualizacións para soportar versións máis novas do NVDA (compatible con
  Python 2 e 3)
* As liberacións realízanse agora con Appveyor


### Versión 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
