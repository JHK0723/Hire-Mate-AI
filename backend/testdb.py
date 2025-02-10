import sqlite3

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

cursor.execute("INSERT INTO employees (Company, Job_Role, Email) VALUES ('Microsoft', 'Software Engineer', 'sambarlasagna@gmail.com')")
cursor.execute("INSERT INTO employees (Company, Job_Role, Email) VALUES ('Microsoft', 'Software Engineer', 'aadhityaayyappan06@gmail.com')")
cursor.execute("INSERT INTO employees (Company, Job_Role, Email) VALUES ('Microsoft', 'Software Engineer', 'jhk.300506@gmail.com')")
cursor.execute("INSERT INTO employees (Company, Job_Role, Email) VALUES ('Microsoft', 'Software Engineer', 'sulaimanibrahimucps@gmail.com')")

cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

conn.close()