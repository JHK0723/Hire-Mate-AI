import smtplib
from email.message import EmailMessage
import sqlite3
import ollama

def sendmail():
    # Connect to the database
    conn = sqlite3.connect("backend/data.db")  # Ensure correct path
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM employees;")  
    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        id= row[0] 
        company = row[1]  
        job_role = row[2]        
        mail_id = row[3]  
        print(f"Sending email to {mail_id} for {job_role} at {company}")


        prompt = f"Generate Mail body for {company} for the role of {job_role}"

        response_llama = ollama.generate(model="llama2", prompt=prompt)
        email_body = response_llama.get("response", "").strip()

        if not email_body:
            print(f"Failed to generate email body for {mail_id}")
            continue  # Skip sending email if no response
        
        email = EmailMessage()
        email.set_content(email_body)
        email['subject'] = f"Job Application for {job_role} at {company}"
        email['to'] = mail_id
        email['from'] = 'abc.gmail.com'

        pdf_path = "./uploads/resume.pdf" 

        with open(pdf_path, "rb") as pdf_file:
            email.add_attachment(
                pdf_file.read(),
                maintype="application",
                subtype="pdf",
                filename="resume.pdf"  # Name shown in email
            )

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.ehlo()
                smtp.login("thebruzz0000@gmail.com", "rblp vxrt lauq psct")
                response = smtp.send_message(email)
                print(f"📩 Email sent successfully to {mail_id}, SMTP Response: {response}")

        except smtplib.SMTPRecipientsRefused as e:
            print(f"❌ Recipient refused: {e}")
        except smtplib.SMTPAuthenticationError as e:
            print(f"❌ SMTP Authentication Error: {e}")
        except smtplib.SMTPException as e:
            print(f"❌ SMTP Exception: {e}")
        except Exception as e:
            print(f"❌ Unknown Error: {e}")


