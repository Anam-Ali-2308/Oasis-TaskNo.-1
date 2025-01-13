import speech_recognition as sr
import pyttsx3
import requests
from datetime import datetime
import smtplib

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return None

def get_weather(city):
    api_key = "your_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"]
        description = response["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {description}."
    else:
        return "City not found."

def send_email(to, subject, message):
    sender = "your_mail@gmail.com"
    password = "your_password"
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        email = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender, to, email)
    speak("Email has been sent.")

def main():
    speak("Hello! I am your advanced voice assistant.")
    while True:
        command = listen()
        if command:
            if "hello" in command:
                speak("Hello! How can I help you today?")
            elif "time" in command:
                speak(f"The current time is {datetime.now().strftime('%I:%M %p')}")
            elif "date" in command:
                speak(f"Today's date is {datetime.now().strftime('%B %d, %Y')}")
            elif "weather" in command:
                speak("Which city's weather would you like to know?")
                city = listen()
                if city:
                    weather = get_weather(city)
                    speak(weather)
            elif "email" in command:
                speak("Who is the recipient?")
                recipient = listen()
                speak("What is the subject?")
                subject = listen()
                speak("What is the message?")
                message = listen()
                if recipient and subject and message:
                    send_email(recipient, subject, message)
            elif "exit" in command:
                speak("Goodbye!")
                break

if __name__ == "__main__":
    main()
