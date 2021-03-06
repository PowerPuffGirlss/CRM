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
#database_tablo_olustur("CRM","Hat??rlat??c??_Mesajlar","ID INT AUTO_INCREMENT PRIMARY KEY, Baslik VARCHAR(45),??lgili_Kontaklar  VARCHAR(45) ,??lgili_Kullan??c??lar VARCHAR(45),Ba??lang????_Saati_ve_Tarihi DATETIME ,Hat??rlatma_Tarihi DATETIME,??nem_Derecesi VARCHAR(45),Durumu VARCHAR(165),Sonu?? VARCHAR(165),Hat??rlat??c??_mesajlar VARCHAR(165)")
#tablo_bilgi_ekle("CRM","Hat??rlat??c??_Mesajlar","ID,Musteriisim,Musteriekonomisi,Cinsiyet,Mezundurumu",(111111,"Mustafa","Orta","E","??niversite") )
#bilgi_toplama("CRM","Hat??rlat??c??_Mesajlar","Hat??rlat??c??_mesaj.csv")
#tablo_bilgileri_goster("CRM","Hat??rlat??c??_Mesajlar")
#tablo_bilgi_sayi("CRM","Hat??rlat??c??_Mesajlar")
