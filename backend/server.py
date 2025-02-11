from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
# from olamAI import mail_body
import uvicorn
import shutil
import os
from ppdf import extract_data_from_pdf
from mailer import sendmail
from previewdb import  view_data
app = FastAPI()
#hi

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins (for testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
RESUME_PATH = os.path.join(UPLOAD_FOLDER, "resume.pdf")

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    print("File receiving...")
    with open(RESUME_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print("File receieved in backend")
    extract_data_from_pdf()
    return {"filename": file.filename, "status": "File uploaded successfully"}

@app.get("/preview/")
def get_message(background_tasks: BackgroundTasks):
    return {"message1": """Subject: Application for Machine Learning Scientist Role at Amazon

Dear Hiring Manager,

I am excited to apply for the Machine Learning Scientist position at Amazon and contribute my skills and experience to your esteemed team. With a passion for machine learning and a proven track record of developing innovative solutions, I believe I would be an excellent fit for this role.

In my current position at XYZ Corporation, I have honed my skills in data analysis, algorithm development, and model deployment. I have also worked on several projects involving natural language processing, computer vision, and predictive modeling, which have helped me build a strong foundation in these areas. My experience working with large datasets and distributed computing environments has also prepared me well for the challenges of working at Amazon.

I am particularly drawn to Amazon's commitment to innovation and its focus on using machine learning to drive business outcomes. I believe that my skills and experience make me a strong candidate to help Amazon continue to push the boundaries of what is possible with machine learning.

If you would like to learn more about my qualifications or discuss how I can contribute to your team, please do not hesitate to contact me. Thank you for considering my application.""","message2":view_data()}  # Returns JSON response

@app.post("/send-emails/")
async def send_emails(background_tasks: BackgroundTasks):
    print("Sending emails...(fastapi)")
    background_tasks.add_task(sendmail())
    return {"message": "Email sending started in the background"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, reload=True)

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Hello World"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)


