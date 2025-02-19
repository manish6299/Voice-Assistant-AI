import speech_recognition as sr
import pyttsx3
import requests

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return None
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        return None

def text_to_speech(response_text):
    engine = pyttsx3.init()
    engine.say(response_text)
    engine.runAndWait()

def send_text_to_api(text):
    url = "http://127.0.0.1:8000/process-text/"  
    try:
        response = requests.post(url, json={"text": text})
        if response.status_code == 200:
            return response.json().get("response", "I couldn't process that.")
        else:
            return "Error connecting to AI API."
    except requests.exceptions.RequestException as e:
        return f"API request failed: {e}"

if __name__ == "__main__":
    while True:
        user_input = recognize_speech()
        if user_input:
            ai_response = send_text_to_api(user_input)
            print(f"AI Assistant: {ai_response}")
            text_to_speech(ai_response)
        
        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != "yes":
            print("Goodbye!")
            break
