# import requests

# API_KEY = "380774089YZYxobMC4wwJGwircJJaxICQg6BZEOx2Z"  # Replace with your Skrapp API key

# def get_data(data_dict):
#     data_dict = data_dict
import requests
def get_company_emails(company_names):
    
    print("i called this function")
    API_KEY = "380774089YZYxobMC4wwJGwircJJaxICQg6BZEOx2Z"  # Replace with your Skrapp API key
    
    mail_data = {
        "Email": [],
        "Job Role": [],
        "Company": []
    }
    
    
    for company, job_roles in company_names.items():
        url = f"https://api.skrapp.io/profile/search/email?companyName={company}&size=1"
        headers = {
            "X-Access-Key": API_KEY,
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            
            if not results:
                print(f"No emails found for {company}.")
                continue  # Skip to the next company
            for result in results:
                email = result.get("email", "No email found")

                for job in job_roles:  # Assign all job roles for this company
                    mail_data["Email"].append(email)
                    mail_data["Job Role"].append(job)
                    mail_data["Company"].append(company)

        else:
            # return f"Error {response.status_code}: {response.text}"
            print(f"Error {response.status_code}: {response.text}")
    print(mail_data)

# Example usage
# company_names = ["microsoft"]  # Replace with any company name
# emails = get_company_emails(company_names)

# print("\n".join(emails) if isinstance(emails, list) else emails)
