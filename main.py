import pyttsx3 #py text to speach module
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib #smptp mail transfer module
engine = pyttsx3.init('sapi5') # used sapi5 microsoft speech api

voices = engine.getProperty('voices') # get sapi5 voices
engine.setProperty('voice',voices[0].id) #set voice 1: female 0:male

def speak(audio):
    engine.say(audio) # speaks
    engine.runAndWait() # speak and wait for 0.8 secs


def wishMe():
    hour=int(datetime.datetime.now().hour) # current time function
    if hour >=0 and hour < 12:
        speak('Good Morning Sir!')
    if hour >=12 and hour < 18:
        speak('Good Afternoon Sir!')
    if hour >=18 and hour < 24:
        speak('Good Evening Sir!')
    speak("I am aditya soni's personal assistant , How may I help You Sir!")


def takeCommand():
    '''takes microphonic input--- returns --- string output'''
    r = sr.Recognizer() # r initiated as speech recognizer
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1 # to listen atleast 1 sec before user completes its sentance
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print('User said....\n',query)
    except Exception as e:
        # print(e)
        print('say that again... \n')
        return 'none'
    return query


def sendEmail(to,matter):
    server = smtplib.SMTP('smtp.gmail.com',587) # server set to smtp - gmail with port 587
    server.ehlo()
    server.starttls() # start
    server.login('from--- mail id--','password---')
    server.sendmail('from ---mail -- id--',to,matter)
    server.close()


if __name__=="__main__": # DRIVER CODE
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query=query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences = 2)
            speak("That's what I found on wikipedia     According to it")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak('what should i do after opening google')
            m = takeCommand()
            webbrowser.open(f'https://www.google.com/search?q={m}')
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
        elif 'open gmail' in query:
            webbrowser.open('gmail.com')
        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the current time is{strTime}')
        elif 'write mail' in query:
            try:
                speak('what should I say?')
                matter = takeCommand()
                sendEmail('to--mail--id--',matter)
                speak('Your email has been sent sir!')
            except Exception as e:
                speak('Sorry Sir, I am not able to send the email!')
        elif 'search on youtube' in query:
            speak('what to search sir!')
            command = takeCommand()
            webbrowser.open(f'https://www.youtube.com/results?search_query={command}')
        elif 'bye bye'in query:
            speak('It was pleasure to help you Sir, take care bye bye')
            break
