import sqlite3
import pandas as pd
import os
import subprocess

def append_data(full_data):
    if not full_data:
        print("No data to append.")
        return
    df = pd.DataFrame(full_data)
    conn = sqlite3.connect("./data.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS employees")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Company TEXT,
            Job_Role TEXT,
            Email TEXT
        )
    """)

    # Insert data into SQLite
    df.to_sql("employees", conn, if_exists="append", index=False)

    # Commit & close
    subprocess.run(["python", "viewdb.py"])

    conn.commit()
    conn.close()

# import sqlite3
# from mails import get_company_emails

# table_data = get_company_emails()
# connection = sqlite3.connect('data.db')

# cursor = connection.cursor()

# command1 = """CREATE TABLE IF NOT EXISTS dbase(S.No INTEGER PRIMARY KEY, Company TEXT, Email TEXT)"""

# cursor.execute(command1)
# for i,row in enumerate(table_data):
#     cursor.execute(f"INSERT INTO dbase VALUES({i}, '{row['name'][i]}', '{table_data[column]}')")
# cursor.execute(f"INSERT INTO dbase VALUES({i},")