import requests
import speech_recognition as sr
import pyttsx3
import musiclibrary  
from openai import openAI
from gtts import gTTS
import pygame 
import os 
import webbrowser
recognizer = sr.recognizer()
engine = pyttsx3.init()
newsapi ="77e94f1641464f89acda97a29aa1c6a8"
def speak_old(text):
    engine.say("text")
    engine.runAndWait()
    newsapi="77e94f1641464f89acda97a29aa1c6a8"
def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    def processcommand(c):
        print(c)
        if __name__==" __main__":
            speak("initializing jarvis....")
            while true:
                #listen for the wake word "jarvis"
                #obtain audio for microphone
                r=sr.recognizer()
                print("recognizing")
             try:
                  with sr.Microphone()as source:
                      print ("listening...")
                      audio =r.listen(source,timeout=2,phase_time_limit=1)
            word =r.recognizer_google(audio)
            if (word.lower()=="jarvis"):
                speak("ya")
                #listen for command
                with sr.Microphone() as source:
                    print("jarvis active.....!!!")
                    command = r.recognizer_google(audio)
                    processcommand(command)
                 except Exception as e:
                print("error;{0}".format(e))
                #to add features of open google changes in def command
                def processcommand(c):
                    if"open.google"in c.lower():
                       webbrowser.open("https://google.com")
                    elif"open facebook"in c.lower():
                        webbrowser.open("https://facebook.com")
                    elif"open youtube"in c.lower():
                        webbrowser.open("https://youtube.com")
                    elif"open pysics wallah"in c.lower():
                        webbrowser.open("https:pysics wallah.com")
                    elif c.lower().startswith("play"):
                        song=c.lower().split(" ")[1]
                        link=musiclibrary.music[song]
                        webbrowser.open(link)
                    elif "news" in c.lower():
                        r=requests.get("https//newsapi.org/v2/top-headlines:country=us&api key={newsapi}")
                        #parse the json  response
                        data =r.json()
                        #extract the article
                        article=data.get('article',[])
                            #print the headlines
                        for articles in articles:
                            speak(article['title'])   
                        else:
                            output=aiProcess(c)  
                            speak(output)     
                            completion=client.completions.create(
                            model="gpt 3.5-turbo"
                            messages=[
                            { "role":"system","contents":"you are a virtual assistence jarvis skilled in general tasks like alexa and google cloud"}
            {"role":"user","contents":command}
               ])
            print(completions.choices[0].messages.content)
        #initialize pygame mixer
    pygame.mixer.init(
    )
    #load the mp3  file
    pygame.mixer.music.load("temp.mp3")
    #play the mp3 file
    pygame.mixer.music.load("temp.mp3")
    #play the mp3 file
    pygame.mixer.music.play()
    #keep the program runs until the music plays
    while pygame.mixer.music.get_busy():
        pygame.time.clock().tick(10)
        pygame.mixer.music.unload()
        os.remove("temp.mp3")
    def aiProcess(command):
        client=openAI(
            api_key="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"
        )
        completion=client.chat.completions.create(
        model="gpt 3.5-turbo"
        messages=[
            { "role":"system","contents":"you are a virtual assistence jarvis skilled in general tasks like alexa and google cloud"}
            {"role":"user","contents":command}
        ]
        )
import requests
import speech_recognition as sr
import pyttsx3
import musiclibrary  # Ensure you have this module and the 'music' dict in it
import os
import webbrowser
import pygame
from gtts import gTTS
from openai import OpenAI  # Fix: Correct import

# Initialize recognizer and TTS
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# API Keys
newsapi_key = "77e94f1641464f89acda97a29aa1c6a8"
openai_api_key = "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"

# Speak using gTTS
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    os.remove("temp.mp3")

# Process the command
def process_command(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open physics wallah" in c:
        webbrowser.open("https://www.pw.live")
    elif c.startswith("play"):
        song = c.split(" ", 1)[1]
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")
    elif "news" in c:
        get_news()
    else:
        output = ai_process(c)
        speak(output)

# News feature
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}"
    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])
        for article in articles[:5]:  # Limit to 5 headlines
            speak(article.get("title", "No Title"))
    except Exception as e:
        speak("Failed to fetch news.")
        print(f"Error fetching news: {e}")

# AI Processing
def ai_process(command):
    try:
        client = OpenAI(api_key=openai_api_key)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are ram, a helpful assistant."},
                {"role": "user", "content": command}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"AI processing error: {e}")
        return "Sorry, I couldn't process that."

# Main loop
if __name__ == "__main__":
    speak("Initializing ram...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
                word = recognizer.recognize_google(audio)
                print("Heard:", word)
                
                if word.lower() == "ram":
                    speak("Yes?")
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print("Command:", command)
                        process_command(command)

        except Exception as e:
            print(f"Error: {e}")

import requests
import speech_recognition as sr
import pyttsx3
import musiclibrary  # Make sure this module exists and has `music` dict
import os
import webbrowser
import openai

# Initialize recognizer and TTS engine (pyttsx3)
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# API Keys (replace with your own keys)
newsapi_key = "77e94f1641464f89acda97a29aa1c6a8"
openai_api_key = "your-openai-api-key-here"

openai.api_key = openai_api_key

# Speak function using pyttsx3 (offline, no temp file issues)
def speak(text):
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

# Process the command
def process_command(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open physics wallah" in c:
        webbrowser.open("https://www.pw.live")
    elif c.startswith("play"):
        song = c.split(" ", 1)[1]
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")
    elif "news" in c:
        get_news()
    else:
        output = ai_process(c)
        speak(output)

# News feature
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}"
    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])
        for article in articles[:5]:
            speak(article.get("title", "No Title"))
    except Exception as e:
        speak("Failed to fetch news.")
        print(f"Error fetching news: {e}")

# AI Processing using official openai package
def ai_process(command):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are ram, a helpful assistant."},
                {"role": "user", "content": command}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"AI processing error: {e}")
        return "Sorry, I couldn't process that."

# Main loop
if __name__ == "__main__":
    speak("Initializing gouri...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
                word = recognizer.recognize_google(audio)
                print("Heard:", word)
                
                if word.lower() == "gouri":
                    speak("Yes?")
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print("Command:", command)
                        process_command(command)

        except sr.WaitTimeoutError:
            print("Listening timed out, retrying...")
        except Exception as e:
            print(f"Error: {e}")

