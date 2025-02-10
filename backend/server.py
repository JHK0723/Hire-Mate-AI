from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
# from olamAI import mail_body
import uvicorn
import shutil
import os
from ppdf import extract_data_from_pdf
from mailer import sendmail
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

@app.get("/preview/")
def get_message():
    return {"message1": "This is the mail body"}  # Returns JSON response


print("Hello")
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

@app.post("/send-emails/")
async def send_emails(background_tasks: BackgroundTasks):
    background_tasks.add_task(sendmail)
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
#     uvicorn.run(app, host="127.0.0.1", port=8080)


