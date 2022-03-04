# Karakter bilgisi #

* Yazar: Cyrille Bougot
* NVDA uyumluluğu: 2017.3-2021.1
* [Kararlı sürümü][1] indir
* [geliştirici sürümünü][2] indir

Bu eklenti, NVDA'nın bir karakterin unikod adı, sayısı, kategorisi gibi
bilgileri mesaj şeklinde sunmasını sağlar.


## Komutlar

* Numaratör2 (tüm klavye düzenleri) veya NVDA+. (dizüstü düzeni): 4 kez
  basıldığında, inceleme imlecinin bulunduğu konumdaki nesne sunucusu
  karakteri hakkında bilgi gösterir.


## Notlar

* Bu eklenti ayrıca varsayılan olarak kısayolu atanmamış olan 2 işlev sunar:

    * İnceleme imlecinin üzerinde bulunduğu karakter hakkında bilgi
      görüntülemek için bir script. 4 kez basma kısayolundan memnun
      değilseniz farklı bir kısayol atayabilirsiniz. Atamayı girdi
      hareketleri iletişim kutusunun metin incelemesi kategorisinden
      yapabilirsiniz.
    * Düzenleme imlecinin üzerinde bulunduğu karakter hakkında bilgi
      göstermek için bir script (düzenleme imleci olan yerlerde
      çalışır). NVDA girdi hareketleri iletişim kutusunun "sistem düzenleme
      imleci" kategorisinde bulabilirsiniz.

* Karakter hakkında bilgi, unicode düzeninde olduğu için İngilizce
  verilir. Eklenti başka bir dile çevrildiyse bilgi İngilizceyle birlikte
  verilir.
* Karakterin CLDR (Unicode Common Locale Data Repository) adı NVDA 2019.1 ve
  üzeri sürümlerde gösterilebilmektedir.
* Microsoft proprietary yazı tipi sembolüyle yazılan karakterler için,
  Wingding (1, 2,, 3) ve Webding, bazı ek bilgiler sunulur:


## Değişiklikler

### Sürüm 1.6

* Eklenti NVDA 2021.1 sürümüyle uyumlu hâle getirildi.

### Sürüm 1.5

* NVDA 2021.1 sürümüyle uyumluluk hazırlıkları yapıldı (katkıda bulunan
  Lukasz Golonka).
* Eklenti taslağına son değişiklikler dahil edildi.

### Sürüm 1.4

* Düzenleme imlecinin bulunduğu konumdaki karakter hakkında bilgi edinmek
  için bir script eklendi (katkıda bulunan Lukasz Golonka).
* Unicode 13.0'a güncellendi.

### Sürüm 1.3

* NVDA 2019.3 sürümünde karşılaşılan bir hata düzeltildi.


### Sürüm 1.2

* Eklenti Microsoft yazı tipleriyle yazılan karakterler hakkında ek bilgi
  veriyor.


### Sürüm 1.1

* Eklenti NVDA'nın yeni sürümlerini desteklemek için güncellendi (Python 2
  ve 3 ile uyumlu)
* Eklenti appveyor ile yayınlanıyor


### Sürüm 1.0

* İlk sürüm.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=chari

[2]: https://addons.nvda-project.org/files/get.php?file=chari-dev
