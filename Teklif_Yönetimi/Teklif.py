import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1" ,

    user="root", 

    password="08Ozge34",

    auth_plugin="mysql_native_password"

)

mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE Teklif ")

mycursor.execute("Create Table customers (name Varchar(255),adress varchar(255))")