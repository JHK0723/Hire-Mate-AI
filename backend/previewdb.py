from tabulate import tabulate
def view_data():
    import sqlite3

    # Connect to your database
    conn = sqlite3.connect("./data.db")  # Ensure this path is correct
    cursor = conn.cursor()
    finalstr = f"ID\tCompany\t\t\t\t\tJob Role\t\t\t\t\tEmail\n"
    # Fetch all records from the employees table
    cursor.execute("SELECT * FROM employees;")
    rows = cursor.fetchall()
    conn.close()

    # Define headers
    headers = ["ID", "Company", "Job Role", "Email"]

    # Generate the table
    finalstr = tabulate(rows, headers=headers, tablefmt="grid")  # Other styles: "plain", "pipe", "fancy_grid"

    return finalstr
    