import numpy as np
import pandas as pd # Gerekli kütüphaneleri yüklemek için.

pd.set_option('display.max_columns', None) # Oluşturduğumuz kolonların hepsini görebilmek için.
pd.set_option('display.width', 1000) # Oluşturduğumuz kolonları yan yana tek satırda görebilmek için.

PU_Dashboard = pd.read_excel("synthetic_workforce_data_generator/Sample_Data.xlsx", sheet_name="Queue Dashboard") # Excel üzerinden oluşturduğumuz örnek veriyi dataframe olarak kaydediyoruz.

PU_Dashboard.info() # kolon tiplerini ve isimlerini görebilmek için.

Weights = [0.05,0.048,0.046,0.042,0.032,0.021,0.019,0.018,0.019,0.021,0.022,0.025,0.03,0.034,0.042,0.049,0.051,0.052,0.055,0.059,0.061,0.068,0.072,0.064]
# Burada gün içi trend oluşturmak için günün farklı saatlerine farklı ağırlıklar atandmıştır.Veriye gerçekçi bir varyasyon katmak için rastgele gürültü (noise) eklenecektir.

Date = pd.to_datetime("28.02.2026 23:00", dayfirst=True) # Veri oluşturmak istediğimiz aralığın ilk gününden bir gün öncesinin son saati.
Target_Date = pd.to_datetime("31.03.2026 23:00", dayfirst=True) # veri oluşturmak istediğimiz aralığın son günününe ait son saat dilimi.

df_list_1 = [] # aşağıdaki döngüde oluşturulacak verileri tutacağımız boş liste

while Date < Target_Date :  # Oluşturmak istediğimiz gün aralığı kadar döngü oluşturacak while döngüsü

    df_list = [] # aşağıdaki döngüde oluşturulacak verileri tutacağımız boş liste

    for row in PU_Dashboard.itertuples(): # Veri setindeki her bir iş birimi (PU) için üretilicek saatlik verileri her gün için tekrarlayacak for döngüsü

        Daily_Volume = row.Daily_Volume # her döngüde yukarıdaki dataframe' den ilgili PUya ait verileri çekecek ve aşağıdaki saatlik döngüye iletecek.
        Pu_Title = row.Power_Unite # her döngüde yukarıdaki dataframe' den ilgili PUya ait verileri çekecek ve aşağıdaki saatlik döngüye iletecek.
        Pu_Id = row.PU_ID # her döngüde yukarıdaki dataframe' den ilgili PUya ait verileri çekecek ve aşağıdaki saatlik döngüye iletecek.
        AHT = row.AHT_Sec # her döngüde yukarıdaki dataframe' den ilgili PUya ait verileri çekecek ve aşağıdaki saatlik döngüye iletecek.
        AHT_Target = row.AHT_TGT # her döngüde yukarıdaki dataframe' den ilgili PUya ait verileri çekecek ve aşağıdaki saatlik döngüye iletecek.
        Date_day = Date # Bir üst döngüden gün bilgisini alacak olan satır.

        data_points = [] # aşağıdaki döngüde oluşturulacak verileri tutacağımız boş liste

        for i in Weights: # saatlik verileri satır satır oluşturacak olan for döngüsü.
            noise = np.random.uniform(-55, 55) # total input satırına eklenecek olan random gürültü değeri.
            Date_hour = Date_day + pd.Timedelta(hours=1) # her iterasyonda saati bir saat ileri atacak olan satır.
            total_input= round((Daily_Volume * i) + noise) # o saate ait ağırlığın ve gürültünün birleştirilerek gerçeğe yakın rastgele bir total input üreten satır.
            total_output = round(total_input + np.random.uniform(-5, 5)) # output üreten satır
            ontime_output = round(total_input + np.random.uniform(-(total_input * 0.2), (total_input * 0.2))) # zamanında çözülmüş caseleri simule eden bilgiyi ifade eden satır.
            if ontime_output > total_output :
                ontime_output = total_output # zamanında çözülen caseler, çözülen caselerden daha büyük olamayacağı için böyle bir if formulu kullandık.
            Hourly_AHT = round(AHT + np.random.uniform(-8, 8))  # aht değerini üreten satır.
            AHT_Ratio = round(Hourly_AHT/AHT_Target,2) # aht ratio değerini hesaplayan satır.
            Productivity = round(3600/Hourly_AHT,2) # productivity değerini hesaplayan satır.
            SLA = round(ontime_output/total_output,2) # sla değerini hesaplayan satır.
            new_row = {'Date': Date_hour,
                        'Pu_Id': Pu_Id,
                        'Pu_Title': Pu_Title,
                        'total_input': total_input,
                        'total_output': total_output,
                        'ontime_output': ontime_output,
                        'Hourly_AHT': Hourly_AHT,
                        'AHT_Target': AHT_Target,
                        'AHT_Ratio': AHT_Ratio,
                        'Productivity': Productivity,
                        'SLA': SLA} # yukarıda üretilen bilgileri satır olarak kaydetmemize yarayan sözlük yapısı.
            data_points.append(new_row) # her iterasyonda satır satır boş listeye veri giren satır.
            Date_day = Date_hour # Bir sonraki satır için saati +1 ile değiştiren satır.

        df_temp= pd.DataFrame(data_points) # her pu için oluşturulmuş saatlik verileri tuttuğumuz dataframe
        df_list.append(df_temp) # her pu için oluşturulmuş saatlik verileri tuttuğumuz dataframeleri kaydettiğimiz liste

    df_master = pd.concat(df_list, ignore_index=True) # her gün için oluşturulmuş verileri alt alta birleştiren satır.
    df_list_1.append(df_master) # her gün için oluşturulmuş verileri alt alta birleştirdiğimiz dataframeleri kaydettiğimiz liste
    Date = Date + pd.Timedelta(days=1) # her döngünün sonunda bir sonraki güne geçmemizi sağlayan satır.

df_final = pd.concat(df_list_1, ignore_index=True)
# her gün için oluşturulmuş verileri alt alta birleştirdiğimiz dataframeleri kaydettiğimiz liste leri birleştirerek nihai dataframe e ulaştığımız son adım.

df_final.to_csv("Volume_Information.csv", index=False)  # Oluşturduğumuz verinin csv olarak çıktısını aldığımız satır.
