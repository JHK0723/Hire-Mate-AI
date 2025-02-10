import smtplib
from email.message import EmailMessage
import sqlite3

email = EmailMessage()
# Connect to the database
conn = sqlite3.connect("backend/data.db")  # Ensure correct path
cursor = conn.cursor()


cursor.execute("SELECT Email FROM employees;")  
emails = [row[0] for row in cursor.fetchall()]

conn.close()

for email in emails:

    email['from'] = 'ichinisan11092006@gmail.com'
    email['to'] = f'{email}'
    email['subject'] = 'Congrats for VIT'
    email.set_content('Im anonymous chuchu')
    try:
        with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('ichinisan11092006@gmail.com', 'xxx')
            smtp.send_message(email)
            print("all good")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")