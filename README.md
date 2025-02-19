

### 🗣️ AI Voice Assistant API  

🚀 **AI Voice Assistant** is a FastAPI-based AI-powered chatbot that integrates with Gemini API for natural language processing. It also stores interactions in MongoDB for analysis and logging.  

---

## 📌 Features  
✅ Process text inputs using **Gemini API**  
✅ Store chat history in **MongoDB**  
✅ Built with **FastAPI** for high performance  
✅ Dockerized for easy deployment  

---

## 🏗️ Tech Stack  
- **FastAPI** - Backend API framework  
- **Google Gemini API** - AI model for text processing  
- **MongoDB** - Database for storing interactions  
- **Docker** - Containerization  
- **Uvicorn** - ASGI server  

---

## 🚀 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/manish6299/Voice-Assistant-AI.git
cd Voice-Assistant-AI
```

### 2️⃣ Set Up Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables  
Create a `.env` file in the root directory and add:  
```ini
OPENAI_API_KEY=your_gemini_api_key
MONGO_URI=your_mongo_connection_string
```

---

## 🚀 Running the Application  

### Run Locally  
```bash
uvicorn main:app --reload
```
> API will be available at **http://127.0.0.1:8000**  

### Run with Docker  
1. **Build Docker Image**  
   ```bash
   docker build -t voice-assistant-ai .
   ```
2. **Run the Container**  
   ```bash
   docker run -p 8000:8000 voice-assistant-ai
   ```

---

## 📡 Deployment on DockerHub  

### 1️⃣ Login to DockerHub  
```bash
docker login -u manish62
```

### 2️⃣ Tag & Push Image  
```bash
docker tag voice-assistant-ai manish62/voice-assistant-ai:latest
docker push manish62/voice-assistant-ai:latest
```

---

## 📍 API Endpoints  

### ✅ **Process Text**  
- **POST** `/process-text/`  
- **Request:**  
  ```json
  { "text": "Hello, how are you?" }
  ```
- **Response:**  
  ```json
  { "response": "I'm doing great! How can I help you?" }
  ```

### ✅ **Check API Status**  
- **GET** `/`  
- **Response:**  
  ```json
  { "message": "AI Voice Assistant API is running" }
  ```

---

## 🤝 Contributing  
Feel free to fork this repository and create pull requests. Contributions are welcome!  

