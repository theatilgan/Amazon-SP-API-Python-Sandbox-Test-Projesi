#!/usr/bin/env python3
"""
Access Token ile SP-API Testi
"""

import os
import requests
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

def get_access_token():
    """Refresh token kullanarak access token alır"""
    
    refresh_token = os.getenv('SP_API_REFRESH_TOKEN')
    client_id = os.getenv('LWA_APP_ID')
    client_secret = os.getenv('LWA_CLIENT_SECRET')
    
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

def test_catalog_with_token():
    """Access token ile Catalog API testi"""
    print("=== Access Token ile Catalog API Test ===")
    
    # Access token al
    access_token = get_access_token()
    if not access_token:
        return
    
    # SP-API Catalog endpoint (sandbox)
    catalog_url = "https://sandbox.sellingpartnerapi-na.amazon.com/catalog/v0/items"
    
    # Headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'x-amz-access-token': access_token
    }
    
    # Query parameters
    params = {
        'keywords': 'laptop',
        'marketplaceIds': 'ATVPDKIKX0DER',
        'limit': 5
    }
    
    try:
        print("🔍 Catalog API çağrısı yapılıyor...")
        response = requests.get(catalog_url, headers=headers, params=params)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ API çağrısı başarılı!")
            
            if data.get('items'):
                print(f"   {len(data['items'])} ürün bulundu")
                for i, item in enumerate(data['items'][:3]):
                    title = item.get('attributes', {}).get('title', 'Başlık yok')
                    print(f"   Ürün {i+1}: {title}")
            else:
                print("   Ürün bulunamadı")
        else:
            print(f"❌ API hatası: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"❌ API çağrısı hatası: {e}")

def test_orders_with_token():
    """Access token ile Orders API testi"""
    print("\n=== Access Token ile Orders API Test ===")
    
    # Access token al
    access_token = get_access_token()
    if not access_token:
        return
    
    # SP-API Orders endpoint (sandbox)
    orders_url = "https://sandbox.sellingpartnerapi-na.amazon.com/orders/v0/orders"
    
    # Headers
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'x-amz-access-token': access_token
    }
    
    # Query parameters
    params = {
        'MarketplaceIds': 'ATVPDKIKX0DER',
        'MaxResultsPerPage': 5
    }
    
    try:
        print("🔍 Orders API çağrısı yapılıyor...")
        response = requests.get(orders_url, headers=headers, params=params)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ API çağrısı başarılı!")
            
            if data.get('Orders'):
                print(f"   {len(data['Orders'])} sipariş bulundu")
                for i, order in enumerate(data['Orders'][:3]):
                    order_id = order.get('AmazonOrderId', 'ID yok')
                    status = order.get('OrderStatus', 'Durum yok')
                    print(f"   Sipariş {i+1}: {order_id} - {status}")
            else:
                print("   Sipariş bulunamadı")
        else:
            print(f"❌ API hatası: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"❌ API çağrısı hatası: {e}")

if __name__ == "__main__":
    test_catalog_with_token()
    test_orders_with_token() 