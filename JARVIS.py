import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyjokes
import pyautogui
from datetime import date
import requests
import sys
from bs4 import BeautifulSoup  

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
        

def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir, I am your personal voice assistant, JARVIS. How may I help you")
    elif hour>=12 and hour <16:
        speak("Good AFternoon Sir, I am your personal voice assistant, JARVIS. How may I help you?")
        
    else:
        speak("Good Evening Sir,  I  am   your   personal   voice assistant , JARVIS. How may I help you?")

def Take_Command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n" )
        
    except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"
    return query
    
if __name__ == "__main__":
    while True:
         query = Take_Command().lower()
         
         # Logic for executing tasks based on query
         if 'wikipedia' in query:
             speak("Browsing Wikipedia...")
             query = query.replace("wikipedia" , "")
             results = wikipedia.summary(query, sentences = 2)
             speak("According to wikipedia")
             print(results)
             speak(results)
             
         elif 'school protocol' in query:
             speak("Inistialising School protocol")
             webbrowser.open("https://meet.google.com/")
             webbrowser.open("https://web.whatsapp.com/")
             
         elif 'gaming protocol' in query:
             speak("Inistialising Gaming protocol")
             webbrowser.open("https://web.whatsapp.com/")
             webbrowser.open("https://meet.google.com/")
             webbrowser.open("https://shellshock.io/?showAd=false")
             
             
         elif 'open youtube' in query or 'play youtube' in query or 'play a video' in query or 'search on youtube' in query:
            dg = 'what should i search on youtube', 'what would you like to search on youtube', 'say the words you like to search on youtube'
            speak(random.choice(dg))
            x = Take_Command().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")
            
         elif 'capital' in query:
             query = query.replace("wikipedia" , "")
             results = wikipedia.summary(query, sentences = 1)
             speak("According to wikipedia")
             print(results)
             speak(results)
            
         elif 'open google' in query:
             speak("opening")
             webbrowser.open("google.com")
            
         elif 'play my favourite playlist' in query:
             speak("playing")
             webbrowser.open("https://open.spotify.com/playlist/6lmkOtTdAmVjMWUqUjyrEe")
            
         elif 'play my favorite song' in query:
             speak("playing")
             webbrowser.open("https://www.youtube.com/watch?v=fKopy74weus")
             
         elif 'open my website' in query:
             speak("opening")
             webbrowser.open("https://harshilgauravshah.github.io/Portfolio/")
             
         elif 'open chess' in query:
             speak("opening")
             webbrowser.open("https://www.chess.com/home")
             
         elif 'open a meet' in query:
            speak("Opening")
            webbrowser.open("https://meet.google.com/nur-agkn-ygk")
             
         elif 'rickroll' in query:
             speak("opening")
             webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
             
         elif 'play come and get your love' in query:
             speak("opening")
             webbrowser.open("https://www.youtube.com/watch?v=bc0KhhjJP98")
             
         elif 'play we will rock you' in query:
             speak("opening")
             webbrowser.open("https://www.youtube.com/watch?v=-tJYN-eG1zk")
             
         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir the time is {strTime}")
             print(f"Sir the time is {strTime}")
             
         elif 'open spotify' in query:
             speak("opening")
             musicPath = "C:\\Users\\HP\\AppData\\Roaming\\Spotify\\Spotify.exe"
             os.startfile(musicPath)
             
         elif 'open whatsapp' in query:
             speak("opening")
             webbrowser.open("https://web.whatsapp.com/")
             
         elif 'open discord browser' in query:
             speak("opening")
             webbrowser.open("https://discord.com/channels/@me")
             
         elif 'open shellshock' in query:
             speak("Opening")
             webbrowser.open("https://shellshock.io/?showAd=false")
             
         elif 'sleep' in query:
             speak("Ok Sir, bye.")
             speak("")
             speak("Jarvis is Offline")
             sys.exit()
             
         elif 'screenshot' in query:
             image = pyautogui.screenshot()
             image.save('screenshot.png')
             speak('Screenshot taken.')
             
         elif 'initiate' in query:
             speak('Target required')
             
         elif 'open beluga' in query:
             speak("opening")
             webbrowser.open("https://www.youtube.com/c/Beluga1%22")
             
         elif 'Bhavya' in query:
             speak('Good decision Sir, she is an absolute nincompoop')
             
         elif 'open classroom' in query:
             speak("opening")
             webbrowser.open("https://classroom.google.com/u/1/c/MzA3OTY2MDU0NjM3")
                
         elif 'open meet' in query:
             speak("opening")
             webbrowser.open("https://meet.google.com/")
             
         elif 'search' in query:
               speak("What do you want me to search for (please type) ? ")
               search_term = input()
               search_url = f"https://www.google.com/search?q={search_term}"
               webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(search_url)
               speak(f"here are the results for the search term: {search_term}")
               
         elif 'joke' in query:
             random_joke = pyjokes.get_joke()
             print(random_joke)
             speak(random_joke)
             
         elif 'thank you' in query:
             speak("Always at your service sir")
             
         elif 'wake up' in query:
             speak(".........Jarvis is online...")
             intro = "C:\\Users\\HP\\Desktop\\J.A.R.V.I.S FOLDER\\jarvis\\JARVIS with song\\intro.png.gif"
             os.startfile(intro)
             speak("")
             speak(".........Retinal Scan Complete...")
             speak(f"It is {date.today()} today.")
             search = "temperature in Mumbai"
             url = "https://www.google.com/search?q=Temperature%20in%20Mumbai"
             request = requests.get(url)
             data = BeautifulSoup(request.text,"html.parser")
             temp = data.find("div", class_="BNeawe").text
             speak(f"Current{search} is {temp}")
             speak("")
             wishMe()
             
         elif 'back to work' in query:
             speak("Jarvis is online")
             wishMe()
         
         elif 'lichess' in query:
             speak("opening")
             webbrowser.open("https://lichess.org/")

         elif 'good' in query or 'well' in query:
             speak(f'great to that you are well')

         elif 'who are you' in query:
             speak("I am JARVIS Point o created by HARSHIL SHAH")

         elif "how are you" in query:
             speak("I'm fine, glad you asked me that")
                
         elif 'krishna' in query:
             speak("Good decision Sir, she is an absolute nincompoop")
                
         elif 'hello' in query:
            gf = "O hello sir", "Hi sir", "I am here for your help sir!", "hello sir", "I was surfing the web, and gathering information for hacking pan, how can i help?", "Online and ready"
            speak(random.choice(gf))
            
         elif 'bye' in query:
             speak("Bye sir...have a great day ahead")
             speak("")
             speak("JARVIS is offline")
             sys.exit()
         
         elif 'alarm' in query:
             speak("Enter The time:")
             time = input("Enter The time :")
             
             while True:
                 Time_Ac = datetime.datetime.now()
                 now = Time_Ac.strftime("%H:%M:%S")
                 
                 if now==time:
                     speak("Time to wake up sir!")
                     musicPath = "C:\\Users\\HP\\Desktop\\J.A.R.V.I.S FOLDER\\jarvis\JARVIS with song\\ironman.mp3"
                     os.startfile(musicPath)
                     speak("Alarm CLosed")
                     
                 elif now>time:
                     break