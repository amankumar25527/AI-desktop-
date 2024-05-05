import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import  webbrowser
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning.........")
        r.pause_threshold=1
        audio=r.listen(source,timeout=3,phrase_time_limit=10)
        try:
            print("Reconizing....")
            query=r.recognize_google(audio, language='en-in')
            print(f"user said:{query}\n")
        except Exception as e:
            speak("Unable to recognize your voice ........")
            return "none"
        return query

# query=takeCommand().lower()

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def searchGoogle(query):
    if 'google' in query:
        import wikipedia as googleScrap
        query = query.replace("search", "")
        query = query.replace("on google", "")
        query=query.replace("emma","")
        query=query.replace("google search","")
        query=query.replace("google","")
        speak("this is what i found on google sir")

        try:
            pywhatkit.search(query)
            result=googleScrap.summary(query,2)
            speak(result)
        except:
            speak("nothing is found related to this")

def searchYoutube(query):
    if "youtube" in query:
        speak("this is what i found for you search!")
        query= query.replace("youtube search","")
        query = query.replace("search", "")
        query = query.replace("on youtube", "")
        query = query.replace("emma", "")
        query = query.replace("play", "")
        web ="https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done sir")
