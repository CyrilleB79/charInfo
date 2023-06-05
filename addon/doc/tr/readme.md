# Karakter bilgisi #

* Yazar: Cyrille Bougot
* NVDA uyumluluğu: 2022.3.3 ve sonrası
* [Kararlı sürümü][1] indir

Bu eklenti, bir mesajda bir karakter hakkında çeşitli bilgiler sunmaya izin
verir.

## Sunulan bilgiler

Sunulan bilgiler aşağıdaki bölümleri içerir:

* Unicode: Unicode normundan gelen bilgiler, yani ad, CLDR adı, değer, blok
  vb.
* MS yazı tipi, yalnızca tescilli Microsoft yazı tipleriyle yazılmış
  karakterler için (Symbol, Wingding 1, 2, 3 ve Webding): eşdeğer Unicode
  karakteri hakkında ad ve bilgi.
* NVDA sembol bilgisi: NVDA'nın sembol bilgisini nasıl raporladığını
  anlamayı sağlayan bilgiler. NVDA, bir sembolün bilgisini sağlamak için
  mevcut bilgileri içeren en üst satırlardaki bilgileri kullanır.
* NVDA karakter Bilgisi: NVDA'nın karakter bilgisini nasıl rapor ettiğini
  anlamaya olanak sağlayan bilgiler (örn. "A" için "adana"). NVDA, bir
  karakterin tanımını sağlamak için mevcut bilgileri içeren en üstteki
  satırlardaki bilgileri kullanır.


## Komutlar

* Numaratör2 (tüm klavye düzenleri) veya NVDA+. (dizüstü düzeni): 4 kez
  basıldığında, inceleme imlecinin bulunduğu konumdaki nesne sunucusu
  karakteri hakkında bilgi gösterir.
* Atanmamış: İnceleme imlecinin bulunduğu karakter hakkında ayrıntılı
  bilgiler içeren bir mesaj sunar. Dörtlü basma hareketinden rahatsızsanız,
  NVDA'nın girdi hareketi iletişim kutusunda ("Metin incelemesi" kategorisi)
  buna bir hareket atayabilirsiniz.
* Atanmamış: İmlecin bulunduğu konumdaki karakter hakkında ayrıntılı
  bilgiler içeren bir mesaj sunar (yalnızca bir imlecin olduğu yerlerde
  çalışır). NVDA girdi hareketleri iletişim kutusunun "sistem düzenleme
  imleci" kategorisinde bulunabilir.

## Notlar

* İki komut varsayılan olarak atanmamıştır. Kullanılabilmeleri için Girdi
  hareketleri iletişim kutusunda atanmaları gerekir.
* Karakter hakkında bilgi, unicode düzeninde olduğu için İngilizce
  verilir. Eklenti başka bir dile çevrildiyse bilgi İngilizceyle birlikte
  verilir.


## Değişiklikler

### Sürüm 2.1

* Bazı seçenekler kullanıldığında karakter bilgi raporunun görüntülenmesini
  engelleyen bazı hatalar düzeltildi.
* Yerelleştirmeler güncellendi.

### Sürüm 2.0

* Karakter bilgisi duyurusu, NVDA sembolü ve NVDA karakter açıklaması
  hakkında bilgilerle geliştirildi.
* Bileşik karakter desteği eklendi, örn. iki veya daha fazla Unicode
  karakterinden oluşan aksanlı harfler.
* Unicode 15.0'a güncellendi.
* Fransız blok verileri güncellendi.
* Kilit ekranında ve güvenli ekranlarda karakter bilgilerinin
  görüntülenmesine izin verilmez.
* Windows kilit ekranında, mevcut karakteri gözden geçiren komut artık
  normal şekilde çalışabilir (tek, çift veya üçlü basın).
* Eklenti NVDA 2023.1 sürümüyle uyumlu hâle getirildi.
* NVDA ile uyumluluğu 2022.3.3'ün altına düşürür. NVDA 2019.3 ile uyumlu son
  sürüm [1.8][indirSürüm 1.8]'dir.
* Yerelleştirmeleri güncellendi.

### Sürüm 1.8

* Unicode 14.0'a güncellendi.
* Eklenti NVDA 2022.1 sürümüyle uyumlu hâle getirildi.
* NVDA ile uyumluluğu 2019.3'ün altına düşürür. NVDA 2017.3 ile uyumlu son
  sürüm [1.7][indirSürüm 1.7]'dir.
* Sürüm artık appVeyor yerine bir GitHub eylemi sayesinde
  gerçekleştiriliyor.
* Yerelleştirmeleri güncellendi.

### Sürüm 1.7

* Yerelleştirmeler eklendi.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=charInfo

[indirSürüm 1.7]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[indirSürüm 1.8]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon
