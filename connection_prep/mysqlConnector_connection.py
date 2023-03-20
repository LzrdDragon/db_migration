import mysql.connector

connection = mysql.connector.connect(
    user='',
    password='',
    host='127.0.0.1',
    database='crypto_wp'
)
print(connection.database)
connection.close()
