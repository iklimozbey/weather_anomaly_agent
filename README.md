# Hava Durumu Anomali Analiz Ajanı (Weather Anomaly Agent)

Bu proje, internet üzerinden otomatik olarak hava durumu verilerini çeken, işleyen, doğrulayan ve istatistiksel/yapay zekâ yöntemleriyle hava durumundaki anormallikleri (anomalileri) tespit eden bir robot yazılımdır (ajan).

## Özellikler
* **[FETCH]** Canlı hava durumu verilerinin otomatik çekilmesi.
* **[VALIDATE]** Veri bütünlüğü ve eksik kayıt kontrolü.
* **[STORE]** Verilerin yüksek performanslı modern **Parquet** formatında saklanması.
* **[DETECT]** Gelişmiş veri analizi kütüphaneleriyle anomali tespiti.

## Kurulum ve Çalıştırma
Proje, bağımlılıkların izole edilmesi için sanal ortam (venv) kullanılarak geliştirilmiştir.

```bash
# Sanal ortam oluşturma ve aktif etme
python3 -m venv venv
source venv/bin/activate

# Kütüphanelerin kurulması
pip install -r requirements.txt

# Projenin çalıştırılması
python main.py
```
