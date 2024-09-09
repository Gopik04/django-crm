import mysql.connector
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Gopi007@"
)

#prepare a cursor object
cursorObject=dataBase.cursor()

#create database
cursorObject.execute('CREATE DATABASE elderco')
print('all done')