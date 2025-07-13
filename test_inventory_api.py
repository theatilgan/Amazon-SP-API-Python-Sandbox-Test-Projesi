from sp_api.api import Inventories
from sp_api.base import SellingApiException
from config import MARKETPLACE_ID, check_credentials

def test_inventory_api():
    """Inventories API'sini test eder"""
    print("=== Inventories API Test ===")
    
    # Credentials kontrolü
    missing_vars = check_credentials()
    if missing_vars:
        print(f"❌ Eksik credentials: {', '.join(missing_vars)}")
        return
    
    try:
        # Inventories API instance'ı oluştur (credentials parametresi yok)
        inventory_api = Inventories()
        
        # Stok durumu sorgula (örnek SKU ile)
        print("1. Stok durumu testi...")
        # Not: Gerçek SKU'larınızı kullanmanız gerekecek
        test_sku = "TEST-SKU-001"
        
        inventory_result = inventory_api.get_inventory_summary_marketplace(
            marketplaceIds=[MARKETPLACE_ID],
            sku=test_sku
        )
        
        if inventory_result.payload and inventory_result.payload.get('inventorySummaries'):
            print(f"   {len(inventory_result.payload['inventorySummaries'])} stok kaydı bulundu")
            for i, inventory in enumerate(inventory_result.payload['inventorySummaries'][:3]):
                print(f"   Stok {i+1}: {inventory.get('sku', 'SKU yok')} - {inventory.get('totalQuantity', 0)} adet")
        else:
            print("   Stok kaydı bulunamadı (test SKU kullanıldığı için normal)")
            
        # Stok türlerini listele
        print("\n2. Stok türleri testi...")
        inventory_types_result = inventory_api.get_inventory_summary_marketplace(
            marketplaceIds=[MARKETPLACE_ID]
        )
        
        if inventory_types_result.payload and inventory_types_result.payload.get('inventorySummaries'):
            print(f"   {len(inventory_types_result.payload['inventorySummaries'])} stok türü bulundu")
            for i, inventory in enumerate(inventory_types_result.payload['inventorySummaries'][:3]):
                print(f"   Tür {i+1}: {inventory.get('sku', 'SKU yok')} - {inventory.get('inventoryDetails', {}).get('totalQuantity', 0)} adet")
        else:
            print("   Stok türü bulunamadı")
            
    except SellingApiException as e:
        print(f"   Hata: {e}")
    except Exception as e:
        print(f"   Beklenmeyen hata: {e}")

if __name__ == "__main__":
    test_inventory_api() 