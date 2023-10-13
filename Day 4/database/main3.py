# R z CRUD (DML - Data Modification Language, aka DQL - Data Query Language) = SELECT
import sqlite3

connection = sqlite3.connect("mydatabase.db")

cursor = connection.cursor()

stmt = """
    SELECT * FROM person;
"""
cursor.execute(stmt)

rows = cursor.fetchall()
print(rows)

# commit nie, bo operacja bezpieczna
# connection.commit()

connection.close()
