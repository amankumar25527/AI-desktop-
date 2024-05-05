import random
import sys
import time

import speech_recognition as sr
import pyttsx3
import datetime
import os
import random
import wikipedia
import webbrowser
import pyjokes
import subprocess
import time
import pyautogui
import psutil
import winshell
import sys
import socket
import imdb
import  string
from GoogleNews import GoogleNews
import pandas as pd
import requests
from bs4 import BeautifulSoup

# def googleSearch(self,query):
#     query=query.replace("emma","")
#     query=query.replace("google","")
#     URL= 'https://www.google.com/search?q=' + query
#     header={
#         'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
#     }

def news():
    news=GoogleNews(period='id')
    news.search("India")
    result=news.result()
    data=pd.DataFrame.from_dict(result)
    data=data.drop(columns=["img"])
    print(data.head())
    data.head()
    for i in result:
        speak(i["title"])

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def password():
    char=string.ascii_letters+string.digits
    ret= ''.join(random.choice(char) for x in range(0,15))
# print(random())
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold=1
        audio=r.listen(source,timeout=3,phrase_time_limit=10)
        try:
            print("Recognizing....")
            query=r.recognize_google(audio, language='en-in')
            print(f"user said:{query}\n")
        except Exception as e:
            speak("Unable to recognize your voice ........")
            return "none"
        return query

def username():
    speak("what should i call you sir?")
    uname=takeCommand()
    speak("welcome Mister" +uname)
    speak("how can i help you,sir?")
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir !")
    speak("i am your virtual assistant emma")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("cpu is at "+usage)
    battery=str(psutil.sensors_battery())
    speak("cpu having battery "+battery+"percentage")
def camera():
    subprocess.run('start microsoft.windows.camera:', shell=True)
def movie():
    moviesdb=imdb.IMDb()
    speak("please tell the movie name sir")
    text=takeCommand()
    movies=moviesdb.search_movie(text)
    speak("searching for "+text)
    length=len(movies)
    if length==0:
        speak("no result found")
    else:
        speak("i found these ")
    for movie in movies:
        title=movie["title"]
        year=movie["year"]
        speak(f'{title}-{year}')
        info=movie.getID()
        movie=moviesdb.get_movie(info)
        # rating =moviedb.get_movie(info)
        rating=movie["rating"]
        plot=movie['plot outline']
        if year<int(datetime.datetime.now().strftime("%y")):
            speak(f'{title} was released in {year} has IMBD rating of {rating}.the plot summary of movie is {plot} ')
            break;
        else:
            speak(f'{title} will release in {year} has IMBD rating of {rating}.the plot summary of movie is {plot} ')
            break;


if __name__ == '__main__':
    print('pycharm')
    #speak("hello i am aman kumar")
    # wishme()
    # username()
    while True:
        order=takeCommand().lower()

        if 'how are you' in order:

            speak("I am fine ,thankyou")
            speak("how are you sir")
        elif 'fine' in order or 'good' in order:
            speak("it is good to know that you are fine.")
        elif 'who i am' in order:
            speak("if you can speak then you are a human.")
        # elif 'love' in order:
        #     speak("it is the sense that distroy all other sense")
        elif 'who are you' in order:
            speak("i am your virtual assistant Emma")
        elif 'I love u' in order:
            speak('oh my god, thankyou . I love you too .Anything i can help you with dear?')
        elif 'will you be my girlfriend' in order or 'will you be my valentine' in order:
            speak("I am not sure about that , maybe you should give me some more time.")
        elif 'what is your name' in order:
            speak("my friends call me emma")
        elif 'open notepad' in order:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)
        elif 'play music' in order or 'play song' in order or 'open music' in order or 'play music' in order:
            music_dir="C:\\Users\\25527\Desktop\music open"
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))
        elif 'wikipedia' in order:
            speak('searching......')
            order=order.replace("wikipedia","")
            order = order.replace("search", "")
            order = order.replace("on wikipedia", "")
            results=wikipedia.summary(order,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open google' in order:
            speak("here you go to google sir")
            webbrowser.open("google.com")

        elif 'open myntra' in order or 'search myntra' in order:
            speak("here you go to myntra sir enjoy shoping")
            webbrowser.open("myntra.com")
        elif 'open amazon' in order or 'search amazone' in order:
            speak("here you go to amazon sir enjoy shoping")
            webbrowser.open("amazon.in")
        elif 'open youtube' in order or 'search youtube' in order:
            speak("here you go to youtube sir")
            webbrowser.open("youtube.com")
        elif "where is" in order or 'what is my current location' in order:
            order.replace("where is","")
            location=order
            speak("locating........")
            speak("location")
            webbrowser.open("https://www.google.co.in/maps/place/"+location+"")
        elif "write a note" in order or 'please write a note' in order or 'write' in order:
            speak("what should i write, sir?")
            note=takeCommand()
            file=open('jarvis.txt','w')
            speak("sir,should i include date and time as well")
            sn=takeCommand()
            if 'yes' in sn or 'sure' in sn or 'yeah' in sn:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(note)
                speak("done sir")
            else:
                file.write(note)
                speak("done sir")
        elif 'show note' in order or 'open note' in order:
            speak("showing note")
            file=open("jarvis.txt","r")
            print(file.read())
            speak(file.read(6))
        elif 'joke' in order or 'make joke' in order:
            speak(pyjokes.get_joke(language="en",category="neutral"))
        elif 'time' in order:
            strTime=datetime.datetime.now().strftime("%H:%M:%s")
            speak(f"well the time is {strTime}")
        elif 'shutdown' in order or 'turn off' in order:
            speak("hold on sir the system in on its way to shutdown")
            speak("make sure your all the application are closed")
            time.sleep(5)
            subprocess.call(['shutdown','/s'])
        elif 'restart' in order:
            speak("your device is going for restart sir ")
            subprocess.call(['shutdown','/r'])
        elif 'hibernate' in order:
            speak("hibernating")
            subprocess.call(['shutdown','/h'])
        elif 'log off' in order or 'sign out' in order:
            speak("make sure all of your application closed befor sign off")
            time.sleep(5)
            subprocess.call(['shutdown','/i'])
        elif 'switch window' in order:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
        elif 'take screenshot' in order or 'screenshot this' in order:
            speak('sir,please tell me the name for this screeshot')
            name=takeCommand().lower()
            speak("please hold the screen")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screen shot capture sir!")
        elif 'cpu status' in order:
            cpu()
        elif 'empty recycle bin' in order or 'clear recycle bin' in order:
            winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)
            speak("recycle bin recycled")
        elif 'open camera' in order or 'take photo' in order:
            camera()
        elif 'open calculator' in order  or 'calculator' in order:
            speak("opening calculator sir....")
            # subprocess.Popen(paths['calculator'])
            subprocess.run('start microsoft.windows.calculator:', shell=True)

        elif 'exit' in order or 'quit' in order or 'by' in order or 'stop' in order:
            speak("ok sir , thankyou for using me have a nice day")
            sys.exit()
        elif 'ip' in order:
            speak("your ip address is ")
            host=socket.gethostname()
            ip=socket.gethostbyname(host)
            speak("your ip address is "+ip)
        elif 'bmi' in order:
            speak("please tell me your heigh in centimeter")
            height=takeCommand()
            speak("please tell me weight in kg")
            weight=takeCommand()
            height=float(height)/100
            BMI=float(weight)/(height*height)
            speak("your body mass index is "+str(BMI))
            if(BMI>0):
                if(BMI<=16):
                    speak("you are  severly underweight ")
                elif(BMI<=18.5):
                    speak("you are under weight")
                elif(BMI<=25):
                    speak("you are healthy")
                elif(BMI<=30):
                    speak("you are severly over weight")
                else:
                    speak("enter valid detail")
        elif 'movie' in order:
            movie()
        elif 'news' in order:
            news()
        elif 'password' in order:
            password()
        elif 'google' in order or 'search on google' in order or 'on google' in order:
            from search import  searchGoogle
            searchGoogle(order)
        elif 'youtube' in order or 'search on youtube' in order or 'on youtube' in order or 'play' in order:
            from  search import searchYoutube
            searchYoutube(order)
