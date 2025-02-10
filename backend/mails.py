import requests

API_KEY = "380774089YZYxobMC4wwJGwircJJaxICQg6BZEOx2Z"  # Replace with your Skrapp API key
def get_company_emails(company_names, size=1):

    """Fetch professional emails from a company using Skrapp API"""
    mail_data = {}
    mail_data['Email'] = []
    mail_data['Name'] = []
    mail_data['Company'] = []
    for name in company_names:
        url = f"https://api.skrapp.io/profile/search/email?companyName={name}&size={size}"
        headers = {
            "X-Access-Key": API_KEY,
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            
            if not results:
                return f"No emails found for {name}."

            mail_data['Email']= [emp.get('email', 'None') for emp in results]
            mail_data['Name']= [emp.get('name', 'None') for emp in results]
            mail_data['Company'].append(name)

        else:
            return f"Error {response.status_code}: {response.text}"
    return mail_data

# Example usage
company_names = ["microsoft"]  # Replace with any company name
emails = get_company_emails(company_names)

print("\n".join(emails) if isinstance(emails, list) else emails)
