import sqlite3

# Connect to your database
conn = sqlite3.connect("./data.db")  # Ensure this path is correct
cursor = conn.cursor()

# Fetch all records from the employees table
cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

conn.close()
