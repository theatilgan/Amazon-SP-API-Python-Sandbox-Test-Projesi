#!/usr/bin/env python3
"""
SP-API Authentication Helper
Access token almak için gerekli fonksiyonlar
"""

import os
import requests
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

def get_access_token():
    """Refresh token kullanarak access token alır"""
    
    refresh_token = os.getenv('SP_API_REFRESH_TOKEN')
    client_id = os.getenv('SP_API_CLIENT_ID')
    client_secret = os.getenv('SP_API_CLIENT_SECRET')
    
    if not all([refresh_token, client_id, client_secret]):
        print("❌ Eksik credentials!")
        return None
    
    # LWA (Login with Amazon) token endpoint
    token_url = "https://api.amazon.com/auth/o2/token"
    
    # Token request payload
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret
    }
    
    try:
        print("🔄 Access token alınıyor...")
        response = requests.post(token_url, data=payload)
        
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data.get('access_token')
            expires_in = token_data.get('expires_in')
            
            print(f"✅ Access token alındı!")
            print(f"   Token: {access_token[:20]}...")
            print(f"   Süre: {expires_in} saniye")
            
            return access_token
        else:
            print(f"❌ Token alınamadı! Status: {response.status_code}")
            print(f"   Hata: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Token alma hatası: {e}")
        return None

def test_authentication():
    """Authentication testi"""
    print("=== SP-API Authentication Test ===")
    
    # Environment variables kontrolü
    required_vars = [
        'SP_API_REFRESH_TOKEN',
        'SP_API_CLIENT_ID', 
        'SP_API_CLIENT_SECRET'
    ]
    
    print("1. Environment variables kontrol ediliyor...")
    for var in required_vars:
        value = os.getenv(var)
        if value:
            print(f"   ✅ {var}: {value[:10]}...")
        else:
            print(f"   ❌ {var}: Eksik!")
            return False
    
    # Access token al
    print("\n2. Access token alınıyor...")
    access_token = get_access_token()
    
    if access_token:
        print("\n3. SP-API test ediliyor...")
        try:
            from sp_api.api import Catalog
            
            # API instance'ı oluştur
            catalog_api = Catalog()
            
            # Basit test
            result = catalog_api.search_catalog_items(
                keywords="test",
                marketplaceIds=['ATVPDKIKX0DER'],
                limit=1
            )
            
            print("   ✅ API çağrısı başarılı!")
            return True
            
        except Exception as e:
            print(f"   ❌ API hatası: {e}")
            return False
    else:
        return False

if __name__ == "__main__":
    test_authentication() 