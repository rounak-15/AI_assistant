import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pyjokes
import requests
import openai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
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
        print("Say that again please...")  
        return "None"
    return query

def get_weather():
    api_key = "your_openweathermap_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "your_city"
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

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "I'm sorry, I couldn't process that."

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

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
            speak("Opening Google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening Stack Overflow")

        elif 'open wikipedia' in query:
            webbrowser.open("wikipedia.com")
            speak("Opening Wikipedia")

        elif 'play music' in query:
            music_dir = 'you music directory'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("PLaying Music")

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
            response = generate_response(query)
            speak(response)
            print(response)
