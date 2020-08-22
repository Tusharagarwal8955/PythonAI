import pyttsx3
import speech_recognition as sr
import datetime
import os


engine = pyttsx3.init()
# print(voices[1].id)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')


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

    speak("I am Siri version 2.0. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Sorry say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()


        if 'editor' in query:
            os.system('notepad')

        elif 'browser' in query:
            os.system('chrome')

        elif 'wallpaper' in query:
            speak('Your new wallpaper is downloading..')
            os.system('wall')
            speak('new wallpaper is applied, hope you like it')
            speak('powered by Tushar Agrawal')

        elif 'music' in query:
            os.system('vlc')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'code' in query:
            os.system('jupyter notebook')

        elif 'thank you' in query:
            print('See Yaa ! ! ')
            speak('Pleasure is all mine sir')
            speak('See yaa!')
            break
