import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient

load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

# Check Google Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("❌ Google Gemini API Key not found! Check your .env file.")

# Initialize Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("❌ MongoDB URI not found! Check your .env file.")

try:
    mongo_client = MongoClient(MONGO_URI)
    db = mongo_client["voice_assistant_db"]
    collection = db["interactions"]
    logger.info("✅ Connected to MongoDB successfully!")
except Exception as e:
    logger.error(f"❌ MongoDB Connection Error: {e}")
    raise RuntimeError("MongoDB Connection Failed")

# FastAPI setup 
app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/process-text/")
async def process_text(request: TextRequest):
    user_text = request.text
    try:
        response = model.generate_content(user_text)
        ai_response = response.text if response.text else "Sorry, I couldn't generate a response."

        # Store the conversation in MongoDB
        collection.insert_one({"user_text": user_text, "ai_response": ai_response})

        return {"response": ai_response}

    except Exception as e:
        logger.error(f"Gemini API Error: {e}")
        raise HTTPException(status_code=500, detail=f"Gemini API Error: {str(e)}")

@app.get("/")
async def read_root():
    return {"message": "AI Voice Assistant API is running with Gemini AI"}

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
