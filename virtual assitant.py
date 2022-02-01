import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit

engine = pyttsx3.init()
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id) #Voice id helps us to select different voices.


def speak(audio):    # To make our assistant talk.
    engine.say(audio)
    engine.runAndWait() #function will make the speech audible in the system


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=7 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your virtual assistant. Please tell me how may I help you")


def takeCommand(): #rcv cmd
    #It takes microphone input from the user and returns string output

    listener = sr.Recognizer()  # what is user say,to isten this audio  we need a listener
    with sr.Microphone() as source:  #call microphn of pc
        print("Listening...")  # when we see listening..user will ready to give her command
        listener.pause_threshold = 1  # it will execute only one command
        voice = listener.listen(source)

    try:
        print("Recognizing...")
        command = listener.recognize_google(voice, language='en-in') #Performs speech recognition on audio_data
        print(F"User said: {command}\n")



    except : # if engine dont understand the cmd
        print("Say that again please...")
        return "None"
    return command


def run_assistant():

    wishMe()
    while True:
    #if 1:
        command = takeCommand().lower()

        # Logic for executing tasks based on command

        if 'wikipedia' in command: # if there is wikipedia in user sentence
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in command: # if there is open yt in user sentence
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            webbrowser.open("google.com")


        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, current time is {strTime}")
            print(strTime)


        elif 'play' in command:
            song = command.replace ('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)


run_assistant()