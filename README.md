# Unity Kanser Hücresi Sınıflandırma Projesi

Bu proje, kanser hücrelerini iyi huylu veya kötü huylu olarak sınıflandırmak için Unity'yi Python ile eğitilmiş bir modelle entegre eder. Sınıflandırma, verileri işleyen ve sonucu Unity'ye döndüren bir Flask sunucusu aracılığıyla yapılır.

## Proje Açıklaması
Bu proje, kanser hücrelerinin görselleştirildiği Unity tabanlı bir uygulamayı içermektedir. Bu hücrelerin üzerine tıklandığında veriler, hücreleri iyi huylu veya kötü huylu olarak sınıflandırmak için eğitilmiş bir makine öğrenimi modelini barındıran bir Flask sunucusuna gönderilir.
![image](https://github.com/Osman911P/Ag-Programlama/assets/120224636/47404ef3-b198-41ba-a4e6-821d8914fa11)

## Özellikler
- *Etkileşimli Kanser Hücreleri:* Unity'de tıklanabilir kanser hücresi varlıkları.
- *Flask Sunucu Entegrasyonu:* Unity'den Flask sunucusuna işlenmek üzere veri gönderir.
- *Makine Öğrenimi Modeli:* Kanser hücrelerini sınıflandırmak için eğitimli bir Python modeli kullanır.
- *Gerçek Zamanlı Geri Bildirim:* Unity'de sınıflandırma sonucunu (iyi huylu/kötü huylu) görüntüler.

## Kullanım
- **Flask sunucusunu çalıştırın: flaskserver.py dosyasındaki kodu bir python ortamında açın.
- **Unity Editor'de Unity projesini açın ve Play moduna girin.
- **Flask sunucusuna veri göndermek için kanser hücresi varlıklarına tıklayın.
- **Flask sunucusu verileri işler ve daha sonra Unity'de görüntülenecek olan sınıflandırma sonucunu döndürür.


### Ön Koşullar
- Unity 2020.3 veya üstü
- Python 3.8 veya üstü
- Flask 2.0 veya üstü
