# 🚀 Synthetic Workforce & Operations Data Generator

## 📌 Proje Vizyonu: Veri Gizliliği Engelini Aşmak
Veri analitiği ve ETL süreçlerinde en büyük zorluk, gerçek dünya verilerine (PII/KVKK) erişim kısıtlamasıdır. Bu proje; operasyonel trendleri, saatlik yoğunluk dalgalanmalarını ve gerçekçi gürültü (noise) faktörlerini taklit ederek, **gizlilik ihlali yapmadan** yüksek kaliteli veri setleri üretmek amacıyla geliştirilmiştir.

Özellikle Call Center, Service Desk ve Paylaşımlı Hizmet Merkezleri (SSC) için KPI dashboard prototipleri oluşturmak ve veri mühendisliği pipeline'larını test etmek için tasarlanmıştır.

## 🛠️ Teknik Yetkinlikler & Yaklaşım
Bu script sadece rastgele sayılar üretmez; bir operasyonun gün içindeki doğal akışını simüle eder:

* **Zaman Serisi Simülasyonu:** Günün her saati için farklı ağırlıklar (`Weights`) kullanılarak "Morning Peak" veya "Night Shift" gibi gerçekçi iş hacmi dağılımları oluşturulur.
* **KPI Modellemesi:** `AHT (Average Handling Time)`, `Productivity` ve `SLA` gibi kritik metrikler, birbirleriyle ilişkili ve hedef (`Target`) değerlerle karşılaştırılabilir şekilde üretilir.
* **Stokastik Yaklaşım:** NumPy kullanılarak verilere eklenen gürültü (noise), verinin "fazla mükemmel" görünmesini engeller ve gerçek dünya analizlerine (anomaly detection vb.) uygun hale getirir.
* **Pandas & Veri Yapılandırma:** Excel tabanlı konfigürasyon dosyalarından beslenerek, çok boyutlu DataFrame yapıları kurar.

## 📊 Proje İçeriği & Analitik Odaklar

Aşağıdaki tablo, bu script ile üretilen verilerin hangi analiz yetkinliklerini test etmek için kullanılabileceğini göstermektedir:

| Analiz Alanı | Simüle Edilen Metrikler | Teknik Araçlar | Amaç |
| :--- | :--- | :--- | :--- |
| **Workforce Management** | Headcount, Shift Plan, Productivity | `Pandas`, `NumPy` | Personel verimliliği ve kapasite planlama. |
| **Operational Excellence** | SLA %, AHT Ratio, Volume Trend | `Time-Series Modeling` | Hizmet seviyesi hedeflerinin analizi. |
| **Performance Tracking** | Manager vs. Agent Performance | `Aggregations`, `Joins` | Hiyerarşik raporlama yapıları kurma. |
| **ETL Ready Data** | Clean & Structured Output | `CSV/XLSX Export` | SQL, Tableau veya Power BI'a hazır veri besleme. |

## 🚀 Kullanım
1.  `Sample_Data.xlsx` dosyasında departman hedeflerinizi ve çalışan bilgilerinizi tanımlayın.
2.  `data_generator.py` dosyasını çalıştırarak istediğiniz tarih aralığını belirleyin.
3.  Üretilen `df_final` çıktısını ETL pipeline'ınıza veya görselleştirme aracınıza bağlayın.

## 📈 Gelecek Planları
- [ ] Verilerin doğrudan bir SQL veritabanına (PostgreSQL/BigQuery) otomatik aktarılması (Automated ETL).
- [ ] Streamlit ile kullanıcı dostu bir arayüz (UI) üzerinden veri konfigürasyonu.
- [ ] Farklı sektörler (E-ticaret, Finans) için yeni gürültü modelleri.

---
> **Not:** Bu script ile üretilen verilerle oluşturduğum **End-to-End ETL & Tableau Dashboard** projem çok yakında yayında olacak!
