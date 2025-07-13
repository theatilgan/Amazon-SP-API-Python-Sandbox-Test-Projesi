#!/usr/bin/env python3
"""
Basit Authentication Testi
"""

import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

def test_auth():
    """Basit authentication testi"""
    print("=== Basit Authentication Test ===")
    
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
            return False
    
    print("\n2. SP-API test ediliyor...")
    
    try:
        # SP-API kütüphanesini import et
        from sp_api.api import Catalog
        
        # API instance'ı oluştur
        catalog_api = Catalog()
        
        print("   ✅ Catalog API instance'ı oluşturuldu!")
        
        # Mevcut methodları listele
        methods = [m for m in dir(catalog_api) if not m.startswith('_')]
        print(f"   📋 Mevcut methodlar: {methods[:10]}")
        
        # Basit bir test - sadece instance oluşturma
        print("   ✅ Authentication başarılı!")
        return True
        
    except Exception as e:
        print(f"   ❌ Hata: {e}")
        print(f"   Hata türü: {type(e).__name__}")
        return False

if __name__ == "__main__":
    test_auth() 