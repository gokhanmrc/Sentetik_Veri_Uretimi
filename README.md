# Gerçekçi Sentetik Veri Üretimi 🚀

Profesyonel iş hayatımdaki raporlama ve analiz becerilerimi ETL süreçlerine adapte etmek için bir ETL pipeline kurgularken karşılaştığım en büyük engel, verilerin gizliliğiydi. Çözüm olarak; operasyonel trendleri, saatlik yoğunlukları ve rastgelelik (noise) faktörlerini içeren bu **Sentetik Veri Simülasyonu** scriptimi geliştirdim.

## 📌 Proje Hakkında
Bu script, bir operasyonel merkezin (Call Center, Service Desk vb.) iş akışını taklit ederek anlamlı ve analiz edilebilir veri setleri üretir. Üretilen veriler, veri mühendisliği süreçlerini (ETL) test etmek ve Tableau/Power BI gibi araçlarda dashboard prototipleri oluşturmak için mükemmel bir temel sağlar.

### Bu Script Ne Yapıyor?
Bu Python scripti; Excel tabanlı, gerçeği taklit eden 11 farklı departmana ait örnek veriyi girdi olarak kullanır. NumPy ve Pandas kütüphanelerinin gücünden faydalanarak, bu departmanlar için saatlik bazda iş hacmi ve kritik KPI metriklerini simüle eder. Belirlediğiniz tarih aralığı boyunca tamamen sentetik ama operasyonel gerçekliğe uygun veriler üretir. İşlem sonunda elde edilen `df_final` çıktısı, analiz veya ETL süreçlerine doğrudan aktarılmaya hazır, yapılandırılmış bir veri setidir.

## 🛠️ Teknik Yetkinlikler & Yaklaşım
Bu script sadece rastgele sayılar üretmez; bir operasyonun gün içindeki doğal akışını simüle eder:

* **Zaman Serisi Simülasyonu:** Günün her saati için farklı ağırlıklar (`Weights`) kullanılarak "Morning Peak" veya "Night Shift" gibi gerçekçi iş hacmi dağılımları oluşturulur.
* **KPI Modellemesi:** `AHT (Average Handling Time)`, `Productivity` ve `SLA` gibi kritik metrikler, birbirleriyle ilişkili ve hedef (`Target`) değerlerle karşılaştırılabilir şekilde üretilir.
* **Stokastik Yaklaşım:** NumPy kullanılarak verilere eklenen gürültü (noise), verinin "fazla mükemmel" görünmesini engeller ve gerçek dünya analizlerine uygun hale getirir.
* **Pandas & Veri Yapılandırma:** Excel tabanlı konfigürasyon dosyalarından beslenerek, çok boyutlu DataFrame yapıları kurar.

## 🚀 Kullanım
1. `Sample_Data.xlsx` dosyasındaki departman hedeflerinizi ve çalışan sayılarını belirleyin.
2. `data_generator.py` içerisindeki `Date` değişkenini (Başlangıç Tarihi) ve döngü miktarını (Gün Sayısı) isteğinize göre güncelleyin.
3. Scripti çalıştırdığınızda, analizlerinizde kullanabileceğiniz `Volume_Information.csv` dosyası otomatik olarak oluşturulacaktır.

## 📊 Örnek Veri Çıktısı (Preview)
Script çalıştırıldıktan sonra aşağıdaki yapıda, analize hazır bir tablo sunar:

| Date | Pu_Id | Pu_Title | total_input | total_output | ontime_output | Hourly_AHT | AHT_Target | AHT_Ratio | Productivity | SLA |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026_03_01_00:00 | 835745 | EN_Category_A_1 | 865 | 867 | 867 | 49 | 65 | 0.75 | 73.46 | 1.00 |
| 2026-03-01 01:00 | 835745 | EN_Category_A_1 | 848 | 843 | 843 | 48 | 65 | 0.73 | 75.00 | 1.00 |
| 2026-03-01 02:00 | 835745 | EN_Category_A_1 | 790 | 792 | 792 | 62 | 65 | 0.95 | 58.06 | 1.00 |
| 2026-03-01 03:00 | 835745 | EN_Category_A_1 | 705 | 706 | 568 | 57 | 65 | 0.87 | 63.15 | 0.80 |
| 2026-03-01 04:00 | 835745 | EN_Category_A_1 | 521 | 517 | 425 | 63 | 65 | 0.96 | 57.14 | 0.82 |

---
> **Not:** Bu script ile üretilen verilerle oluşturduğum **End-to-End ETL & Tableau Dashboard** projem çok yakında yayında olacak!
