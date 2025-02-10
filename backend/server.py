from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from olamAI import mail_body
import uvicorn

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

@app.get("/")
def get_message():
    return {"message1": mail_body()}  # Returns JSON response

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

