import mysql.connector

mydb=mysql.connector.connect(
    host="localhost", 

    user="root", 

    password="08Ozge34", 

    auth_plugin ="mysql_native_password"
)
mydb.close()
print(mydb)