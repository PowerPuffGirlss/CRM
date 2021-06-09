import deger

deger.database_ac("crm")


deger.database_tablo_olustur("crm",
"urunler",
"""id INT AUTO_INCREMENT PRIMARY KEY, urun_kod  INT  NOT NULL , urun_adi VARCHAR(55)  NOT NULL , Marka_Kategori VARCHAR(55) NOT NULL , urun_fiyat INT NOT NULL , stok_miktari VARCHAR(55) NOT NULL , Durum VARCHAR(300)""")

deger.database_tablo_olustur("crm",
"satislar",
"""id INT AUTO_INCREMENT PRIMARY KEY, satis_adi  VARCHAR(15)  NOT NULL ,satis_tarihi DATETIME NOT NULL , satis_yapan VARCHAR(55), kontakt VARCHAR(55), fiyat INT  NOT NULL , odeme_durumu  VARCHAR(300), karlilik VARCHAR(55), islem VARCHAR(300)""")

deger.database_tablo_olustur("crm",
"sirketler","""id INT AUTO_INCREMENT PRIMARY KEY, sirket_adi  VARCHAR(15) NOT NULL , failiyet_yili DATETIME NOT NULL  ,danisman VARCHAR(55),kontakt VARCHAR(55), iliskidurumu VARCHAR(55), hakinda VARCHAR(300)""")

# deger.database_tablo_olustur("crm",
# "sirketler","""id INT AUTO_INCREMENT PRIMARY KEY, marka_adi VARCHAR(85) ,durum  VARCHAR(300), Oluşturulma_Tarihi  DATETIME , islem  VARCHAR(300)""")

# deger.tablo_bagla("csv","urunler","sirketler","Marka_Kategori","marka_adi")

deger.database_tablo_olustur("crm","Müşteri_Yönetimi","ID INT AUTO_INCREMENT PRIMARY KEY, ADI_SOYADI VARCHAR(45), Marka_Adı VARCHAR(45) ,Marka_Ekonomisi VARCHAR(45),Cinsiyet VARCHAR(45) ,Telefon_numarası INT  ")
#deger.tablo_bilgi_ekle("crm","Musteri","ID,Musteriisim,Musteriekonomisi,Cinsiyet,Mezundurumu",(111111,"Mustafa","Orta","E","Üniversite") )
#deger.bilgi_toplama("crm","Müşteri_Yönetimi","Müşteri_yönetimi.csv")
#deger.tablo_bilgileri_goster("crm","Müşteri_Yönetimi")
#deger.tablo_bilgi_sayi("crm","Müşteri_Yönetimi")

deger.database_tablo_olustur("crm","Hatırlatıcı_Mesajlar","ID INT AUTO_INCREMENT PRIMARY KEY, Baslik VARCHAR(45),İlgili_Kontaklar  VARCHAR(45) ,İlgili_Kullanıcılar VARCHAR(45),Başlangıç_Saati_ve_Tarihi DATETIME ,Hatırlatma_Tarihi DATETIME,Önem_Derecesi VARCHAR(45),Durumu VARCHAR(165),Sonuç VARCHAR(165),Hatırlatıcı_mesajlar VARCHAR(165)")
#deger.tablo_bilgi_ekle("crm","Hatırlatıcı_Mesajlar","ID,Musteriisim,Musteriekonomisi,Cinsiyet,Mezundurumu",(111111,"Mustafa","Orta","E","Üniversite") )
# deger.bilgi_toplama("crm","Hatırlatıcı_Mesajlar","Hatırlatıcı_mesaj.csv")
#deger.tablo_bilgileri_goster("crm","Hatırlatıcı_Mesajlar")
#deger.tablo_bilgi_sayi("crm","Hatırlatıcı_Mesajlar")

deger.database_tablo_olustur("crm","Ajanda_Randevu","ID INT AUTO_INCREMENT PRIMARY KEY, Baslik VARCHAR(45), İlgili_Kontaklar VARCHAR(45) ,İlgili_Kullanİcİlar VARCHAR(45),Başlangİç_Saati_ve_Tarihi DATETIME ,Onem_Derecesi VARCHAR(45) ,Durumu VARCHAR(165),Sonuc VARCHAR(165) ")
# deger.tablo_bilgi_ekle("crm","Musteri","ID,Musteriisim,Musteriekonomisi,Cinsiyet,Mezundurumu",(111111,"Mustafa","Orta","E","Üniversite") )
# deger.bilgi_toplama("crm","Ajanda_Randevu","ajanda_randevu.csv")
# deger.tablo_bilgileri_goster("crm","Ajanda_Randevu")
# deger.tablo_bilgi_sayi("crm","Ajanda_Randevu")





deger.database_tablo_olustur("crm","Teklif_Yönetimi","id INT AUTO_INCREMENT PRIMARY KEY, Teklif_Adi VARCHAR(15) , Teklif_Tarihi VARCHAR(15), Kontak VARCHAR(15) , Fiyat VARCHAR(15) , Karlilik_Bilgileri VARCHAR(15),  islem VARCHAR(15) ")
# deger.bilgi_toplama("crm","Teklif_Yönetimi","Crm_Sistemi/Teklif_Yönetim.csv")

deger.database_tablo_olustur("crm","Teklif_Raporları","id INT AUTO_INCREMENT PRIMARY KEY, Teklif_Adi VARCHAR(15) , Baslangic_Tarihi VARCHAR(15), Kontak VARCHAR(15) , Teklif_Yapan VARCHAR(15) , Durum VARCHAR(15),  Tutar VARCHAR(15) ")
# deger.bilgi_toplama("crm","Teklif_Raporları","Crm_Sistemi/Teklif_Rapor.csv")

deger.database_tablo_olustur("crm","Satış_Raporları","id INT AUTO_INCREMENT PRIMARY KEY, Satis_Adi VARCHAR(15) , Satis_Tarihi VARCHAR(15), Kontak VARCHAR(15) , Satis_Yapan VARCHAR(15) , Durum VARCHAR(15),  Tutar VARCHAR(15),  Kalan_Tutar VARCHAR(15) ")
# deger.bilgi_toplama("crm","Satış_Raporları","Crm_Sistemi/Satıs_Rapor.csv")

deger.database_tablo_olustur("crm","Tahsilat_Raporları","id INT AUTO_INCREMENT PRIMARY KEY, Satis_Adi VARCHAR(15) , Kontak VARCHAR(50), Tutar VARCHAR(15) , Zaman VARCHAR(15) , Odeme_Durumu VARCHAR(15),  Odeme_Tipi VARCHAR(15),  Tahsilat_Durumu VARCHAR(15) ")
# deger.bilgi_toplama("crm","Tahsilat_Raporları","Crm_Sistemi/Tahsilat_Rapor.csv")

deger.database_tablo_olustur("crm","Görev_Raporları","id INT AUTO_INCREMENT PRIMARY KEY, Baslik VARCHAR(55) , ilgili_Kontaklar VARCHAR(50), ilgili_Kullanicilar VARCHAR(15) , Baslangic_Tarihi VARCHAR(55) , Tip VARCHAR(55),  Durum VARCHAR(55),  Onem_Derecesi VARCHAR(55),  Hatirlatma VARCHAR(55) ")
# deger.bilgi_toplama("crm","Görev_Raporları","Crm_Sistemi/Görev_Rapor.csv")

deger.database_tablo_olustur("crm","Hedef_Raporları","id INT AUTO_INCREMENT PRIMARY KEY, Kullanici VARCHAR(55) , Hedef_Tipi VARCHAR(50), Hedef VARCHAR(15) , Gerceklesen VARCHAR(55) , Gerceklesme_Yuzdesi VARCHAR(55),  Prim VARCHAR(55),  Prim_Tutari VARCHAR(55) ")
# deger.bilgi_toplama("crm","Hedef_Raporları","Crm_Sistemi/Hedef_Rapor.csv")

deger.database_tablo_olustur("crm","Aktivite_Yönetimi","id INT AUTO_INCREMENT PRIMARY KEY, Aktivite_Adi VARCHAR(55) , Aktivite_Yeri VARCHAR(50), Aktivite_Zamani VARCHAR(15) , Katilimci_Sayisi VARCHAR(55)")



                                                                                                                                                                                                                                    





















