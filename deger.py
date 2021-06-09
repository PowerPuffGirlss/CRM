from sys import setprofile
import mysql.connector,datetime
from csv import reader

from mysql.connector import cursor
def database_ac(isim):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ana2almaal#"
    )
    mycursor=sql.cursor()  
    mycursor.execute(f"CREATE DATABASE {isim}")
    mycursor.execute("Show Databases")
    for x in mycursor:
        print(x)
    mycursor.close()








def database_tablo_olusdur(database,isim,params=str):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ana2almaal#",
        database=database
    )
    mycursor=sql.cursor()  
    mycursor.execute(F"CREATE TABLE {isim}({params})")
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x) 







def tablo_bilgi_ekle(database,tablo_isimi,eklemek_istedigin,liste):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ana2almaal#",
        database=database
    )
    a="%s "
    d=a+", %s"*(len(eklemek_istedigin.split(","))-1)
    mycursor=sql.cursor()
    sq=f"INSERT INTO {tablo_isimi} ({eklemek_istedigin}) VALUES ({d})"
    mycursor.execute(sq,liste)
    sql.commit()
    print(mycursor.rowcount)
def bilgi_toplama(database,tablo,csvdosyaismi):
    with open(csvdosyaismi,"r") as file:
        f=reader(file)
        g=0
        for p in f:
            if g==0:
                d=list(p)
            if g>0:
                # print(",".join(d))
                tablo_bilgi_ekle(database,tablo,", ".join(d),tuple(p))
            g+=1





def tablo_bilgileri_gosder(database,tablo_isimi):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ana2almaal#",
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






# tablo_bilgileri_gosder("school","class")
def tablo_bilgi_sayi(database,tablo_isimi):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ana2almaal#",
        database=database
    )
    mycursor=sql.cursor()
    deger=f"SELECT COUNT(*) FROM {tablo_isimi}"
    result=mycursor.execute(deger)
    result=mycursor.fetchone()
    print(f"bilgi sayi: {result[0]}")






def tablo_bagla(database,ana_tablo,baglanan_tablo,neye_baglanacak_ana,neye_baglanacak_baglanan):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ana2almaal#",
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


def tablo_bilgi_cikar(database,tablo_isimi,silmek_istedigin,bilgiler):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql123",
        database=database
    )
    mycursor = sql.cursor()

    sql1 = f"DELETE FROM {tablo_isimi} WHERE {silmek_istedigin} = '{bilgiler}'"

    mycursor.execute(sql1)

    sql.commit()

    print(mycursor.rowcount, " kayıt silindi")


def gelir_modeli():
    a=0
    x=int(input("siparişinizin fiyatı:"))
    gelir=x*0.15+120
    print(gelir)

def bilgi_cek(database ,tablo ,ne_soru , spesifif_cekmek_isdedigin_bilgi="*"):
    sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ana2almaal#",
        database=database
    )
    mycursor=sql.cursor()
    result=mycursor.execute(f"SELECT {spesifif_cekmek_isdedigin_bilgi} FROM {tablo} WHERE {ne_soru} ")
    result=mycursor.fetchall()
    print(result)
    return result




# database_ac("yemek_sepeti")
# database_tablo_olusdur("yemek_sepeti",
# "Menu",
# "id INT AUTO_INCREMENT PRIMARY KEY,yemek_turu VARCHAR(25) , ek_olarak_ne VARCHAR(255),fiyat INT")
# database_tablo_olusdur("yemek_sepeti","KULANICI","id INT AUTO_INCREMENT PRIMARY KEY,ISIM_SOY VARCHAR(25) , ADRESS VARCHAR(255),BAKIYE INT")
# database_tablo_olusdur("yemek_sepeti","SEPET","id INT AUTO_INCREMENT PRIMARY KEY, KULANICI_id INT,yemek_LISDESI VARCHAR(25) , URUN_SAYI VARCHAR(255),DURUM INT,CALISAN_KURYEid INT")
# database_tablo_olusdur("yemek_sepeti","CALISAN_KURYE","id INT AUTO_INCREMENT PRIMARY KEY,isim_soy VARCHAR(25)")
# database_tablo_olusdur("yemek_sepeti","mutfak","id INT AUTO_INCREMENT PRIMARY KEY,SEPETid VARCHAR(25),durum VARCHAR(25)")

























# tablo_bagla("school","student","class","classId","id")


# tablo_bilgi_sayi("school","class")
# class tablo_islemleri:
#     def __init__(self,database,tablo_isimi):
#         sql=mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Ana2almaal#",
#         database=database)
#         self.mycursor=sql.cursor()
#         self.tablo=tablo_isimi
#     @property
#     def count(self):
#         mycursor=self.mycursor
#         deger=f"SELECT COUNT(*) FROM {self.tablo}"
#         result=mycursor.execute(deger)
#         result=mycursor.fetchone()
#         return result[0]

# tablo_islemleri.count
# database_ac("fonkim")



# bilgi_toplama("school","student","sinifdakicocuklar.csv")

# database_ac("school")
# database_tablo_olusdur("school","class","id INT AUTO_INCREMENT PRIMARY KEY, sdtnumber VARCHAR(5) , name VARCHAR(255), surname VARCHAR(255) , birthdate DATETIME , gender CHAR(1)")
# tablo_bilgi_ekle(
#     "school",
#     "class",
#     " sdtnumber , name , surname , birthdate , gender",
#     ("34567","deniz","nazari",datetime.datetime(2003,4,7),'F')
# )






#school database      tables:    student♥,teacher,class,lesson,classlesson

# database_tablo_olusdur("school","teacher","id INT AUTO_INCREMENT PRIMARY KEY, Branch VARCHAR(255) , name VARCHAR(255), surname VARCHAR(255) , birthdate DATETIME , gender CHAR(1)")
#database_tablo_olusdur("school","CLASSLESSON","id INT AUTO_INCREMENT PRIMARY KEY, classId VARCHAR(255) NOT NULL, lessonId VARCHAR(255) NOT NULL, teacherId VARCHAR(255) NOT NULL")
