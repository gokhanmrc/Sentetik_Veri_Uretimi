# Gerçekçi Sentetik Veri Üretimi 🚀

Profesyonel iş hayatımdaki raporlama ve analiz becerilerimi ETL süreçlerine adapte etmek için bir ETL pipeline kurgularken karşılaştığım en büyük engel, verilerin gizliliğiydi. Çözüm olarak; operasyonel trendleri, saatlik yoğunlukları ve rastgelelik (noise) faktörlerini içeren bu **Sentetik Veri Simülasyonu** scriptimi geliştirdim.

## 📌 Proje Hakkında
Bu script, bir operasyonel merkezin (Call Center, Service Desk vb.) iş akışını taklit ederek anlamlı ve analiz edilebilir veri setleri üretir. Üretilen veriler, veri mühendisliği süreçlerini (ETL) test etmek ve Tableau/Power BI gibi araçlarda dashboard prototipleri oluşturmak için mükemmel bir temel sağlar.

### Bu Script Ne Yapıyor?
Bu Python scripti; Excel tabanlı, gerçeği taklit eden 11 farklı departmana ait örnek veriyi girdi olarak kullanır. NumPy ve Pandas kütüphanelerinin gücünden faydalanarak, bu departmanlar için saatlik bazda iş hacmi ve kritik KPI metriklerini simüle eder. Belirlediğiniz tarih aralığı boyunca tamamen sentetik ama operasyonel gerçekliğe uygun veriler üretir. İşlem sonunda elde edilen df_final çıktısı, analiz veya ETL süreçlerine doğrudan aktarılmaya hazır, yapılandırılmış bir veri setidir.

## 🛠️ Teknik Yetkinlikler & Yaklaşım
Bu script sadece rastgele sayılar üretmez; bir operasyonun gün içindeki doğal akışını simüle eder:

* **Zaman Serisi Simülasyonu:** Günün her saati için farklı ağırlıklar (`Weights`) kullanılarak "Morning Peak" veya "Night Shift" gibi gerçekçi iş hacmi dağılımları oluşturulur.
* **KPI Modellemesi:** `AHT (Average Handling Time)`, `Productivity` ve `SLA` gibi kritik metrikler, birbirleriyle ilişkili ve hedef (`Target`) değerlerle karşılaştırılabilir şekilde üretilir.
* **Stokastik Yaklaşım:** NumPy kullanılarak verilere eklenen gürültü (noise), verinin "fazla mükemmel" görünmesini engeller ve gerçek dünya analizlerine (anomaly detection vb.) uygun hale getirir.
* **Pandas & Veri Yapılandırma:** Excel tabanlı konfigürasyon dosyalarından beslenerek, çok boyutlu DataFrame yapıları kurar.

---
> **Not:** Bu script ile üretilen verilerle oluşturduğum **End-to-End ETL & Tableau Dashboard** projem çok yakında yayında olacak!
