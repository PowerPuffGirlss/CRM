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

# database_ac("school")
# database_tablo_olusdur("school","class","id INT AUTO_INCREMENT PRIMARY KEY, sdtnumber VARCHAR(5) , name VARCHAR(255), surname VARCHAR(255) , birthdate DATETIME , gender CHAR(1)")
# tablo_bilgi_ekle(
#     "school",
#     "class",
#     " sdtnumber , name , surname , birthdate , gender",
#     ("34567","deniz","nazari",datetime.datetime(2003,4,7),'F')
# )
def bilgi_toplama(csvdosyaismi):
    with open(csvdosyaismi,"r") as file:
        f=reader(file)
        g=0
        for p in f:
            print(tuple(p))
            if g>0:
                tablo_bilgi_ekle("school","class"," sdtnumber , name , surname , birthdate , gender",tuple(p))
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
tablo_bilgileri_gosder("school","class")
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
tablo_bilgi_sayi("school","class")
class tablo_islemleri:
    def __init__(self,database,tablo_isimi):
        sql=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ana2almaal#",
        database=database)
        self.mycursor=sql.cursor()
        self.tablo=tablo_isimi
    @property
    def count(self):
        mycursor=self.mycursor
        deger=f"SELECT COUNT(*) FROM {self.tablo}"
        result=mycursor.execute(deger)
        result=mycursor.fetchone()
        print(f"bilgi sayi: {result[0]}")

tablo_islemleri.count()

