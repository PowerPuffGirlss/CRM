import database

database.database_ac("csv")

# stok mallar , markalar , urun turu , urun 
#  satış temsilcileri , musteri, Teklifleriniz

database.database_tablo_olusdur("csv",
"urunler",
"""id INT AUTO_INCREMENT PRIMARY KEY, urun_kod  INT  NOT NULL , urun_adi VARCHAR(55)  NOT NULL , Marka_Kategori VARCHAR(55) NOT NULL , urun_fiyat INT NOT NULL , stok_miktari VARCHAR(55) NOT NULL , Durum VARCHAR(300)""")

database.database_tablo_olusdur("csv",
"satislar",
"""id INT AUTO_INCREMENT PRIMARY KEY, satis_adi  VARCHAR(15)  NOT NULL ,satis_tarihi DATETIME NOT NULL , satis_yapan VARCHAR(55), kontakt VARCHAR(55), fiyat INT  NOT NULL , odeme_durumu  VARCHAR(300), karlilik VARCHAR(55), islem VARCHAR(300)""")

database.database_tablo_olusdur("csv",
"sirketler","""id INT AUTO_INCREMENT PRIMARY KEY, sirket_adi  VARCHAR(15) NOT NULL , failiyet_yili DATETIME NOT NULL  ,danisman VARCHAR(55),kontakt VARCHAR(55), iliskidurumu VARCHAR(55), hakinda VARCHAR(300)""")










                                                                                                                                                                                                                                    






















# database.database_ac("Stok Yönetimi")
# database.database_ac("Satış Yönetimi")
# database.database_ac("Ürün Yönetimi")





