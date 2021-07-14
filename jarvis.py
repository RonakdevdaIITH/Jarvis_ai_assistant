"""
This is main code for Jarvis AI it can do many simple task like opening youtude/google ,search something on wikipedia ,play music,play movies,open  your useful apps and many other things.you can add some of your task as per your choice .

Some of commands you can try :
1. Hey jarvis open YOUTUBE
2. Hey jarvis open GOOGLE
3. jarvis can you open Facebook for me
4. Tell me Jarvis who is shahrukhkhan WIKIPEDIA
5. jarvis pLAY MUSIC dude
6. Hey what is the TIME bro
7. i want to CODE
8. ohk jarvis BYE

Note: jarvis use keywords to understand what to do so dont forget to add those keywords(ex- youtube ,play music,time,code,bye) while speaking! 
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices') 

engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <11:
        speak('Very Good morning Sir!')

    elif hour >11 and hour <=16:
        speak('Good afternoon Sir!')

    elif hour >16 and hour <=19:
        speak('Good evening sir!')

    elif hour  >19 and hour <=24:
        speak('Good night sir!')

    speak("Hello, i am Jarvis. How can i help you ? ")
    
def takecommands():
    
    r =sr.Recognizer()
    with sr.Microphone() as source :  
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("recognizing ..") 
        query = r.recognize_google(audio,language = 'en-in')
        print(f"You mean :{query}\n")
       
    except Exception as e:
        # print(e)
        print("say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server  = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    #enter your email or password below
    server.login('youremail@gmail.com','your-password')
    server.sendEmail('youremail@gmail.com')    
    
if __name__ == "__main__":
    wishMe()
    while True:
        query =  takecommands().lower()
    # logic for executing task
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia") 
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            speak("Opening youtube ....")
            webbrowser.open_new_tab("youtube.com")
        
        elif "open google" in query:
            speak("Opening google....")
            webbrowser.open_new_tab("google.com")

        elif "open facebook" in query:
            speak("Opening facebook....")
            webbrowser.open_new_tab("facebook.com")

        elif "play music" in query:
            speak("Ohk here we go....")
            music_dir  = "C:\\favs"
            songs  = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "code" in query:
            speak(f"Ohk sir, Lets code!")
            code_path= "C:\\Users\\91702\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif "movie" in query:
            speak("As you wish sir....")
            movie_dir  = "C:\\Users\\91702\\Videos\\MOVIES\\Avengers"
            movies  = os.listdir(movie_dir)
            # print(songs)
            os.startfile(os.path.join(movie_dir,movies[0]))
        
        elif "email " in query:
            try:
                speak("What should i say?")
                content = takecommands()
                to = "recieversemail10@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successfully!")
            
            except Exception as e:
                # print(e)
                print("Sorry i am not able to send this email!")
            
        elif "hello" in query:
            speak("Hello sir, How are you?")

        elif "whatsup dude" in query:
            speak("I am good what about you sir ?")

        elif "how are you" in query:
            speak("I am good what about you sir ?")
        
        elif "who are you" in query:
            speak("Hello I am jarvis,I am created by Sir Ronak,I can help you in many ways like play music ,open some app , tell date or time and many more. I am an ai software made by using only python, There is no machine learning algorithm but you can update me if you want as per your need,just go through the code it is nice and simple,atlast Thank you for using me!!")
        
        elif "yourself" in query:
            speak("Hello I am jarvis,I am created by Sir Ronak,I can help you in many ways like play music ,open some app,tell date or time and many more. I am an ai software made by using only python, There is no machine learning algorithm but you can update me if you want as per your need,just go through the code it is nice and simple,atlast Thank you for using me!!")
        
        elif "stop" in query:
            speak("Ohk bye sir I am leaving ,have a good day!")
            exit()
        
        elif "bye" in query:
            speak("Okay bye sir I am leaving ,have a good day!")
            exit()
        
        elif "made" in query:
            speak("I am made by Sir Ronak Devda ,He is student of IIT hyderabad purusing BTEch in Electrical Engineering!")

        else:
            speak("I dont understand ,speak again please Otherwise sorry i can do this!") 
