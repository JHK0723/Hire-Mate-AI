import re
import ollama
import time
import ast  # Safer than eval()
from pypdf import PdfReader

PDF_PATH = r"C:\projects\Hire-Mate-AI\backend\resume-computer-engineering.pdf"

def extract_roles_and_companies(text):
    """Extracts a dictionary with companies as keys and job roles as values using LLaMA 3, strictly based on the resume."""
    
    prompt = f"""
    You are given the following resume text: 

    {text}

    Your task is to extract **EXACTLY 20** real companies/startups **mentioned in the resume** and assign **a relevant job role** to each one **based on the resume content**.

    **IMPORTANT RULES:** 
    - only major companies which are still active should be displayed
    - The companies must be **mentioned in the resume** (DO NOT make up company names). 
    - The job role for each company must be **relevant to what is written in the resume** (DO NOT invent roles that are not aligned with the candidate's experience).
    - If fewer than 20 companies are in the resume, use only those present and DO NOT add extra ones.
    - Format the output **STRICTLY as a Python dictionary** with 20 (or fewer) key-value pairs.  
    - **DO NOT** include extra explanations, notes, or text.
    - **DO NOT** include any student roles.
    - **Job Roles:** Must be common industry job roles, **not skills** or generic words.**  
    - **Companies:** Must be real-world, major companies (no universities, no software products).**

    **OUTPUT FORMAT EXAMPLE (FOLLOW THIS EXACTLY):**
    {{
        "Google": "Software Engineer",
        "Microsoft": "Data Scientist",
        "OpenAI": "AI Engineer",
        ...
    }}
    """

    try:
        response_llama = ollama.generate(model="llama3", prompt=prompt)
        extracted_data = response_llama["response"].strip()
    except Exception as e:
        return f"Error generating response from Ollama: {str(e)}"

    return extracted_data

def extract_data_from_pdf():
    """Reads text from a PDF, sends it to LLaMA 3 for processing, and extracts a dictionary with companies as keys and job roles as values."""
    
    start_time = time.time()

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

    end_time = time.time()
    print(f"⚡ Execution Time: {end_time - start_time:.2f} seconds")
    print(f"✅ Extracted Data ({len(extracted_dict)} key-value pairs): {extracted_dict}")

    return extracted_dict

# Run the script
extract_data_from_pdf()

