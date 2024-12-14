import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning, Boss!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, Boss!")
    else:
        speak("Good Evening, Boss!")

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