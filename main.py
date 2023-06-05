import os

import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
from config import apikey


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    print("Enter the word to speak")
    s = text
    speaker.Speak(s)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured"

if __name__ == '__main__':
    say("Hello")
    while True:
        print("Listening...")
        query = takeCommand()

        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikpedia.com"],["google","https://www.google.com"],["chat","https://chat.openai.com/"],["spotify","https://open.spotify.com"]]
        musics = [["music 1","music 1 location"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f"Opening{site[0]}")

        for music in musics:
            if f"play music {music[0]}".lower() in query.lower():
                musicPath = music[1]
                os.startfile(musicPath)
                say(f"playing{music[0]}")

        if "open github" in query.lower():
            app= "app location"
            os.startfile(app)
            say(f"opening github")

        if "the time" in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")
            #say(query)

