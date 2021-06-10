
import deger
import tablo_olusturma,csv_dosya_ekleme

def Crm_Sistemi():
    s=0
    d=0
    while s==0 :
        if d==0:
            print("😁CRM sisteme hoş geldiniz😁")
            print("-----------------------------")

        print("""
        Ajanda ve randevu işlemleri için :1
        Teklif ve Yönetim Sistemi için   :2
        Müşteri ve Yönetimi için         :3
        Aktivite Yönetimi için           :4
        Satim İşlemleri için             :5
        Ürün Yönetimi için               :6
        Hatırlatıcı Mesajlar için        :7
        Raporlar için                    :8
        Çıkış için                       :9
            """)

        islem=int(input("Yapmak istediğiniz işlemin değerini giriniz:"))

        if islem==1:
            d=0
            while(d==0):
                print(""" -----Ajanda ve Randevu Sistemi-----
                            Randevu ekle          :1
                            Randevu sil           :2
                            Randevu bilgileri     :3
                            Randevu sayısı        :4
                            Ana ekrana dön        :5
                            """)
                ajan=int(input(" Yapmak istediğiniz işlemin değerini giriniz:"))
                if ajan==1:
                    bilgi_eklemek_icin=(input("Baslik:"), input("İlgili_Kontaklar:"), input("İlgili_Kullanicilar:"),input("Başlangiç Saati ve Tarihi:"), input("Onem Derecesi:"),input("Durum:"), input("Sonuc:"))
                    try:
                        deger.tablo_bilgi_ekle("crm","Ajanda_Randevu","Baslik, İlgili_Kontaklar, İlgili_Kullanİcİlar, Başlangİç_Saati_ve_Tarihi, Onem_Derecesi, Durumu, Sonuc",bilgi_eklemek_icin)
                    except :
                        print("eklemede bilinmeyen hata olusdu.")
                if ajan==2:
                    deger.tablo_bilgi_cikar("crm","Ajanda_Randevu",input(" hangi katagoriye gore :   "),input("secdigin katagoriye gore bilgi :     "))  
                                  
                if ajan==3:
                    print("☻--------Bilgiler---------☻")
                    deger.tablo_bilgileri_goster("crm","Ajanda_Randevu")
                    
                if ajan==4:
                    print("  ↓↓↓↓↓Randevu sayisi↓↓↓↓↓")
                    deger.tablo_bilgi_sayi("crm","Ajanda_Randevu")
                if ajan==5:
                    print("Gercekten ana ekrana donmek istiyor musun? (Y/N) ")
                    say=input()
                    if say=="Y":
                        print("Ana ekran......")
                        d=1
                        
                    



        if islem==2:
            d=0
            while(d==0):
                print(""" -----Teklif ve Yönetim Sistemi-----
                Teklif ve Yönetim Sistemi ekle       :1
                Teklif ve Yönetim Sistemi sil:2
                Teklif ve Yönetim Sistemi bilgileri:3
                Teklif ve Yönetim Sistemi sayısı:4
                Ana ekrana dön:5
                """)
                ajan=int(input(" Yapmak istediğiniz işlemin değerini giriniz:"))
                
                if ajan==1:
                    bilgi_eklemek_icin=(input("Teklif Adi:"),input("Teklif Tarihi:"),input("Kontak:"),input("Fiyat:"),input("Karlilik Bilgileri:"),input("islem:"))
                    try:
                        deger.tablo_bilgi_ekle("crm","Teklif_Yönetim","Teklif_Adi,Teklif_Tarihi,Kontak,Fiyat,Karlilik_Bilgileri,islem",bilgi_eklemek_icin)
                    except :
                        print("eklemede bilinmeyen hata olusdu.")
                if ajan==2:
                    deger.tablo_bilgi_cikar("crm","Teklif_Yönetim",input(" hangi katagoriye gore :   "),input("secdigin katagoriye gore bilgi :     "))
                if ajan==3:
                    print("☻--------Bilgiler---------☻")
                    deger.tablo_bilgileri_goster("crm","Teklif_Yönetim")
                if ajan==4:
                    print("  ↓↓↓↓↓Teklif sayisi↓↓↓↓↓")
                    deger.tablo_bilgi_sayi("crm","Teklif_Yönetim")
                if ajan==5:
                    print("Gercekten ana ekrana donmek istiyor musun? (Y/N) ")
                    say=input()
                    if say=="Y":
                        print("Ana ekran......")
                        d=1
      


        if islem==3:
            d=0
            while(d==0):
                print(""" -----Müşteri ve Yönetim Sistemi-----
                Müşteri ve Yönetimi ekle:1
                Müşteri ve Yönetimi sil:2
                Müşteri ve Yönetimi için bilgileri:3
                Müşteri ve Yönetimi sayısı:4
                Ana ekrana dön:5
                """)
                ajan=int(input(" Yapmak istediğiniz işlemin değerini giriniz:"))
                
                if ajan==1:
                    bilgi_eklemek_icin=(input("ADI SOYADI:"),input("Marka Adı:"),input("Marka Ekonomisi:"),input("Cinsiyet:"),input("Telefon Numarası:"))
                    try:
                        deger.tablo_bilgi_ekle("crm","Müşteri_yönetimi","ADI_SOYADI, Marka_Adı, Marka_Ekonomisi, Cinsiyet, Telefon_numarası",bilgi_eklemek_icin)
                    except :
                        ("Eklemede bilinmeyen hata olustu.")
                if ajan==2:
                    deger.tablo_bilgi_cikar("crm","Müşteri_yönetimi",input(" hangi katagoriye gore :   "),input("secdigin katagoriye gore bilgi :     "))
                if ajan==3:
                    print("☻--------Bilgiler---------☻")
                    deger.tablo_bilgileri_goster("crm","Müşteri_yönetimi")
                if ajan==4:
                    print("  ↓↓↓↓↓Müşteri sayisi↓↓↓↓↓")
                    deger.tablo_bilgi_sayi("crm","Müşteri_yönetimi")
                if ajan==5:
                    print("Gercekten ana ekrana donmek istiyor musun? (Y/N) ")
                    say=input()
                    if say=="Y":
                        print("Ana ekran......")
                        d=1

          


        if islem==4:
            d=0
            while(d==0):
                print(""" -----Aktivite Yönetimi Sistemi-----
                Aktivite ekle          :1
                Aktivite sil           :2
                Aktivite bilgileri     :3
                Aktivite sayısı        :4
                Ana ekrana dön        :5
                """)
                ajan=int(input(" Yapmak istediğiniz işlemin değerini giriniz:"))
                
                if ajan==1:
                    bilgi_eklemek_icin=(input("Aktivite Adi:"),input("Aktivite Yeri:"),input("Aktivite Zamani:"),input("Katilimci Sayisi:"))
                    try:
                        deger.tablo_bilgi_ekle("crm","Aktivite_Yönetimi","Aktivite_Adi,Aktivite_Yeri,Aktivite_Zamani,Katilimci_Sayisi",bilgi_eklemek_icin)
                    except :
                        print("Eklemede bilinmeyen hata olustu.")
                if ajan==2:
                    deger.tablo_bilgi_cikar("crm","Aktivite_Yönetimi",input(" hangi katagoriye gore :   "),input("secdigin katagoriye gore bilgi :     "))
                if ajan==3:
                    print("☻--------Bilgiler---------☻")
                    deger.tablo_bilgileri_goster("crm","Aktivite_Yönetimi")
                if ajan==4:
                    print("  ↓↓↓↓↓Aktivite sayisi↓↓↓↓↓")
                    deger.tablo_bilgi_sayi("crm","Aktivite_Yönetimi")
                if ajan==5:
                    print("Gercekten ana ekrana donmek istiyor musun? (Y/N) ")
                    say=input()
                    if say=="Y":
                        print("Ana ekran......")
                        d=1

        if islem==5:
            d=0
            while(d==0):
                print(""" -----Satim İşlemleri Sistemi-----
                Satım ekle          :1
                Satım sil           :2
                Satım bilgileri     :3
                Satım sayısı        :4
                Ana ekrana dön      :5
            
                """)
                ajan=int(input(" Yapmak istediğiniz işlemin değerini giriniz:"))
                
                if ajan==1:
                    bilgi_eklemek_icin=(input("Satis Adi:"),input("Satis Tarihi:"),input("Satis Yapan:"),input("Kontak:"),input("fiyat:"),input("Ödeme Durumu:"),input("Karlilik:"),input("İslem:"))
                    try:
                        deger.tablo_bilgi_ekle("crm","satislar","satis_adi,satis_tarihi,satis_yapan,kontakt,fiyat,odeme_durumu,karlilik,islem",bilgi_eklemek_icin)
                    except :
                        print("Eklemede bilinmeyen hata olustu.")
                if ajan==2:
                    deger.tablo_bilgi_cikar("crm","satislar",input(" hangi katagoriye gore :   "),input("secdigin katagoriye gore bilgi :     "))
                if ajan==3:
                    print("☻--------Bilgiler---------☻")
                    deger.tablo_bilgileri_goster("crm","satislar")
                if ajan==4:
                    print("  ↓↓↓↓↓Satım sayisi↓↓↓↓↓")
                    deger.tablo_bilgi_sayi("crm","satislar")
                if ajan==5:
                    print("Gercekten ana ekrana donmek istiyor musun? (Y/N) ")
                    say=input()
                    if say=="Y":
                        print("Ana ekran......")
                        d=1
         
        if islem==6:
            d=0
            while(d==0):
                print(""" -----Ürün Yönetimi Sistemi-----
                Ürün ekle          :1
                Ürün sil           :2
                Ürün bilgileri     :3
                Ürün sayısı        :4
                Ana ekrana dön     :5
                """)
                
                ajan=int(input(" Yapmak istediğiniz işlemin değerini giriniz:"))
                
                if ajan==1:
                    bilgi_eklemek_icin=(input("Ürun Kod:"),input("Ürun Adi:"),input("Marka Kategori:"),input("Ürun Fiyat:"),input("Stok Miktari:"),input("Durum:"))
                    try:
                        deger.tablo_bilgi_ekle("crm","urunler","urun_kod,urun_adi,Marka_Kategori,urun_fiyat,stok_miktari,Durum",bilgi_eklemek_icin)
                    except :
                        print("Eklemede bilinmeyen hata olustu.")
                if ajan ==2:
                    deger.tablo_bilgi_cikar("crm","urunler",input(" hangi katagoriye gore :   "),input("secdigin katagoriye gore bilgi :     "))
                if ajan==3:
                    print("☻--------Bilgiler---------☻")
                    deger.tablo_bilgileri_goster("crm","urunler")
                if ajan==4:
                    print("  ↓↓↓↓↓Ürün sayisi↓↓↓↓↓")
                    deger.tablo_bilgi_sayi("crm","urunler")
                if ajan==5:
                    print("Gercekten ana ekrana donmek istiyor musun? (Y/N) ")
                    say=input()
                    if say=="Y":
                        print("Ana ekran......")
                        d=1
            
        if islem==7:
            d=0
            while(d==0):
                print(""" -----Hatırlatıcı Mesajlar Sistemi-----
                Hatırlatıcı mesaj ekle      :1
                Hatırlatıcı mesaj sil       :2
                Hatırlatıcı mesaj bilgileri :3
                Hatırlatıcı mesaj sayısı    :4
                Ana ekrana dön              :5
                """)
                ajan=int(input(" Yapmak istediğiniz işlemin değerini giriniz:"))
                
                if ajan==1:
                    bilgi_eklemek_icin=(input("Baslik:"),input("İlgili Kontaklar:"),input("İlgili Kullanıcılar:"),input("Başlangıç Saati ve Tarihi:"),input("Hatırlatma Tarihi:"),input("Önem Derecesi:"),input("Durumu:"),input("Sonuç:"),input("Hatırlatıcı Mesajlar:"))
                    try:
                        deger.tablo_bilgi_ekle("crm","Hatırlatıcı_Mesajlar","Baslik,İlgili_Kontaklar ,İlgili_Kullanıcılar,Başlangıç_Saati_ve_Tarihi,Hatırlatma_Tarihi,Önem_Derecesi ,Durumu,Sonuç,Hatırlatıcı_mesajlar",bilgi_eklemek_icin)
                    except :
                        print("Eklemede bilinmeyen hata olustu.")
                if ajan==2:
                    deger.tablo_bilgi_cikar("crm","Hatırlatıcı_Mesajlar",input(" hangi katagoriye gore :   "),input("secdigin katagoriye gore bilgi :     "))
                if ajan==3:
                    print("☻--------Bilgiler---------☻")
                    deger.tablo_bilgileri_goster("crm","Hatırlatıcı_Mesajlar")
                if ajan==4:
                    print("  ↓↓↓↓↓Hatırlatıcı mesaj sayisi↓↓↓↓↓")
                    deger.tablo_bilgi_sayi("crm","Hatırlatıcı_Mesajlar")
                if ajan==5:
                    print("Gercekten ana ekrana donmek istiyor musun? (Y/N) ")
                    say=input()
                    if say=="Y":
                        print("Ana ekran......")
                        d=1
            
            

              
        if islem==8:
            f=0
            while(f==0):
                print(""" -----Raporlar-----
                Teklif Raporu         :1
                Tahsilat Raporu       :2
                Satış Raporu          :3
                Hedef Raporu          :4
                Görev Raporu          :5
                Ana ekrana dön        :6
                """)
                a=int(input('işlem giriniz:'))
                if a==1:
                    d=0
                    while(d==0):
                        print(""" -----Teklif Raporu-----
                            Teklif Raporu ekle:1
                            Teklif Raporu sil:2
                            Teklif Raporu bilgileri:3
                            Teklif Raporu sayısı:4
                            Ana ekrana dön:5
                            """)
                        ajan=int(input(" Yapmak istediğiniz işlemin değerini giriniz:"))
                        if ajan==1:
                            bilgi_eklemek_icin=(input("Teklif Adı:"),input("Baslangic Tarihi:"),input("Kontak:"),input("Teklif Yapan:"),input("Durum:"),input("Önem Derecesi:"),input("Durumu:"),input("Tutar:"))
                        try:
                            deger.tablo_bilgi_ekle("crm","Teklif_Yönetimi","Teklif_Adi,Baslangic_Tarihi,Kontak,Teklif_Yapan,Durum,Tutar",bilgi_eklemek_icin)
                        except :
                            print("Eklemede bilinmeyen hata olustu.")
                        if ajan==2:
                            deger.tablo_bilgi_cikar("crm","Teklif_Yönetimi",input(" hangi katagoriye gore :   "),input("secdigin katagoriye gore bilgi :     "))
                        if ajan==3:
                            print("☻--------Bilgiler---------☻")
                            deger.tablo_bilgileri_goster("crm","Teklif_Yönetimi")
                        if ajan==4:
                            print("  ↓↓↓↓↓Teklif Rapor Sayısı sayisi↓↓↓↓↓")
                            deger.tablo_bilgi_sayi("crm","Teklif_Yönetimi")
               
                        if ajan==5:
                            print("""____Devam etmek istediğin işlem____
                            1. Raporlar
                            2. Ana ekran
                            3. İşleme devam et...  
                            """)
                            deli=int(input())
                            if deli==1:
                                d=1
                                print("Raporlara donuluyor......")
                            if deli==2:
                                d=1
                                f=1
                                print("Ana ekrana donuluyor.......")
                        
                        

                if a==2:
                    d=0
                    while(d==0):
                        print(""" -----Tahsilat Raporu-----
                            Tahsilat Raporu ekle:1
                            Tahsilat Raporu  sil:2
                            Tahsilat Raporu bilgileri:3
                            Tahsilat Raporu sayısı:4
                            Ana ekrana dön:5
                            """)
                        ajan=int(input(" Yapmak istediğiniz işlemin değerini giriniz:"))
                        if ajan==1:
                            bilgi_eklemek_icin=(input("Satis_Adi:"),input("Kontak:"),input("Tutar:"),input("Zaman:"),input("Odeme_Durumu:"),input("Odeme_Tipi:"),input("Tahsilat_Durumu:"))
                        try:
                            deger.tablo_bilgi_ekle("crm","Tahsilat_Raporları","Satis_Adi,Kontak,Tutar,Zaman,Odeme_Durumu,Odeme_Tipi,Tahsilat_Durumu",bilgi_eklemek_icin)
                        except :
                            print("Eklemede bilinmeyen hata olustu.")
                        if ajan==2:
                            deger.tablo_bilgi_cikar("crm","Tahsilat_Raporları",input(" hangi katagoriye gore :   "),input("secdigin katagoriye gore bilgi :     "))
                        if ajan==3:
                            print("☻--------Bilgiler---------☻")
                            deger.tablo_bilgileri_goster("crm","Tahsilat_Raporları")
                        if ajan==4:
                            print("  ↓↓↓↓↓Teklif Rapor Sayısı ↓↓↓↓↓")
                            deger.tablo_bilgi_sayi("crm","Tahsilat_Raporları")
                        if ajan==5:
                            print("""____Devam etmek istediğin işlem____
                            1. Raporlar
                            2. Ana ekran
                            3. İşleme devam et... 
                            """)
                            deli=int(input())
                            if deli==1:
                                d=1
                                print("Raporlara donuluyor......")
                            if deli==2:
                                d=1
                                f=1
                                print("Ana ekrana donuluyor.......")
               
                
                
                if a==3:
                    d=0
                    while(d==0):
                        print(""" -----Satış Raporu-----
                            Satış Raporu ekle:1
                            Satış Raporu sil:2
                            Satış Raporu bilgileri:3
                            Satış Raporu sayısı:4
                            Ana ekrana dön:5
                            """)
                        ajan=int(input(" Yapmak istediğiniz işlemin değerini giriniz:"))
                        if ajan==1:
                            bilgi_eklemek_icin=(input("Satis_Adi:"),input("SAtis_Tarihi:"),input("Kontak:"),input("Satis_Yapan:"),input("Durum:"),input("Tutar:"),input("Kalan_Tutar:"))
                        try:
                            deger.tablo_bilgi_ekle("crm","Satış_Raporları","Satis_Adi,SAtis_Tarihi,Kontak,Satis_Yapan,Durum,Tutar,Kalan_Tutar",bilgi_eklemek_icin)
                        except :
                            print("Eklemede bilinmeyen hata olustu.")
                        if ajan==2:
                            deger.tablo_bilgi_cikar("crm","Satış_Raporları",input(" hangi katagoriye gore :   "),input("secdigin katagoriye gore bilgi :     "))
                        if ajan==3:
                            print("☻--------Bilgiler---------☻")
                            deger.tablo_bilgileri_goster("crm","Satış_Raporları")
                        if ajan==4:
                            print("  ↓↓↓↓↓Teklif Rapor Sayısı ↓↓↓↓↓")
                            deger.tablo_bilgi_sayi("crm","Satış_Raporları")
                        if ajan==5:
                            print("""____Devam etmek istediğin işlem____
                            1. Raporlar
                            2. Ana ekran
                            3. İşleme devam et... 
                            """)
                            deli=int(input())
                            if deli==1:
                                d=1
                                print("Raporlara donuluyor......")
                            if deli==2:
                                d=1
                                f=1
                                print("Ana ekrana donuluyor.......")
                if a==4:
                    d=0
                    while(d==0):
                        print(""" -----Hedef Raporu-----
                            Hedef Raporu ekle:1
                            Hedef Raporu sil:2
                            Hedef Raporu bilgileri:3
                            Hedef Raporu sayısı:4
                            Ana ekrana dön:5
                            """)
                        ajan=int(input(" Yapmak istediğiniz işlemin değerini giriniz:"))
                        if ajan==1:
                            bilgi_eklemek_icin=(input("Kullanici:"),input("Hedef Tipi:"),input("Hedef:"),input("Gerceklesen:"),input("Gerceklesme_Yuzdesi:"),input("Prim:"),input("Prim_Tutari:"))
                        try:
                            deger.tablo_bilgi_ekle("crm","Hedef_Raporları","Kullanici,Hedef_Tipi,Hedef,Gerceklesen,Gerceklesme_Yuzdesi,Prim,Prim_Tutari",bilgi_eklemek_icin)
                        except :
                            print("Eklemede bilinmeyen hata olustu.")
                        if ajan==2:
                            deger.tablo_bilgi_cikar("crm","Hedef_Raporları",input(" hangi katagoriye gore :   "),input("secdigin katagoriye gore bilgi :     "))
                        if ajan==3:
                            print("☻--------Bilgiler---------☻")
                            deger.tablo_bilgileri_goster("crm","Hedef_Raporları")
                        if ajan==4:
                            print("  ↓↓↓↓↓Teklif Rapor Sayısı ↓↓↓↓↓")
                            deger.tablo_bilgi_sayi("crm","Hedef_Raporları")
                        if ajan==5:
                            print("""____Devam etmek istediğin işlem____
                            1. Raporlar
                            2. Ana ekran
                            3. İşleme devam et... 
                            """)
                            deli=int(input())
                            if deli==1:
                                d=1
                                print("Raporlara donuluyor......")
                            if deli==2:
                                d=1
                                f=1
                                print("Ana ekrana donuluyor.......")
                if a==5:
                    d=0
                    while(d==0):
                        print(""" -----Görev Raporu-----
                            Görev Raporu ekle:1
                            Görev Raporu sil:2
                            Görev Raporu bilgileri:3
                            Görev Raporu sayısı:4
                            Ana ekrana dön:5
                            """)
                        ajan=int(input(" Yapmak istediğiniz işlemin değerini giriniz:"))
                        if ajan==1:
                            bilgi_eklemek_icin=(input("Baslik:"),input("İlgili Kontaklar:"),input("İlgili Kullanıcılar:"),input("Başlangıç Saati ve Tarihi:"),input("Hatırlatma Tarihi:"),input("Önem Derecesi:"),input("Durumu:"),input("Sonuç:"),input("Hatırlatıcı Mesajlar:"))
                        try:
                            deger.tablo_bilgi_ekle("crm","Görev_Raporları","Baslik,ilgili_Kontaklar,ilgili_Kullanicilar,Baslangic_Tarihi,Tip,Durum,Onem_Derecesi,Hatirlatma",bilgi_eklemek_icin)
                        except :
                            print("Eklemede bilinmeyen hata olustu.")
                        if ajan==2:
                            deger.tablo_bilgi_cikar("crm","Görev_Raporları",input(" hangi katagoriye gore :   "),input("secdigin katagoriye gore bilgi :     "))
                        if ajan==3:
                            print("☻--------Bilgiler---------☻")
                            deger.tablo_bilgileri_goster("crm","Görev_Raporları")
                        if ajan==4:
                            print("  ↓↓↓↓↓Teklif Rapor Sayısı ↓↓↓↓↓")
                            deger.tablo_bilgi_sayi("crm","Görev_Raporları")
                        if ajan==5:
                            print("""____Devam etmek istediğin işlem____
                            1. Raporlar
                            2. Ana ekran
                            3. İşleme devam et... 
                            """)
                            deli=int(input())
                            if deli==1:
                                d=1
                                print("Raporlara donuluyor......")
                            if deli==2:
                                d=1
                                f=1
                                print("Ana ekrana donuluyor.......")
                if  a==6:
                    print("Gercekten ana ekrana donmek istiyor musun? (Y/N) ")
                    say=input()
                    if say=="Y":
                        print("Ana ekran......")
                        f=1
                    
                        
            
        if islem==9:
            print("gerçekten çıkmak istiyor musunuz? (Y/N) ")
            say=input()
            if say=="Y":
                print('Program sonlandırılıyor...')
                s=1
        



Crm_Sistemi()
