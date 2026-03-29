# Bir ETL Projesinin Temeli: Gerçekçi Sentetik Veri Üretimi 🚀

Gerçek bir iş problemini (**Workforce Planning & SLA Analysis**) çözmek için bir ETL pipeline kurgularken karşılaştığım en büyük engel, verilerin gizliliğiydi. Çözüm olarak; operasyonel trendleri, saatlik yoğunlukları ve rastgelelik (noise) faktörlerini içeren bu **Sentetik Veri Simülasyonu** scriptimi geliştirdim.

## 📌 Proje Hakkında
Bu script, bir operasyonel merkezin (Call Center, Service Desk vb.) iş akışını taklit ederek anlamlı ve analiz edilebilir veri setleri üretir. Üretilen veriler, veri mühendisliği süreçlerini (ETL) test etmek ve Tableau/Power BI gibi araçlarda dashboard prototipleri oluşturmak için mükemmel bir temel sağlar.

### Bu Script Ne Yapıyor?
* **Daily Trend Simulation:** Günün her saati için farklı ağırlıklar (`Weights`) kullanarak gerçekçi çağrı/iş hacmi dağılımı yaratır.
* **Operational KPIs:** AHT (*Average Handle Time*), *Productivity* ve *SLA* gibi kritik metrikleri, önceden tanımlanmış hedefler ve mantıklı sapmalarla üretir.
* **Noise Integration:** `numpy.random` kütüphanesi ile veriye kontrollü gürültü (noise) ekleyerek, analizin daha "gerçekçi" ve "zorlayıcı" (outlier barındıran) olmasını sağlar.
* **Multi-PU (Power Unit) Support:** Farklı departmanlar, diller (TR, EN vb.) ve kategoriler bazında özelleştirilmiş veri üretimine olanak tanır.

## 🛠️ Teknik Yetenekler
Script içerisinde kullanılan temel teknolojiler:
* **Pandas:** Karmaşık veri çerçevelerinin (DataFrame) yönetimi ve zamansal iterasyonlar.
* **NumPy:** İstatistiksel dağılımlar ve matematiksel simülasyonlar.
* **Openpyxl:** Excel tabanlı girdi verilerini okuma ve işleme.

## 🚀 Kurulum ve Kullanım

1.  **Gereksinimleri Yükleyin:**
    ```bash
    pip install pandas numpy openpyxl
    ```

2.  **Veri Hazırlığı:**
    Script, girdi olarak `Sample_Data.xlsx` dosyasındaki "Queue Dashboard" sayfasını kullanır. Bu dosya; çalışan sayıları (Head Count), hedef SLA ve AHT gibi temel parametreleri içermelidir.

3.  **Çalıştırma:**
    ```bash
    python WorkBook.py
    ```
    İşlem sonunda oluşan `df_final` çıktısı, projenin ETL aşamasına geçmeye hazır halidir.

## 📊 Örnek Veri Yapısı
Scriptin ürettiği tablo şu kolonları ve benzeri verileri içerir:
* `Date_hour`: Zaman damgası
* `Hourly_Volume`: O saatteki iş yükü
* `Hourly_AHT`: Gerçekleşen ortalama işlem süresi
* `SLA`: Servis seviyesi başarısı
* `Productivity`: Verimlilik oranı

---

> **Not:** Bu verileri kullanarak oluşturduğum **End-to-End ETL & Tableau Dashboard** projemin detaylarını yakında paylaşacağım!

## 📫 İletişim
**Gökhan Meriç** - [LinkedIn Profilin](https://www.linkedin.com/in/KENDI_LINKIN)
