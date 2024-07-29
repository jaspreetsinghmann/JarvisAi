
import pyttsx3
import speech_recognition as sr
import datetime
from datetime import datetime as dt
import os
import cv2
import sounddevice as sd
import numpy as np
from requests import get
import wikipedia
import webbrowser
import urllib.parse
import pywhatkit as kit
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM"
engine.setProperty('voices',id)

#text to speech 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

#Convert Voice to Text

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0, 4)

    try:
        print("Recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said:{query}")
    except Exception as e:
        # speak("I cannot Understand That")
        return "none"
    return query    

#Wishing Function
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("Good Morning Sir,")
    elif hour>12 and hour<18:
         speak("Good Afternoon Sir,")   
    elif hour>=18 and hour<=21:
        speak("Good Evening Sir,")
    else:
        speak("Isn't it getting late Sir, The The is ")
    speak("How May I Help You Sir?")

#Time
def time():
    time = dt.now()
    formatted_time = time.strftime("%I:%M:%S %p")
    speak(f"The Current Time is {formatted_time}")

#Date    
def date():
    date = dt.now()
    formatted_date = date.strftime("%B %d, %Y")
    speak(f"The Current Date is {formatted_date}")

#Open Notepad
def notepad():
    path = "C:/Windows/notepad.exe"
    os.startfile(path)
#Open Cmd
def cmd():
    path = "C:/WINDOWS/system32/cmd.exe"
    os.startfile(path)
#Open Camera -- not done 
def camera(): 
    cap = cv2.VideoCapture(0)
    if not (cap.isOpened()):
        print("Could not open video device")
    while(True):
        ret, frame = cap.read()
        cv2.imshow('preview',frame)
    cap.release()
    cv2.destroyAllWindows()
#First Talking     
  
#Brave Browser
def brave():
    path = "C:/Users/DELL/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe"
    os.startfile(path)

#Open Chrome:
def chrome():
    path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    os.startfile(path)

def music():
    music_dir = "F:/Study Material/JarvisAI/Music"
    songs = os.listdir(music_dir)
    rd = random.choice(songs)
    for song in songs:
        if song.endswith('.mp3'):
            os.startfile(os.path.join(music_dir,rd))

def ip_address():
    ip = get('http://api.ipify.org').text
    speak(f"Your Id Address is {ip}")

def youtube():
    webbrowser.open("http://www.youtube.com")

# def msg():
#     kit.sendwhatmsg("+917058867909","69",8,7)
def password():
    speak(f"The password for wifi is arigatou@1313")    
def incognito():
    url = "https://google.com"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito"
    webbrowser.get(chrome_path).open(url)
      
def MainExecution(query):
    Query = str(query).lower()
    if "hello" in Query:
        speak("Hello Sir ,Welcome Back")
    elif "open notepad" in Query:
        notepad()
    elif "open cmd" in Query:
        cmd()
    elif " time" in Query:
        time()
    elif "open camera" in Query:
        speak("Not Yet Completed")
        # camera()
    elif " date" in Query:
        date()
    elif "open brave" in Query:
        brave()
    elif "wish me" in Query:
        wish()
    elif "open chrome" in Query:
        chrome()
    elif "password" in Query:
        speak(f"The password for wifi is arigatou@1313")    
    elif "play music" in Query:
        music()
    elif "ip address" in Query:
        ip_address()
    elif "wikipedia" in Query:
        speak("Searching Wikipedia....")
        query = Query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak(f"According to Wikipedia ... {results} ")
    elif "open youtube" in Query:
        youtube()
    elif "incognito" in Query:
        incognito()
    elif "google" in Query:
        base_url = "https://www.google.com/search?q="
        query_string = urllib.parse.quote_plus(query)
        url = base_url + query_string
        webbrowser.open(url)
    # elif "youtube" in Query:  
    #     speak('What do you want to play on Youtube, sir?')
    #     video = takeCommand().lower()
    elif "sleep" in  Query:
        speak("Ok Sir See You Soon!...")
        quit()    
    else:
        speak("I cannot Understand That")
while True:
    print("")
    Query = takeCommand()
    MainExecution(Query)

 # /////////////////////////////////////////////

# if __name__ == "__main__":
#     wish()
#     # while True:
#     if 1:
#         query = speechrecognition().lower()
        
#         if "open camera" in query:
#             camera()
#     speechrecognition()
#     time()
#     wish()
#    speak("Hello, I am your AI assistant.")    
