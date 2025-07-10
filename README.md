# Deprem Analiz ve Harita Projesi

Bu proje, Türkiye'deki depremleri analiz eder ve interaktif harita üzerinde gösterir.

##  Dosyalar
- `deprem.py` → Verileri işler, harita üretir.
- `deprem.xlsx` → Deprem verisi (Excel formatında).
- `depremler_haritası.html` → Çıktı haritası (folium ile oluşturulmuş).

##  Nasıl Çalıştırılır?
1. Gerekli paketleri kur:
pip install pandas folium openpyxl

2. Python dosyasını çalıştır:
python deprem.py


3. `depremler_haritası.html` dosyasını tarayıcıda açarak haritayı görebilirsin.

##  Özellikler
- Harita üzerinde her deprem daire olarak gösterilir.
- Popup ile yer, büyüklük ve derinlik bilgisi sunulur.

Eda Nur Unal

