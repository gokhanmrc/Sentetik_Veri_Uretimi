# Bir ETL Projesinin Temeli: Gerçekçi Sentetik Veri Üretimi 🚀

Gerçek bir iş problemini (**Workforce Planning & SLA Analysis**) çözmek için bir ETL pipeline kurgularken karşılaştığım en büyük engel, verilerin gizliliğiydi. Çözüm olarak; operasyonel trendleri, saatlik yoğunlukları ve rastgelelik (noise) faktörlerini içeren bu **Sentetik Veri Simülasyonu** scriptimi geliştirdim.

## 📌 Proje Hakkında
Bu script, bir operasyonel merkezin (Call Center, Service Desk vb.) iş akışını taklit ederek anlamlı ve analiz edilebilir veri setleri üretir. Üretilen veriler, veri mühendisliği süreçlerini (ETL) test etmek ve Tableau/Power BI gibi araçlarda dashboard prototipleri oluşturmak için mükemmel bir temel sağlar.

### Bu Script Ne Yapıyor?
Bu Python scripti; Excel tabanlı, gerçeği taklit eden 11 farklı departmana ait örnek veriyi girdi olarak kullanır. NumPy ve Pandas kütüphanelerinin gücünden faydalanarak, bu departmanlar için saatlik bazda iş hacmi ve kritik KPI metriklerini simüle eder. Belirlediğiniz tarih aralığı boyunca tamamen sentetik ama operasyonel gerçekliğe uygun veriler üretir. İşlem sonunda elde edilen df_final çıktısı, analiz veya ETL süreçlerine doğrudan aktarılmaya hazır, yapılandırılmış bir veri setidir.

## 🛠️ Teknik Yetenekler
Script içerisinde kullanılan temel teknolojiler:
* **Pandas:** Karmaşık veri çerçevelerinin (DataFrame) yönetimi ve zamansal iterasyonlar.
* **NumPy:** İstatistiksel dağılımlar ve matematiksel simülasyonlar.

> **Not:** Bu verileri kullanarak oluşturduğum **End-to-End ETL & Tableau Dashboard** projemin detaylarını yakında paylaşacağım!

## 📫 İletişim
**Gökhan Meriç** - [LinkedIn Profilin](https://www.linkedin.com/in/KENDI_LINKIN)
