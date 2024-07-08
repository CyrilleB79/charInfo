# Karakter bilgisi #

* Yazar: Cyrille Bougot
* NVDA uyumluluğu: 2022.3.3 ve sonrası
* [Kararlı sürümü][1] indir

Bu eklenti, bir mesajda bir karakter hakkında çeşitli bilgilerin sunulmasına
olanak tanır. Ayrıca, gözden geçirme imleci karakter gezinme komutlarını
kullanırken veya karakteri gözden geçirme komutuna birden çok kez
basıldığında, bir karakter hakkında bildirilen bilgilerin özelleştirilmesine
de olanak tanır.

### Özellikler

* Bir karaktere ilişkin ayrıntılı bilgileri görüntüleyin, ör. Unicode adı,
  numarası, CLDR, sembol adı vb.
* Bu bilgi, inceleme imlecinin bulunduğu konumda veya sistem imlecinin
  bulunduğu konumda görüntülenebilir.
* 'Numpad2'ye basıldığında bildirilen bilgileri özelleştirir.
* İnceleme imlecini karakter karakter hareket ettirirken aynı özel bilgileri
  kullanır.

## Komutlar

* 'Numpad2' (tüm klavye düzenleri) veya 'NVDA+.' (dizüstü bilgisayar
  düzeni): 4 kez basıldığında, inceleme imlecinin bulunduğu geçerli gezinme
  nesnesinin karakteri hakkında bilgi görüntüler. Bu komut eklentinin
  ayarlarında da özelleştirilebilir.
* Atanmamış: İnceleme imlecinin bulunduğu karakter hakkında ayrıntılı bilgi
  içeren bir mesaj sunar. Dört basma hareketinden rahatsızlık duyuyorsanız
  bunun yerine bu komutu kullanabilirsiniz.
* Atanmamış: İmlecin konumundaki karakter hakkında detaylı bilgi içeren bir
  mesaj sunar (yalnızca imlecin olduğu yerlerde çalışır).
* Atanmamış: Karakter Bilgisi eklenti ayarlarını açar.

Atanmamış komutların kullanılabilmesi için öncelikle Girdi hareketleri
iletişim kutusunda atanması gerekir.

## Bir karakter hakkında detaylı bilgi

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

Karakter hakkında bilgi, unicode düzeninde olduğu için İngilizce
verilir. Eklenti başka bir dile çevrildiyse bilgi İngilizceyle birlikte
verilir.

## Ayarlar

Bu eklentinin NVDA'nın ayarlar iletişim kutusunda aşağıdaki seçenekleri
yapılandırabileceğiniz kendi kategorisi vardır.

### Gözden geçirme karakteri bildirimi komutuna birden çok kez basıldığında yapılacak eylem

Bu grubun üç birleşik kutusu, iki, üç veya dört basış kullanıldığında
inceleme karakteri bildirimi komutu (`numpad2`) tarafından neyin
bildirileceğini özelleştirmeye izin verir.  Varsayılan olarak, NVDA karakter
açıklamasını ikinci basışta, sayısal değerini, ondalık ve onaltılık olarak
üçüncü basışta bildirir.  Birden fazla basışta inceleme imlecinin
konumundaki karakterde bildirilenleri değiştirebilirsiniz.  Örneğin, ikinci
basışta CLDR İngilizce adını, üçüncü basışta Unicode adını bildirebilir ve
dördüncü basışta ayrıntılı bilgileri görüntüleyebilirsiniz.

### Karakter gezintisi sırasında bu eylemleri hatırla

İnceleme karakteri bildirimi komutunu ("numpad2") birden çok kez çağırarak
belirli bilgileri bildirdiğinizde, inceleme imleciyle ("numpad1" ve
"numpad3") gezinirken aynı bilgileri bildirmeye devam etmek
isteyebilirsiniz. Bu seçeneğin işaretlenmesi, 'numpad2'ye birden çok kez
basıldıktan hemen sonra inceleme imleciyle karakter karakter gezindiğiniz
sürece bunu yapmanıza olanak tanır.

## Değişiklikler

### Sürüm 3.0

* Artık 'numpad2'ye birden fazla basıldığında inceleme imlecinin altındaki
  karakter için bildirilen özelliği yapılandırmak mümkün. İsteğe bağlı
  olarak, 'numpad2'ye birden fazla bastıktan sonra, gözden geçirme imleciyle
  ('numpad1' ve 'numpad3') karaktere göre gezindiğiniz sürece son bildirilen
  özellik de bildirilebilir.
* NVDA 2024.1 ile uyumluluğu hazırlar: isteğe bağlı konuşma desteği.
* Eklentiyi NVDA'nın eski sürümleriyle kullanırken [GHSA-xg6w-23rw-39r8][4]
  ile ilgili olası güvenlik sorunlarını giderir. Ancak NVDA 2023.3.3 veya
  üzerini kullanmanız tavsiye edilir.

### Sürüm 2.6

* Unicode 15.1'e güncellendi.
* NVDA 2024.1 ile uyumluluğu hazırlamak amacıyla Python 3.11 desteği
  eklendi.
* Not: Artık çeviri güncellemeleri değişiklik günlüğünde görünmeyecek.

### Sürüm 2.5

* NVDA 2023.2 geliştirme döngüsündeki son NVDA alfa sürümleriyle ilgili içe
  aktarma hatası düzeltildi (katkı Noelia Ruiz Marténez).

### Sürüm 2.4

* Yerelleştirmeler güncellendi.

### Sürüm 2.3

* Yerelleştirmeler güncellendi.

### Sürüm 2.2

* Geliştirici kanalı kaldırıldı.
* Yerelleştirmeler güncellendi.

### Sürüm 2.1

* Bazı seçenekler kullanıldığında karakter bilgi raporunun görüntülenmesini
  engelleyen bazı hatalar düzeltildi.
* Yerelleştirmeler güncellendi.

### Sürüm 2.0


* Karakter bilgisi duyurusu, NVDA sembolü ve NVDA karakter açıklaması
  hakkında bilgilerle geliştirildi.
* Bileşik karakter desteği eklendi, örn. iki veya daha fazla Unicode
  karakterinden oluşan aksanlı harfler.
* Unicode 15.0'a güncellendi
* Fransız blok verileri güncellendi.
* Kilit ekranında ve güvenli ekranlarda karakter bilgilerinin
  görüntülenmesine izin verilmez.
* Windows kilit ekranında, mevcut karakteri gözden geçiren komut artık
  normal şekilde çalışabilir (tek, çift veya üçlü basın).
* Eklenti NVDA 2023.1 sürümüyle uyumlu hâle getirildi.
* NVDA uyumluluğu 2022.3.3'ün altına düşer. NVDA 2019.3 ile uyumlu son sürüm
  [1.8][3]'tür.
* Yerelleştirmeleri güncellendi.

### Sürüm 1.8

* Unicode 14.0'a güncellendi.
* Eklenti NVDA 2022.1 sürümüyle uyumlu hâle getirildi.
* NVDA ile uyumluluğu 2019.3'ün altına düşürür. NVDA 2017.3 ile uyumlu son
  sürüm [1.7][2]'dir.
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

[2]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.7/charInfo-1.7.nvda-addon

[3]:
https://github.com/CyrilleB79/charInfo/releases/download/V1.8/charInfo-1.8.nvda-addon

[4]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
