import database
# CRM DATABASE OLUSDUR
database.database_ac("CRM")
# katagoriler
# 1,ci  kontaktlar:    kontakt , listeler 
database.database_tablo_olusdur("CRM",
"kontakt",
"""id INT AUTO_INCREMENT PRIMARY KEY,
Kisi Adi  VARCHAR(50) ,
surname VARCHAR(255) ,
firma VARCHAR(255), 
 
birthdate DATETIME , 
gender CHAR(1)""")
#  2ci ajanda 

