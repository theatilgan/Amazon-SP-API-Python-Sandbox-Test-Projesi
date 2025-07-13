#!/usr/bin/env python3
"""
Sandbox'a Özel Test
"""

import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

def test_sandbox_specific():
    """Sandbox'a özel testler"""
    print("=== Sandbox'a Özel Test ===")
    
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
    
    print("\n2. Sandbox marketplace ID kontrolü...")
    marketplace_id = os.getenv('MARKETPLACE_ID', 'ATVPDKIKX0DER')
    print(f"   Kullanılan Marketplace ID: {marketplace_id}")
    
    # Sandbox marketplace ID'leri
    sandbox_marketplaces = {
        'US': 'ATVPDKIKX0DER',
        'CA': 'A2EUQ1WTGCTBG2',
        'UK': 'A1F83G8C2ARO7P',
        'DE': 'A1PA6795UKMFR9',
        'FR': 'A13V1IB3VIYZZH',
        'IT': 'APJ6JRA9NG5V4',
        'ES': 'A1RKKUPIHCS9HS',
        'JP': 'A1VC38T7YXB528'
    }
    
    print("   Mevcut sandbox marketplace ID'leri:")
    for country, mpid in sandbox_marketplaces.items():
        print(f"   - {country}: {mpid}")
    
    print("\n3. Basit API testi...")
    
    try:
        from sp_api.api import Catalog
        
        # Catalog API instance'ı oluştur
        catalog_api = Catalog()
        
        print("   ✅ Catalog API instance'ı oluşturuldu!")
        
        # Basit bir test - sadece instance oluşturma
        print("   🔍 Basit API çağrısı deneniyor...")
        
        # Farklı marketplace ID'lerle test et
        for country, mpid in sandbox_marketplaces.items():
            print(f"   Testing {country} ({mpid})...")
            try:
                result = catalog_api.list_items(
                    marketplaceIds=[mpid],
                    maxResults=1
                )
                print(f"   ✅ {country} çalışıyor!")
                break
            except Exception as e:
                print(f"   ❌ {country} hatası: {str(e)[:50]}...")
        
        print("\n4. Sandbox özellikleri:")
        print("   📝 Sandbox'ta gerçek veri olmayabilir")
        print("   📝 Bazı API'ler sandbox'ta kısıtlı olabilir")
        print("   📝 Test verisi oluşturmak gerekebilir")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Hata: {e}")
        return False

if __name__ == "__main__":
    test_sandbox_specific() 