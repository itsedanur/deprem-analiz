import folium.map
import pandas as pd

df = pd.read_csv('deprem.csv', delimiter=';')


#ilk bir kaç satırı görüntüleyelim
# print("İlk 5 Satır:")
# print(df.head())
#veri seti hakkında genel bir bilgi
# print("\nVeri Seti Bilgisi:")
# print(df.info)
#temel istatistiksel özet
# print("\nTemel İstatistiksel Özet:")
# print(df.describe())
#eksik veriler var mı ?
# print("\nEksik veri var mı ?")
# print(df.isnull().sum)

#tarih ve saat sütununu birleştirme

df['TarihSaat'] = pd.to_datetime(df['Tarih'].astype(str)+ ' ' + df['Saat'], format='%Y.%m.%d %H:%M:%S')

df.drop(['Tarih','Saat'], axis=1 , inplace=True)
#birleşmeyi kontrol et
# print("\nGüncellenmiş Veri Tipleri:")
# print(df.dtypes)

#ML ile analiz etme
#düzenleme yapma
df['ML'] = pd.to_numeric(df['ML'] , errors='coerce')
# print("\n'ML' Sütunundaki eksik değerler:")
# print(df['ML'].isnull().sum())
#eğer varsa kadlıralım
df_clean = df.dropna(subset=['ML'])
# print('Temizlenmiş veri seti boyutu :', df_clean.shape)

import matplotlib.pyplot as plt
import seaborn as sns

#TARİHE GÖRE DEPREM SAYISI

# plt.figure(figsize=(12,6))
# sns.countplot(data=df_clean, x=df_clean['TarihSaat'].dt.date , palette='viridis')
# plt.xticks(rotation=45)
# plt.title("Günlere Göre Deprem Sayısı")
# plt.xlabel('Tarih')
# plt.ylabel('Deprem Sayısı')
# plt.tight_layout()
# plt.show()

#DEPREMİN BÜYÜKLÜK DAĞIMI
# plt.figure(figsize=(8,6))
# sns.histplot(df_clean['ML'], bins=50, kde=True, color='skyblue')
# plt.title('Deprem Büyüklük Dağılımı')
# plt.xlabel('Büyüklük (ML)')
# plt.ylabel('Frekans')
# plt.show()

# plt.figure(figsize=(8,6))
# sns.scatterplot(data=df_clean, x='Derinlik(km)' , y ='ML', hue='Yer', palette='deep')
# plt.title('Derinliğine Göre Deprem Büyüklükleri')
# plt.xlabel('Derinlik(km)')
# plt.ylabel('Büyüklük(ML)')
# plt.legend(bbox_to_anchor=(1,1), loc="center")
# plt.tight_layout()
# plt.show()




import folium
#harita merkezini belirle
map_center = [38.0, 35.0]
m = folium.Map(location = map_center , zoom_start=5)
#her bir depremi haritaya ekle

for idx , row in df_clean.iterrows():
    folium.CircleMarker(
        location=[row['Enlem(N)'] , row['Boylam(E)']],
        radius=row['ML']*2,
        popup=f"Yer:{row['Yer']}<br>Büyüklük: {row['ML']}<br>Derinlik:{row['Derinlik(km)']} km ",
        color = 'black',
        fill=True,
        fill_color='black'
    ).add_to(m)

m.save('depremler_haritası.html')
print("İşlem gerçekleşti")
