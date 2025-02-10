from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
# from olamAI import mail_body
import uvicorn
import shutil
import os
from ppdf import extract_data_from_pdf

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

# @app.get("/")
# def get_message():
#     return {"message1": mail_body()}  # Returns JSON response

print("Hi")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
RESUME_PATH = os.path.join(UPLOAD_FOLDER, "resume.pdf")

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open(RESUME_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    print(f"File {file.filename} uploaded successfully to {RESUME_PATH}")  # Debugging
    return {"filename": file.filename, "status": "File uploaded successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

