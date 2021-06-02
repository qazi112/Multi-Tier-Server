import mysql.connector

def createConnection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database = "users" )

    print(mydb)
    return mydb
