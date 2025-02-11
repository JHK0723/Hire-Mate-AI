# HIREMATE-AI 🚀💼

**HIREMATE-AI** is an innovative web application designed to help job seekers by automatically generating job role and company suggestions from their resumes, fetching contact emails for those companies, and sending job application emails on their behalf! With the power of machine learning, web scraping, and automation, HIREMATE-AI streamlines the job application process like never before. 🤖✨

---

## 🚀 Features
- **Resume Parsing:** Extract text from uploaded resumes using PyPDF.
- **Job Role & Company Suggestions:** Get job role and company suggestions by parsing resume data with Llama3.
- **Email Fetching:** Scrape company emails using the Skrapp.io API for suggested companies.
- **Email Sending:** Send professional job application emails to companies using SMTP (Gmail).
- **SQLite Database:** Manage and store employee details like email addresses and job information.

---

## 💻 Technologies Used
### Frontend:
- **HTML** - Structure of the pages
- **CSS** - Styling of the pages
- **JavaScript** - Client-side scripting

### Backend:
- **Python** - Core language
- **PyPDF** - Extract text from resumes
- **Llama3** - Parse resume data and suggest job roles/companies
- **Skrapp.io API** - Fetch emails of companies based on suggestions
- **smtplib** - Send emails using Gmail SMTP
- **SQLite** - Store employee data for easy access and management

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:
- **Python** (version 3.6 or higher)
- **Git** (for version control)

### Setup

#### 1️⃣ Clone the Repository:
```bash
git clone https://github.com/yourusername/HIREMATE-AI.git
cd HIREMATE-AI
```
####2️⃣ Create a Virtual Environment:
In the backend folder:

```bash
python -m venv venv
```
#### 3️⃣ Install Dependencies:
Activate the virtual environment and install all required dependencies:

```bash

# For Windows
venv\Scripts\activate

# For macOS/Linux
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```
## ⚡ How It Works
### 1.User Uploads Resume:

#### The user uploads a resume via the frontend (HTML form).
#### The backend uses PyPDF to extract the text from the uploaded PDF.
### 2.Text Parsing:

#### The extracted text is parsed using Llama3 to suggest relevant job roles and companies.
### 3.Company Email Fetching:

#### The backend uses Skrapp.io API to fetch contact emails for the suggested companies.
### 4.Email Sending:

#### The backend uses smtplib to send professional job application emails to the fetched emails.

## 🛠️ Dependencies
### Here’s a list of some key dependencies you’ll need to install in your virtual environment:

#### FastAPI - Web framework for building APIs.
#### Uvicorn - ASGI server for running FastAPI.
#### PyPDF2 - PDF parsing library.
#### Llama3 - NLP model for text parsing.
#### Skrapp.io - API for fetching company emails.
#### smtplib - SMTP for sending emails.
#### sqlite3 - Database for storing employee data.

### Install them via:
```bash
pip install -r requirements.txt
```
### 📧 Email Setup
#### To send emails through Gmail using smtplib, you'll need to:

#### Enable Less Secure Apps on your Gmail account (if using a standard Gmail account).
#### Use your Gmail account credentials or create an App Password if you have 2-factor authentication enabled.


### 🛠️ Run Locally
#### 1. Run the FastAPI backend server with the following command:
```bash
cd backend
uvicorn app:app --reload --port 8080
```
#### This will start the backend server at http://127.0.0.1:8080.

#### 2.Open the frontend folder and open the index.html file in your browser. The frontend will interact with the backend via API calls.

### 🌟 Acknowledgments
#### Thanks to Skrapp.io for their email fetching API.
#### Big shoutout to FastAPI for making API development fast and easy.
#### Thanks to PyPDF2 for PDF text extraction.

## We hope you enjoy using HIREMATE-AI! Feel free to open an issue if you find any bugs or have suggestions! 🚀
