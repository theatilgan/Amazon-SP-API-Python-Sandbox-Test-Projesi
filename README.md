# Amazon SP-API Sandbox Test Suite

Bu proje Amazon SP-API'nin sandbox modunda test edilmesi için basit Python örnekleri içerir.

## 📋 Gereksinimler

- Python 3.7+
- Amazon SP-API hesabı
- Sandbox erişimi

## 🚀 Kurulum

1. **Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

2. **Çevre değişkenlerini ayarlayın:**
```bash
# env_example.txt dosyasını .env olarak kopyalayın
cp env_example.txt .env
```

3. **.env dosyasını düzenleyin:**
```
SP_API_REFRESH_TOKEN=your_refresh_token_here
LWA_APP_ID=your_client_id_here
LWA_CLIENT_SECRET=your_client_secret_here
MARKETPLACE_ID=ATVPDKIKX0DER
```

## 🧪 Test Çalıştırma

### Tüm testleri çalıştır:
```bash
python run_all_tests.py
```

### Tek tek test etmek için:
```bash
python test_catalog_api.py
python test_orders_api.py
python test_reports_api.py
python test_inventory_api.py
python test_notifications_api.py
```

## 📁 Dosya Yapısı

```
amazon-sandbox/
├── requirements.txt          # Python bağımlılıkları
├── config.py               # API konfigürasyonu
├── env_example.txt         # Örnek çevre değişkenleri
├── run_all_tests.py        # Ana test dosyası
├── test_catalog_api.py     # Catalog API testi
├── test_orders_api.py      # Orders API testi
├── test_reports_api.py     # Reports API testi
├── test_inventory_api.py   # Inventories API testi
└── test_notifications_api.py # Notifications API testi
```

## 🔧 API Anahtarları Nasıl Alınır?

1. [Amazon Seller Central](https://sellercentral.amazon.com/) hesabınıza giriş yapın
2. **Apps & Services** > **Develop Apps** bölümüne gidin
3. Yeni bir uygulama oluşturun
4. **View** butonuna tıklayarak API anahtarlarını alın
5. Sandbox modunda test etmek için **Sandbox** seçeneğini kullanın
6. **Not**: Sandbox modunda AWS anahtarlarına ihtiyaç yoktur

## 📝 Test Edilen API'ler

- **Catalog API**: Ürün arama ve katalog bilgileri
- **Orders API**: Sipariş listesi ve detayları
- **Reports API**: Rapor türleri ve rapor listesi
- **Inventories API**: Stok durumu sorgulama
- **Notifications API**: Bildirim türleri ve abonelikler

## ⚠️ Notlar

- Tüm testler sandbox modunda çalışır
- Gerçek veriler yerine test verileri kullanılır
- Hata durumlarında detaylı mesajlar gösterilir
- API limitlerine dikkat edin

## 🐛 Sorun Giderme

**"Gerekli modüller yüklenemedi" hatası:**
```bash
pip install -r requirements.txt
```

**"Eksik API anahtarları" hatası:**
- `.env` dosyasını oluşturun
- Tüm gerekli anahtarları doldurun

**API hataları:**
- Sandbox modunda olduğunuzdan emin olun
- API anahtarlarının doğru olduğunu kontrol edin
- Marketplace ID'nin doğru olduğunu kontrol edin 