# Gerçekçi Sentetik Veri Üretimi 🚀

Gerçek bir iş problemini (**Workforce Planning & SLA Analysis**) çözmek için bir ETL pipeline kurgularken karşılaştığım en büyük engel, verilerin gizliliğiydi. Çözüm olarak; operasyonel trendleri, saatlik yoğunlukları ve rastgelelik (noise) faktörlerini içeren bu **Sentetik Veri Simülasyonu** scriptimi geliştirdim.

## 📌 Proje Hakkında
Bu script, bir operasyonel merkezin (Call Center, Service Desk vb.) iş akışını taklit ederek anlamlı ve analiz edilebilir veri setleri üretir. Üretilen veriler, veri mühendisliği süreçlerini (ETL) test etmek ve Tableau/Power BI gibi araçlarda dashboard prototipleri oluşturmak için mükemmel bir temel sağlar.

### Bu Script Ne Yapıyor?
Bu Python scripti; Excel tabanlı, gerçeği taklit eden 11 farklı departmana ait örnek veriyi girdi olarak kullanır. NumPy ve Pandas kütüphanelerinin gücünden faydalanarak, bu departmanlar için saatlik bazda iş hacmi ve kritik KPI metriklerini simüle eder. Belirlediğiniz tarih aralığı boyunca tamamen sentetik ama operasyonel gerçekliğe uygun veriler üretir. İşlem sonunda elde edilen df_final çıktısı, analiz veya ETL süreçlerine doğrudan aktarılmaya hazır, yapılandırılmış bir veri setidir.

## Proje içeriği

| Modül | İşlev | Temel Analitik Odaklar | Teknik Yetkinlikler |
| :--- | :--- | :--- | :--- |
| **[Modül 01](./Modul_01_Mobile_Gaming)** | **Mobile Gaming** | **DAU, Whale Analysis, Monetization, Loyalty** | `CTE`, `Date Trunc`, `Filtering` |
| **[Modül 02](./Modul_02_Banking_Fintech)** | **Fintech & Banking** | **Fraud Detection, Risk Profiling, Limit Utilization** | `Subqueries`, `Logical CASE` |
| **[Modül 03](./Modul_03_Supply_Chain)** | **E-Commerce & Supply Chain** | **SLA (Kargo Süresi) Analizi, Inventory Mgmt, Churn** | `Complex Joins`, `Date Diff` |
| **[Modül 04](./Modul_04_HR_Analytics)** | **HR & Workforce** | **Turnover Rate, Salary Equity, Hierarchy Analysis** | `Window Functions`, `Self-Join` |
| **[Modül 05](./Modul_05_Healthcare)** | **Healthcare** | **KVKK Masking, No-Show Rate, Capacity Planning** | `String Manipulation`, `Regex` |
| **[Modül 06](./Modul_06_E-Commerce_&_CRM)** | **E-Commerce Essentials** | **Sales Performance, Customer Segmentation (RFM)** | `Aggregate Functions`, `Group By` |

> **Not:** Bu verileri kullanarak oluşturduğum **End-to-End ETL & Tableau Dashboard** projemin detaylarını yakında paylaşacağım!

