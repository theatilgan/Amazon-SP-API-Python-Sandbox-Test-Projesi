from sp_api.api import Orders
from sp_api.base import SellingApiException
from config import MARKETPLACE_ID, check_credentials
from datetime import datetime, timedelta

def test_orders_api():
    """Orders API'sini test eder"""
    print("=== Orders API Test ===")
    
    # Credentials kontrolü
    missing_vars = check_credentials()
    if missing_vars:
        print(f"❌ Eksik credentials: {', '.join(missing_vars)}")
        return
    
    try:
        # Orders API instance'ı oluştur (credentials parametresi yok)
        orders_api = Orders()
        
        # Son 30 günün siparişlerini getir
        print("1. Sipariş listesi testi...")
        created_after = datetime.now() - timedelta(days=30)
        
        orders_result = orders_api.get_orders(
            MarketplaceIds=[MARKETPLACE_ID],
            CreatedAfter=created_after.isoformat(),
            MaxResultsPerPage=5
        )
        
        if orders_result.payload and orders_result.payload.get('Orders'):
            print(f"   {len(orders_result.payload['Orders'])} sipariş bulundu")
            for i, order in enumerate(orders_result.payload['Orders'][:3]):
                print(f"   Sipariş {i+1}: {order.get('AmazonOrderId', 'ID yok')} - {order.get('OrderStatus', 'Durum yok')}")
        else:
            print("   Sipariş bulunamadı")
            
    except SellingApiException as e:
        print(f"   Hata: {e}")
    except Exception as e:
        print(f"   Beklenmeyen hata: {e}")

if __name__ == "__main__":
    test_orders_api() 