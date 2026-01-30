import sqlite3

connection = sqlite3.connect("university.db")
cursor = connection.cursor()

query = "SELECT * FROM students"
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
