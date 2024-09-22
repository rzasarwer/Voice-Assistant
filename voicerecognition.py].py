import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take a voice command from the user
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
        except Exception as e:
            print("Could not understand audio, please try again...")
            return "None"
        return command.lower()

# Function to respond to commands
def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in command:
        today = datetime.date.today()
        speak(f"Today's date is {today}")

    elif "search" in command:
        speak("What would you like to search for?")
        query = take_command()
        if query != "None":
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query} on Google.")

    elif "wikipedia" in command:
        speak("What topic would you like to know about?")
        query = take_command()
        if query != "None":
            speak("Searching Wikipedia...")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(result)
            except Exception as e:
                speak("Sorry, I couldn't find any information on that.")

    else:
        speak("Sorry, I didn't understand that command.")

# Main loop to keep the assistant running
if __name__ == "__main__":
    speak("Hello, I am your assistant. How can I help you?")

    while True:
        command = take_command()
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        respond_to_command(command)
