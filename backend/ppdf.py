import re
import ollama
import time
import ast  # Safer than eval()
from pypdf import PdfReader
from mails import get_company_emails


def extract_roles_and_companies(text):
    print("Extracting data from resume...")
    """Extracts a dictionary with companies as keys and job roles as values using LLaMA 3, strictly based on the resume."""

    prompt = f"""
You are given the following **resume text**:

{text}

### TASK:
Extract **EXACTLY 20** real-world companies (or fewer if not available) based on the skills of the user's resume and assign **one relevant job role** to each, based strictly on the resume content.
THE COMPANIES GENERATED CAN BE ANYTHING RELATED TO THE DOMAIN OF THE RESUME.
Example:- If the resume is of technical, the companies can be Google, Microsoft, etc.
### **STRICT RULES:**
- **ONLY return a valid Python dictionary (nothing else).**
- **Each company must be explicitly mentioned in the resume.** (DO NOT make up company names.)
- **Companies must be well-known, real, currently active businesses.**  
- **companies must not be names of industries or common technologies only companies like google,microsoft..., it should follow the above rule.**
- **DO NOT include:**  
  - Universities or academic institutions (e.g., "University of Toronto")  
  - Software tools, programming languages, or technologies (e.g., "Python", "TensorFlow", "Microsoft Office", "C++", "Java", "Visual Basic")  
  - Generic industry terms (e.g., "Engineering Firm", "Technical Systems Company", "Software Company")  
  - Job platforms (e.g., "LinkedIn", "Indeed")  
- **Job roles must match the resume experience.** (DO NOT make up random job titles.)  
- **EXCLUDE student roles.** (e.g., "Intern", "Teaching Assistant", "Research Assistant", "Student Software Engineer")  
- **A single company can have multiple job roles.**
- **If fewer than 20 companies exist, return only those found.** (DO NOT invent extra companies.)
- **STRICT OUTPUT FORMAT:**  
  - **Return ONLY a valid Python dictionary.** No explanations, no extra text, no markdown formatting.
  - The dictionary must use **double quotes** for both keys and values.
  - Each company must be a key, and its associated job role must be a **list of job titles**.
  - Example format (strictly follow this structure):

```python
{{
    "Google": ["Software Engineer", "AI Researcher"],
    "Microsoft": ["Data Scientist"],
    "Amazon": ["Cloud Solutions Architect", "Security Engineer"],
    "IBM": ["Machine Learning Engineer"],
    ...
}}
"""
    print("Generating response from Ollama...")
    
    try:
        response_llama = ollama.generate(model="llama3", prompt=prompt)
        extracted_data = response_llama["response"].strip()
    except Exception as e:
        return f"Error generating response from Ollama: {str(e)}"

    return extracted_data

def extract_data_from_pdf():
    """Reads text from a PDF, sends it to LLaMA 3 for processing, and extracts a dictionary with companies as keys and job roles as values."""

    PDF_PATH = r"./uploads/resume.pdf"
    # Extract text from PDF
    try:
        reader = PdfReader(PDF_PATH)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    except FileNotFoundError:
        return "Error: PDF file not found!"
    

    # Get extracted data from LLaMA 3
    extracted_data = extract_roles_and_companies(text)

    # Ensure LLaMA 3 followed the expected format
    pattern = r'\{(.*?)\}'  # Extracts dictionary content inside { }
    match = re.search(pattern, extracted_data, re.DOTALL)

    if match:
        extracted_dict_str = "{" + match.group(1) + "}"
        try:
            extracted_dict = ast.literal_eval(extracted_dict_str)  # Safer than eval()
            if not isinstance(extracted_dict, dict):
                extracted_dict = {}  # Fallback if parsing fails
        except:
            extracted_dict = {}  # Fallback to empty dictionary if parsing fails
    else:
        extracted_dict = {}



    # mails(extracted_dict)
    # print(extracted_dict)
    print(f"Successfully extracted data from PDF: {extracted_dict}")
    get_company_emails(extracted_dict)