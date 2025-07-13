#!/usr/bin/env python3
"""
SP-API Kütüphanesi ile Basit Test
"""

import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

def test_simple_sp_api():
    """SP-API kütüphanesi ile basit test"""
    print("=== SP-API Kütüphanesi Test ===")
    
    # Environment variables kontrolü
    required_vars = [
        'SP_API_REFRESH_TOKEN',
        'LWA_APP_ID', 
        'LWA_CLIENT_SECRET'
    ]
    
    print("1. Environment variables kontrol ediliyor...")
    for var in required_vars:
        value = os.getenv(var)
        if value:
            print(f"   ✅ {var}: {value[:10]}...")
        else:
            print(f"   ❌ {var}: Eksik!")
            return
    
    print("\n2. SP-API test ediliyor...")
    
    try:
        # SP-API kütüphanesini import et
        from sp_api.api import Catalog
        
        # API instance'ı oluştur (SP-API otomatik olarak env vars kullanır)
        catalog_api = Catalog()
        
        print("   ✅ Catalog API instance'ı oluşturuldu!")
        
        # Basit bir arama denemesi
        print("   🔍 Ürün arama testi...")
        result = catalog_api.search_catalog_items(
            keywords="test",
            marketplaceIds=['ATVPDKIKX0DER'],
            limit=1
        )
        
        print("   ✅ API çağrısı başarılı!")
        
        # Sonucu kontrol et
        if result.payload and result.payload.get('items'):
            print(f"   📦 {len(result.payload['items'])} ürün bulundu")
        else:
            print("   📦 Ürün bulunamadı (sandbox'ta normal)")
            
    except Exception as e:
        print(f"   ❌ Hata: {e}")
        print(f"   Hata türü: {type(e).__name__}")

if __name__ == "__main__":
    test_simple_sp_api() 