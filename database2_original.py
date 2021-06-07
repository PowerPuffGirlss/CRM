from typing import Tuple
import mysql.connector
from csv import reader
def database_ac(isim):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql123"
    )
    mycursor=sql.cursor()  
    mycursor.execute(f"CREATE DATABASE {isim}")
    mycursor.execute("Show Databases")
    for x in mycursor:
        print(x)
    mycursor.close()
def database_tablo_olustur(database,isim,params=str):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql123",
        database=database
    )
    mycursor=sql.cursor()  
    mycursor.execute(F"CREATE TABLE {isim}({params})")
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x) 
def tablo_bilgi_ekle(database,tablo_isimi,eklemek_istedigin,bilgiler=Tuple):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql123",
        database=database
    )
    a="%s "
    d=a+", %s"*(len(eklemek_istedigin.split(","))-1)
    mycursor=sql.cursor()
    sq=f"INSERT INTO {tablo_isimi} ({eklemek_istedigin}) VALUES ({d})"
    mycursor.execute(sq,bilgiler)
    sql.commit()
    print(mycursor.rowcount)
def bilgi_toplama(database,tablo,csvdosyaismi):
    with open(csvdosyaismi,"r",encoding="utf8") as file:
        f=reader(file)
        g=0
        for p in f:
            if g==0:
                d=list(p)
            if g>0:       
                tablo_bilgi_ekle(database,tablo,", ".join(d),tuple(p))
            g+=1
     
        




def tablo_bilgileri_goster(database,tablo_isimi):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql123",
        database=database
    )
    mycursor=sql.cursor()
    liste=[]  
    mycursor.execute(f"SELECT * FROM {tablo_isimi}")
    deger=mycursor.fetchall()
    for x in deger:
        liste.append(x)
        print(x)
    return liste

def tablo_bilgi_sayi(database,tablo_isimi):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql123",
        database=database
    )
    mycursor=sql.cursor()
    deger=f"SELECT COUNT(*) FROM {tablo_isimi}" 
    result=mycursor.execute(deger) 
    result=mycursor.fetchone()
    print(f"bilgi sayi: {result[0]}")

#database_ac("CRM")
#database_tablo_olustur("CRM","Müşteri_Yönetimi","ID INT AUTO_INCREMENT PRIMARY KEY, ADI_SOYADI VARCHAR(45), Marka_Adı VARCHAR(45) ,Marka_Ekonomisi VARCHAR(45),Cinsiyet VARCHAR(45) ,Telefon_numarası INT  ")
#tablo_bilgi_ekle("CRM","Musteri","ID,Musteriisim,Musteriekonomisi,Cinsiyet,Mezundurumu",(111111,"Mustafa","Orta","E","Üniversite") )
#bilgi_toplama("CRM","Müşteri_Yönetimi","Müşteri_yönetimi.csv")
#tablo_bilgileri_goster("CRM","Müşteri_Yönetimi")
#tablo_bilgi_sayi("CRM","Müşteri_Yönetimi")
#15:00:00 16:00:00 09:00:00 10:00:00 11:00:00