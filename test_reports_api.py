from sp_api.api import Reports
from sp_api.base import SellingApiException
from config import MARKETPLACE_ID, check_credentials

def test_reports_api():
    """Reports API'sini test eder"""
    print("=== Reports API Test ===")
    
    # Credentials kontrolü
    missing_vars = check_credentials()
    if missing_vars:
        print(f"❌ Eksik credentials: {', '.join(missing_vars)}")
        return
    
    try:
        # Reports API instance'ı oluştur (credentials parametresi yok)
        reports_api = Reports()
        
        # Mevcut raporları listele
        print("1. Rapor listesi testi...")
        reports_result = reports_api.get_reports(
            marketplaceIds=[MARKETPLACE_ID],
            maxCount=5
        )
        
        if reports_result.payload and reports_result.payload.get('reports'):
            print(f"   {len(reports_result.payload['reports'])} rapor bulundu")
            for i, report in enumerate(reports_result.payload['reports'][:3]):
                print(f"   Rapor {i+1}: {report.get('reportId', 'ID yok')} - {report.get('reportType', 'Tür yok')}")
        else:
            print("   Rapor bulunamadı")
            
    except SellingApiException as e:
        print(f"   Hata: {e}")
    except Exception as e:
        print(f"   Beklenmeyen hata: {e}")

if __name__ == "__main__":
    test_reports_api() 