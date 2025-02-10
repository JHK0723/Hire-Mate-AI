import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS dbase(S.No INTEGER PRIMARY KEY, Company TEXT, Email TEXT)"""

cursor.execute(command1)

cursor.execute(f"INSERT INTO dbase VALUES({i},")