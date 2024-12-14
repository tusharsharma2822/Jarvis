import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import time
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("Good Morning Boss!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Boss!")
    elif hour >= 16 and hour < 22:
        speak("Good Evening Boss!")
    else:
        speak("Good Night Boss!")

    speak("I am Jarvis, Your personal assitant, and please tell me how may I help you?")    

def takeCommands():
    r = sr.Recognizer()   
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:- {query}")

    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    
    return query 

if __name__ == '__main__': 
    #speak('Hello Boss, I am Jarvis, your personal AI Assitant!')
    wishMe()
    while True:
        query = takeCommands().lower()

        #Logic for executing tasks based on the query
        if 'wikipedia' in query:
            speak('Searching.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("Opening, Youtube....")
            webbrowser.get('chrome').open("youtube.com")

        elif 'open google' in query:
            speak("Opening, Google....")
            webbrowser.get('chrome').open("google.com")

        elif 'open spotify' in query:
            speak("Opening, Spotify....")
            webbrowser.get('chrome').open("open.spotify.com")    

        elif 'open chat' in query:
            speak("Opening, chatGPT....")
            webbrowser.get('chrome').open("chat.openai.com/")

        elif 'open leetcode' in query: 
            speak("Opening, Leetcode....") 
            webbrowser.get('chrome').open("leetcode.com") 

        elif 'open code' in query:
            speak("Opening, Visual Studio Code!")
            codePath = "C:\\Users\\tusha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'shutdown yourself' in query:
            speak("Bye Boss, I hope you have a nice day")
            break


        else:
            speak("Sorry Boss, I am not be able to understand!")
            break