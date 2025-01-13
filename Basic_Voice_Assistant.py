import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

# Initialize the text-to-speech engine
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
            speak("Sorry, I couldn't understand that.")
            return None

def main():
    speak("Hello! How can I assist you?")
    while True:
        command = listen()
        if command:
            if "hello" in command:
                speak("Hi there!")
            elif "time" in command:
                speak(f"The time is {datetime.now().strftime('%I:%M %p')}")
            elif "date" in command:
                speak(f"Today's date is {datetime.now().strftime('%B %d, %Y')}")
            elif "search" in command:
                speak("What would you like to search for?")
                query = listen()
                if query:
                    webbrowser.open(f"https://www.google.com/search?q={query}")
                    speak(f"Here are the results for {query}.")
            elif "exit" in command:
                speak("Goodbye!")
                break

if __name__ == "__main__":
    main()
