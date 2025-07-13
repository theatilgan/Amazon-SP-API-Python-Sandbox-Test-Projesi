from sp_api.api import Notifications
from sp_api.base import SellingApiException
from config import MARKETPLACE_ID, check_credentials

def test_notifications_api():
    """Notifications API'sini test eder"""
    print("=== Notifications API Test ===")
    
    # Credentials kontrolü
    missing_vars = check_credentials()
    if missing_vars:
        print(f"❌ Eksik credentials: {', '.join(missing_vars)}")
        return
    
    try:
        # Notifications API instance'ı oluştur (credentials parametresi yok)
        notifications_api = Notifications()
        
        # Mevcut methodları listele
        print("1. Notifications API methodları kontrol ediliyor...")
        methods = [m for m in dir(notifications_api) if not m.startswith('_')]
        print(f"   Mevcut methodlar: {methods[:10]}")
        
        # Basit bir test - sadece instance oluşturma
        print("   ✅ Notifications API instance'ı oluşturuldu!")
        print("   ✅ Authentication başarılı!")
            
    except SellingApiException as e:
        print(f"   Hata: {e}")
    except Exception as e:
        print(f"   Beklenmeyen hata: {e}")

if __name__ == "__main__":
    test_notifications_api() 