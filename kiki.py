import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit as kit


machine = pyttsx3.init('sapi5')
voices = machine.getProperty('voices')
machine.setProperty('voice',voices[1].id)

def speak(audio):
    machine.say(audio)
    machine.runAndWait()

def greet():
    time = int(datetime.datetime.now().hour) 
    if time >= 0 and time <=12:
        speak('Good morning bhawna and chinmay')
    elif time >= 12 and time <=17:
        speak('Good afternoon bhawna and chinmay')
    else:
        speak('Good evening bhavna and chinmay') 
    speak('hello bhavna and chinmay, i am lily . how may i help you')

def order():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        c.pause_threshold = .5
        audio = c.listen(source)
        
    try:
        print('Recognizing...')
        query = c.recognize_google(audio,language='en-in')
        print(f'user said:- {query}\n')

    except:
        print('Say that again please...')
        return "none"

    return query

if __name__ == "__main__":
    greet()
    while True:
        query = order().lower()
        if 'wikipedia' in query:
            speak('Searching your choice')
            query = query.replace("wikipedia","")
            answer = wikipedia.summary(query, sentences=2)
            print('According to wikipedia')
            print(answer)
            speak('According to wikipedia')
            speak(answer)

        elif 'youtube' in query:
            kit.playonyt(query)
            break

        elif 'google' in query:
            kit.search(query)

        elif 'open zoom app' in query:
            filepath = "C:\\Users\\chinmay khanna\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(filepath)
            break

        elif 'open main' in query:
            filepath = "c:"
            os.startfile(filepath)

        elif 'open code' in query:
            filepath = "d:"
            os.startfile(filepath)

        elif 'open entertainment' in query:
            filepath = "e:"
            os.startfile(filepath)

        elif 'open movies' in query:
            filepath = "E:\\scaned pdf and movies\\movies"
            os.startfile(filepath)

        elif 'send message' in query:
            while True:
                print("Enter the mobile number")
                speak("Enter the mobile number")
                num = input()
                print('Enter the message')
                speak('Enter the message')
                msg = input()
                print("Enter the time")
                speak("Enter the time")
                hr,sec = map(int,input().split())
                print("Type yes if you want to send the message")
                speak("Type yes if you want to send the message")
                check = input().lower()
                if check == "yes":
                    kit.sendwhatmsg(num,msg,hr,sec)
                    break
                break

        elif 'hello' in query:
            print('Hello Chinmay and Bhawna')
            speak('Hello Chinmay and Bhawna')

        elif 'how are you' in query:
            print('I am fine . how are you???')
            speak('I am fine . how are you?')

        elif 'i am fine' in query or 'i am good' in query:
            print('ohh good!! ok now tell me how can i help you???')
            speak('oh good . ok now tell me how can i help you?')

        elif 'bad mood' in query:
            print("don't worry.. everything will be alright.. you can see movies or songs on youtube tell me what should i open for you??")
            speak("don't worry . everything will be alright . you can see movies or songs on youtube tell me what should i open for you?")
        
        elif 'thank you' in query:
            print('mention not.. it is my duty to serve you a good results')
            speak('mention not . it is my duty to serve you a good results')

        elif 'go for a drive' in query:
            print('ok.. Sure..')
            speak('ok . sure .')

        elif 'but when' in query:
            print('when ever you want')
            speak('when ever you want')  

        elif 'stop' in query:
            speak('yaa sure . have a great day ahead')
            break
        elif 'close' in query:
            speak('yaa sure . have a great day ahead')
            break
