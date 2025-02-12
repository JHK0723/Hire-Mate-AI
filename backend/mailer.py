import smtplib
from email.message import EmailMessage
import sqlite3
import ollama
import time

def sendmail(sample=0):
    # Connect to the database
    print("🚀 Sending mails...")
    conn = sqlite3.connect("./data.db")  # Ensure correct path
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees;")  
    rows = cursor.fetchall()
    conn.close() 

    total_mails = len(rows)
    sent_mails = 0

    for row in rows:
        id = row[0] 
        company = row[1]  
        job_role = row[2]        
        mail_id = row[3] 
        
        if mail_id.lower() == "no email found" or not mail_id.strip():
            print(f"⚠️ Skipping {id} as there is no valid email.")
            continue

        print(f"📝 Generating mail body for {mail_id}, {job_role} at {company}")

        prompt = (
            f"Write a professional job application email for the role of {job_role} at {company}. "
            "Address the recipient as 'Dear Hiring Manager' if their name is unknown. "
            "The email should express enthusiasm for the role, highlight relevant skills and experience, "
            "and end with a polite call to action. DO NOT include any closing phrases like 'Yours sincerely', "
            "'Best regards', or a placeholder for the sender's name. The email must conclude naturally after the final paragraph."
        )

        response_llama = ollama.generate(model="llama2", prompt=prompt)
        email_body = response_llama.get("response", "").strip()

        if not email_body:
            print(f"❌ Failed to generate email body for {mail_id}")
            continue  # Skip sending email if no response

        print(f"📩 Sending email to {mail_id} for {job_role} at {company}")
        
        email = EmailMessage()
        email.set_content(email_body)
        email['subject'] = f"Job Application for {job_role} at {company}"
        email['to'] = mail_id
        email['from'] = 'Enter email here'

        pdf_path = "./uploads/resume.pdf"

        with open(pdf_path, "rb") as pdf_file:
            email.add_attachment(
                pdf_file.read(),
                maintype="application",
                subtype="pdf",
                filename="resume.pdf"
            )

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.ehlo()
                smtp.login("Enter email here", "Enter app password here")
                response = smtp.send_message(email)
                print(f"✅ Email sent successfully to {mail_id} 🚀")
                sent_mails += 1

        except smtplib.SMTPRecipientsRefused as e:
            print(f"❌ Recipient refused: {e}")
        except smtplib.SMTPAuthenticationError as e:
            print(f"❌ SMTP Authentication Error: {e}")
        except smtplib.SMTPException as e:
            print(f"❌ SMTP Exception: {e}")
        except Exception as e:
            print(f"❌ Unknown Error: {e}")

        time.sleep(1)  # Small delay to avoid spam detection

    if sent_mails == total_mails:
        print("\n🎉🎉🎉 ALL EMAILS SENT SUCCESSFULLY! 🎉🎉🎉")
        print("🚀🔥 You have successfully sent all emails without any issues! 💪")
    elif sent_mails > 0:
        print(f"\n✅ {sent_mails}/{total_mails} Emails Sent Successfully! ⚡🚀")
    else:
        print("\n❌ No emails were sent. Please check for issues! 😢")

