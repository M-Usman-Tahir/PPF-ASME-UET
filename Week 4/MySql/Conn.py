import mysql.connector as MSC

mydb = MSC.connect(
  host="localhost",
  user="root",
  password="",
  database='store'
)