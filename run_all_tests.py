#!/usr/bin/env python3
"""
Amazon SP-API Sandbox Test Suite
Tüm API'leri test etmek için ana dosya
"""

import sys
import os

# Gerekli modülleri import et
try:
    from test_catalog_api import test_catalog_api
    from test_orders_api import test_orders_api
    from test_reports_api import test_reports_api
    from test_inventory_api import test_inventory_api
    from test_notifications_api import test_notifications_api
    from config import check_credentials
except ImportError as e:
    print(f"Gerekli modüller yüklenemedi: {e}")
    print("Lütfen 'pip install -r requirements.txt' komutunu çalıştırın")
    sys.exit(1)

def main():
    """Tüm API testlerini çalıştırır"""
    print("Amazon SP-API Sandbox Test Suite")
    print("=" * 50)
    
    # Credentials kontrolü
    missing_vars = check_credentials()
    if missing_vars:
        print("❌ Eksik API anahtarları:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nLütfen .env dosyasını oluşturun ve gerekli anahtarları ekleyin.")
        print("Örnek: env_example.txt dosyasını .env olarak kopyalayın ve değerleri doldurun.")
        return
    
    print("✅ API anahtarları kontrol edildi")
    print()
    
    # Testleri çalıştır
    tests = [
        ("Catalog API", test_catalog_api),
        ("Orders API", test_orders_api),
        ("Reports API", test_reports_api),
        ("Inventories API", test_inventory_api),
        ("Notifications API", test_notifications_api)
    ]
    
    for test_name, test_func in tests:
        print(f"\n🔍 {test_name} test ediliyor...")
        try:
            test_func()
            print(f"✅ {test_name} testi tamamlandı")
        except Exception as e:
            print(f"❌ {test_name} testinde hata: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Tüm testler tamamlandı!")

if __name__ == "__main__":
    main() 