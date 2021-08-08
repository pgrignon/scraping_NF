import mysql.connector  # type: ignore

mydb = mysql.connector.connect(host="localhost", user="paul", password="motdepasse")

print(mydb)
