import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="paul",
  password="motdepasse"
)

print(mydb)