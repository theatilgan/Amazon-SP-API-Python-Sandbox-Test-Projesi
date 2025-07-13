from sp_api.api import Catalog
from sp_api.base import SellingApiException
from config import MARKETPLACE_ID, check_credentials

def test_catalog_api():
    """Catalog API'sini test eder"""
    print("=== Catalog API Test ===")
    
    # Credentials kontrolü
    missing_vars = check_credentials()
    if missing_vars:
        print(f"❌ Eksik credentials: {', '.join(missing_vars)}")
        return
    
    try:
        # Catalog API instance'ı oluştur (credentials parametresi yok)
        catalog_api = Catalog()
        
        # Basit bir ürün listesi - doğru method ismi
        print("1. Ürün listesi testi...")
        list_result = catalog_api.list_items(
            marketplaceIds=[MARKETPLACE_ID],
            maxResults=5
        )
        
        if list_result.payload and list_result.payload.get('items'):
            print(f"   {len(list_result.payload['items'])} ürün bulundu")
            for i, item in enumerate(list_result.payload['items'][:3]):
                print(f"   Ürün {i+1}: {item.get('asin', 'ASIN yok')}")
        else:
            print("   Ürün bulunamadı (sandbox'ta normal)")
            
    except SellingApiException as e:
        print(f"   Hata: {e}")
    except Exception as e:
        print(f"   Beklenmeyen hata: {e}")

if __name__ == "__main__":
    test_catalog_api() 