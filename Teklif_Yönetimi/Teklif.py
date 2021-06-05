import mysql.connector

mydb=mysql.connector.connect(
    host="localhost", 

    user="root", 

    password="08Ozge34"
)
mydb.close()
print(mydb)