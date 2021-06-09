import mysql.connector,datetime
from csv import reader

def database_ac(password,isim):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password=password
    )
    mycursor=sql.cursor()  
    mycursor.execute(f"CREATE DATABASE {isim}")
    mycursor.execute("Show Databases")
    for x in mycursor:
        print(x)
    mycursor.close()



def database_tablo_olusdur(password,database,isim,params=str):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database=database
    )
    mycursor=sql.cursor()  
    mycursor.execute(F"CREATE TABLE {isim}({params})")
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x) 



def tablo_bilgi_ekle(password,database,tablo_isimi,eklemek_istedigin,liste):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database=database
    )
    a="%s "
    d=a+", %s"*(len(eklemek_istedigin.split(","))-1)
    mycursor=sql.cursor()
    mycursor.execute(f"INSERT INTO {tablo_isimi} ({eklemek_istedigin}) VALUES ({d})",liste)
    sql.commit()
    print(mycursor.rowcount)



def bilgi_toplama(password,database,tablo,csvdosyaismi):
    with open(csvdosyaismi,"r") as file:
        f=reader(file)
        g=0
        for p in f:
            if g==0:
                d=list(p)
            if g>0:
                tablo_bilgi_ekle(password,database,tablo,", ".join(d),tuple(p))
            g+=1



def tablo_bilgileri_gosder(password,database,tablo_isimi):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database=database
    )
    mycursor=sql.cursor()
    lisde=[]  
    mycursor.execute(f"SELECT * FROM {tablo_isimi}")
    deger=mycursor.fetchall()
    for x in deger:
        lisde.append(x)
        print(x)
    return lisde



def tablo_bilgi_sayi(password,database,tablo_isimi):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database=database
    )
    mycursor=sql.cursor()
    deger=f"SELECT COUNT(*) FROM {tablo_isimi}"
    result=mycursor.execute(deger)
    result=mycursor.fetchone()
    print(f"bilgi sayi: {result[0]}")



def tablo_bagla(password,database,ana_tablo,baglanan_tablo,neye_baglanacak_ana,neye_baglanacak_baglanan):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database=database
    )
    mycursor=sql.cursor()
    sq=f"SELECT *FROM {ana_tablo} as x inner join {baglanan_tablo} as y on x.{neye_baglanacak_ana}=y.{neye_baglanacak_baglanan} "
    mycursor.execute(sq)
    try: 
        result=mycursor.fetchall()
        for a in result:
            print(a)
    except mysql.connector.Error as err:
        print("hata "+err)



#database_ac("08Ozge34","crm")

#database_tablo_olusdur("08Ozge34","crm","Teklif_Yönetimi","id INT AUTO_INCREMENT PRIMARY KEY, Teklif_Adi VARCHAR(15) , Teklif_Tarihi VARCHAR(15), Kontak VARCHAR(15) , Fiyat VARCHAR(15) , Karlilik_Bilgileri VARCHAR(15),  islem VARCHAR(15) ")
#bilgi_toplama("08Ozge34","crm","Teklif_Yönetimi","Crm_Sistemi/Teklif_Yönetim.csv")

#database_tablo_olusdur("08Ozge34","crm","Teklif_Raporları","id INT AUTO_INCREMENT PRIMARY KEY, Teklif_Adi VARCHAR(15) , Baslangic_Tarihi VARCHAR(15), Kontak VARCHAR(15) , Teklif_Yapan VARCHAR(15) , Durum VARCHAR(15),  Tutar VARCHAR(15) ")
#bilgi_toplama("08Ozge34","crm","Teklif_Raporları","Crm_Sistemi/Teklif_Rapor.csv")

#database_tablo_olusdur("08Ozge34","crm","Satış_Raporları","id INT AUTO_INCREMENT PRIMARY KEY, Satis_Adi VARCHAR(15) , Satis_Tarihi VARCHAR(15), Kontak VARCHAR(15) , Satis_Yapan VARCHAR(15) , Durum VARCHAR(15),  Tutar VARCHAR(15),  Kalan_Tutar VARCHAR(15) ")
#bilgi_toplama("08Ozge34","crm","Satış_Raporları","Crm_Sistemi/Satıs_Rapor.csv")

#database_tablo_olusdur("08Ozge34","crm","Tahsilat_Raporları","id INT AUTO_INCREMENT PRIMARY KEY, Satis_Adi VARCHAR(15) , Kontak VARCHAR(50), Tutar VARCHAR(15) , Zaman VARCHAR(15) , Odeme_Durumu VARCHAR(15),  Odeme_Tipi VARCHAR(15),  Tahsilat_Durumu VARCHAR(15) ")
#bilgi_toplama("08Ozge34","crm","Tahsilat_Raporları","Crm_Sistemi/Tahsilat_Rapor.csv")

#database_tablo_olusdur("08Ozge34","crm","Görev_Raporları","id INT AUTO_INCREMENT PRIMARY KEY, Baslik VARCHAR(55) , ilgili_Kontaklar VARCHAR(50), ilgili_Kullanicilar VARCHAR(15) , Baslangic_Tarihi VARCHAR(55) , Tip VARCHAR(55),  Durum VARCHAR(55),  Onem_Derecesi VARCHAR(55),  Hatirlatma VARCHAR(55) ")
#bilgi_toplama("08Ozge34","crm","Görev_Raporları","Crm_Sistemi/Görev_Rapor.csv")

#database_tablo_olusdur("08Ozge34","crm","Hedef_Raporları","id INT AUTO_INCREMENT PRIMARY KEY, Kullanici VARCHAR(55) , Hedef_Tipi VARCHAR(50), Hedef VARCHAR(15) , Gerceklesen VARCHAR(55) , Gerceklesme_Yuzdesi VARCHAR(55),  Prim VARCHAR(55),  Prim_Tutari VARCHAR(55) ")
#bilgi_toplama("08Ozge34","crm","Hedef_Raporları","Crm_Sistemi/Hedef_Rapor.csv")

#database_tablo_olusdur("08Ozge34","crm","Aktivite_Yönetimi","id INT AUTO_INCREMENT PRIMARY KEY, Aktivite_Adi VARCHAR(55) , Aktivite_Yeri VARCHAR(50), Aktivite_Zamani VARCHAR(15) , Katilimci_Sayisi VARCHAR(55)")
