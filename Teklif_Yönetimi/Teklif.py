import mysql.connector

mydb=mysql.connector.connect(
    host="localhost", 

    user="root", 

    password="08Ozge34"
)
print(mydb)

mycursor=mydb.cursor()

mycursor.execute("Create Table customers (name Varchar(255),adress varchar(255))")