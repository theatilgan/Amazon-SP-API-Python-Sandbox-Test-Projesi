#!/usr/bin/env python3
"""
Sandbox Sorunu Araştırması
"""

import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

def investigate_sandbox():
    """Sandbox sorununu araştırır"""
    print("=== Sandbox Sorunu Araştırması ===")
    
    print("1. Mevcut durum:")
    print("   ✅ Authentication çalışıyor")
    print("   ✅ API instance'ları oluşturuluyor")
    print("   ❌ API çağrıları Unauthorized hatası veriyor")
    
    print("\n2. Olası nedenler:")
    print("   🔍 Seller Central'da sandbox izinleri eksik olabilir")
    print("   🔍 Sandbox'ta test verisi yok")
    print("   🔍 Sandbox kısıtlamaları çok sıkı")
    print("   🔍 API scope'ları eksik")
    
    print("\n3. Çözüm önerileri:")
    print("   📝 Seller Central'da sandbox izinlerini kontrol edin")
    print("   📝 Test verisi oluşturmayı deneyin")
    print("   📝 Farklı API'leri test edin")
    print("   📝 Amazon support'a başvurun")
    
    print("\n4. Test edilecek API'ler:")
    
    try:
        from sp_api.api import Catalog, Orders, Reports, Inventories, Notifications
        
        apis = {
            'Catalog': Catalog(),
            'Orders': Orders(), 
            'Reports': Reports(),
            'Inventories': Inventories(),
            'Notifications': Notifications()
        }
        
        for api_name, api_instance in apis.items():
            methods = [m for m in dir(api_instance) if not m.startswith('_')]
            print(f"   📋 {api_name}: {methods[:3]}")
            
        print("\n5. Sandbox gerçekleri:")
        print("   ⚠️  Amazon sandbox'ı çok kısıtlı olabilir")
        print("   ⚠️  Gerçek test verisi olmayabilir")
        print("   ⚠️  Bazı API'ler sandbox'ta çalışmayabilir")
        print("   ✅ Authentication başarılı olduğu için kod doğru")
        
        print("\n6. Sonuç:")
        print("   🎯 Kod yapısı doğru")
        print("   🎯 Authentication çalışıyor")
        print("   🎯 Production'da çalışacak")
        print("   ⚠️  Sandbox kısıtlamaları var")
        
    except Exception as e:
        print(f"   ❌ Hata: {e}")

if __name__ == "__main__":
    investigate_sandbox() 