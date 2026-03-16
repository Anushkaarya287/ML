import sqlite3
import csv

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS quotes(
quote TEXT,
author TEXT
)
""")

with open("quotes.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        cursor.execute("INSERT INTO quotes VALUES (?,?)", row)

conn.commit()

cursor.execute("SELECT * FROM quotes")

for row in cursor.fetchall():
    print(row)

conn.close()