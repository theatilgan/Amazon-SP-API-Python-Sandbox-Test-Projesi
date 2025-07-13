import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Amazon SP-API Sandbox Konfigürasyonu
# SP-API otomatik olarak environment variables'ları kullanır
# Bu yüzden credentials parametresi geçmeye gerek yok

# Environment variables kontrolü
def check_credentials():
    """Gerekli credentials'ların varlığını kontrol eder"""
    required_vars = [
        'SP_API_REFRESH_TOKEN',
        'LWA_APP_ID', 
        'LWA_CLIENT_SECRET'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    return missing_vars

# Sandbox marketplace ID
MARKETPLACE_ID = os.getenv('MARKETPLACE_ID', 'ATVPDKIKX0DER') 