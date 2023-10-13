# C z crud (DDL - Data Definition Language) = CREATE TABLE
import sqlite3

connection = sqlite3.connect("mydatabase.db")

cursor = connection.cursor()

stmt = """
CREATE TABLE IF NOT EXISTS person(
    id INT PRMIARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(128),
    age INT
)
"""

cursor.execute(stmt)
connection.close()
