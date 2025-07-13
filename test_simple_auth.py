#!/usr/bin/env python3
"""
Basit SP-API Authentication Testi
"""

import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

def test_simple_auth():
    """Basit authentication testi"""
    print("=== Basit Authentication Test ===")
    
    # Environment variables'ları kontrol et
    required_vars = [
        'SP_API_REFRESH_TOKEN',
        'SP_API_CLIENT_ID', 
        'SP_API_CLIENT_SECRET'
    ]
    
    print("Environment variables kontrol ediliyor...")
    for var in required_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ {var}: {value[:10]}...")
        else:
            print(f"❌ {var}: Eksik!")
    
    print("\nSP-API test ediliyor...")
    
    try:
        from sp_api.api import Catalog
        
        # Basit bir test - sadece API instance'ı oluştur
        catalog_api = Catalog()
        
        print("✅ SP-API başarıyla yüklendi!")
        print("✅ Catalog API instance'ı oluşturuldu!")
        
        # Basit bir arama denemesi
        print("\nBasit arama testi...")
        result = catalog_api.search_catalog_items(
            keywords="test",
            marketplaceIds=['ATVPDKIKX0DER'],
            limit=1
        )
        
        print("✅ API çağrısı başarılı!")
        
    except Exception as e:
        print(f"❌ Hata: {e}")
        print(f"Hata türü: {type(e).__name__}")

if __name__ == "__main__":
    test_simple_auth() 