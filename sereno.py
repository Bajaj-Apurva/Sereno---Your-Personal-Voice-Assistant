import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Initialize pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female voice, 0 for male voice

def speak(audio):
    """Convert text to speech"""
    engine.say(audio)
    engine.runAndWait()

def take_command():
    """Listen for voice commands and return the recognized text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
    except Exception as e:
        print(e)
        speak("I didn't understand")
        return "None"
    
    return query.lower()

if __name__ == '__main__':
    speak("Amigo assistance activated")
    speak("How can I help you?")
    
    while True:
        query = take_command()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'who are you' in query:
            speak("I am Amigo, developed by Jaspreet Singh")
        
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        
        elif 'open github' in query:
            speak("Opening GitHub")
            webbrowser.open("github.com")
        
        elif 'open stackoverflow' in query:
            speak("Opening Stack Overflow")
            webbrowser.open("stackoverflow.com")
        
        elif 'open spotify' in query:
            speak("Opening Spotify")
            webbrowser.open("spotify.com")
        
        elif 'open whatsapp' in query:
            speak("Opening WhatsApp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        
        elif 'play music' in query:
            speak("Playing music")
            webbrowser.open("spotify.com")
        
        elif 'open local disk d' in query:
            speak("Opening Local Disk D")
            webbrowser.open("D://")
        
        elif 'open local disk c' in query:
            speak("Opening Local Disk C")
            webbrowser.open("C://")
        
        elif 'open local disk e' in query:
            speak("Opening Local Disk E")
            webbrowser.open("E://")
        
        elif 'sleep' in query:
            speak("Goodbye!")
            exit(0)
