# pip install pyaudio

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pyjokes
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Mycro Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def get_weather():
    api_key = "aaa4eaa87280a0cb5d5b9cf36c92e5be"
    base_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={aaa4eaa87280a0cb5d5b9cf36c92e5be}"
    city_name = "Siliguri"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temp_celsius = main['temp'] - 273.15
        response_text = f"The temperature is {main['temp']}K with {weather['description']}."
    else:
        response_text = "City not found."

    return response_text

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open wikipedia' in query:
            webbrowser.open("wikipedia.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'weather' in query:
            weather_response = get_weather()
            print(weather_response)
            speak(weather_response)

        elif 'open code' in query:
            codePath = "C:\\Users\\Rounak\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
                
        else:
            print("No query matched")