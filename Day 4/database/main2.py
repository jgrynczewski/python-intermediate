# C z CRUD (DML - Data Modification Language) = INSERT
import sqlite3

connection = sqlite3.connect("mydatabase.db")

cursor = connection.cursor()
name = 24

stmt = """
    INSERT INTO person VALUES
    (1, 'John', 'Doe', ?),
    (2, 'Jane', 'Doe', 54),
    (3, 'Jan', 'Kowalski', 40);
"""
cursor.execute(stmt, (24,))

connection.commit()
connection.close()
