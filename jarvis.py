# from math import e
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import os
import wikipedia
from youtube_web import *
from selenium_web import *
import keyboard
import pyjokes
from pywikihow import search_wikihow
import time

engine = pyttsx3.init('sapi5')
rate= engine.getProperty('rate')
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
# print(voices[2].id) #used for how many voices install in your pc
engine.setProperty('voice',voices[0].id)

def speak (audio):
    print("")
    engine.say(audio)
    print(f"{audio}")
    engine.runAndWait()



def takecommand():
    #its take microphone from the user and returns string output
    command = sr.Recognizer()
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        # command.pause_threshold = 1
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)        
        audio = command.listen(source)
        
        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-in')
            print(f"Person Said {query}")

        except Exception as Error:
            return "none"

        return query.lower()

def wishme():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%H:%M %p") 
    if hour>=0 and hour<12:
        speak(f"good morning, its {tt}")
    elif hour>=12 and hour<16:
        speak(f"good afternoon, its {tt}")
    elif hour>16 and hour<24:
        speak(f"good evening, its {tt}")
    else:
         speak(f"good night, its {tt}")

    speak('hello sushant')
    speak("I Am  Your Personal Voice Assistance")
    # speak("")

wishme()

def TaskExecution():

    def OpenSoftware ():

        speak("wait a second")

        if 'vlc' in query:
            speak("opening vlc media player....")
            os.startfile("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")

        elif 'little nightmares' in query:
            speak("opening littlenightmares....")
            os.startfile("D:\\Games\\Little Nightmares\\Atlas\\Binaries\\Win64\\LittleNightmares.exe")

        elif 'chrome' in query:
            speak("opening chrome....")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'youtube' in query:
            speak("opening youtube....")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("opening google....")
            webbrowser.open("google.com")

        elif 'map' in query:
            speak("opening google map....")
            webbrowser.open("google.com/maps")

     
    def CloseSoftware ():
        speak("ok wait a second")

        if 'vlc' in query:
            speak("closing vlc media player....")
            os.system("TASKILL /F /im vlc.exe")

        elif 'littleni ghtmares' in query:
            speak("closing littlenightmares....")
            os.system("TASKILL /F /im LittleNightmares.exe")

        elif 'chrome' in query:
            speak("closing chrome....")
            os.system("TASKKILL /F /im chrome.exe") 

        elif 'youtube' in query:
            speak("closing youtube....")
            os.system("TASKKILL /F /im msedge.exe")      

        elif 'google' in query:
            speak("closing google....")
            os.system("TASKKILL /F /im msedge.exe")

        elif 'map' in query:
            speak("closing google map....")
            os.system("TASkKILL /F /im msedge.exe")       

    def YoutubeAutomation ():
        speak("youtube automation on")

        if 'resume' and 'start' in query:
            keyboard.press('space bar' or 'k')

        elif 'pause' and 'stop' in query:
            keyboard.press('space bar' or 'k')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'next video' in query:
            keyboard.press('shift + n')

        elif 'previous video' in query:
            keyboard.press('shft + p')

        elif 'open miniplayer' in query:
            keyboard.press('i')

        elif 'close miniplayer' and 'exit miniplayer' in query:
            keyboard.press('i')

        elif 'full screen mode' in query:
            keyboard.press('f')

        elif 'close full screen mode' and 'exit full screen mode' in query:
            keyboard.press('f')

    def ChromeAutomation ():
        print("chrome automation started")

        # query=takecommand

        if 'close this tab' in query:
            keyboard.press_and_release('ctrl +w ')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t' )

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'downloads' in query:
            keyboard.press_and_release ('ctrl + j') 


    while True:

        query = takecommand()
            

        if ' joginder' in query:
            speak('Hello Sir')
            speak('yo joginder Thaara bhai joginder ')
            speak('How May I Help You??')

        elif 'how are you' in query:
            speak("I'M Good ,Thank You For Asking")
            # speak("what about you,Sir")
        
        elif 'tell mewho created you' and 'tell me who is your owner' in query:
            # query = query.replace("who is your owner"," ")
            speak("i am voice assistance created by Mr.sushant Sanjay Yadav")
        
   
        
        elif 'take some rest ' in query:
            speak("Ok, You Can Call Me Any Time")
            break

        elif 'tata' in query:
            speak("ok,see you again")
            break

        elif 'bye' in query:
            speak("Bye,see you again")
            break      
            
#used for playing music       
        elif 'music' and 'song' in query:
                r=sr.Recognizer()
                speak('which song u want to listen')
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source, 1.2)
                    r.pause_threshold = 1
                    print('Listning....')
                    audio = r.listen(source)
                    vid = r.recognize_google(audio)
                    speak("playing {} on youtube".format(vid))
                    print("playing {} on youtube".format(vid))

                assist=music_youtube()
                assist.play(vid)
                speak("enjoy your song")
#youtube Automation
        elif 'resume' and 'start' in query:
            keyboard.press('k')

        elif 'pause' and 'stop' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'next song' in query:
            keyboard.press('shift + n')

        elif 'previous song' in query:
            keyboard.press('shft + p')

        elif 'open miniplayer' in query:
            keyboard.press('i')

        elif 'close miniplayer' in query:
            keyboard.press('i')

        elif 'full screen mode' in query:
            keyboard.press('f')

        elif 'close full screen mode' and 'exit full screen mode' in query:
            keyboard.press('f')

        elif 'youtube tools' in query:
            YoutubeAutomation()


            
#getting information
        elif 'information' in query:
            r=sr.Recognizer()
            speak('what kind of information you want')
            with sr.Microphone() as source:
                print('Listning....')
                audio = r.listen(source)
                infor = r.recognize_google(audio)
                speak("searching {} on google".format(infor))
                print("searching {} on google".format(infor))

            assist = infow()
            assist.get_info(infor)
        
#using for wikipedia
        elif 'wikipedia' in query:
            speak('searching on wikipedia....')
            query = query.replace("joginder","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query, sentences=2)                
            speak ("acoording to wikipedia")
            speak(wiki) 

#open or close softwae
        elif 'open vlc' in query:
            OpenSoftware()  

        elif 'open little nightmares' in query:
            OpenSoftware()    

        elif 'open chrome' in query:
            OpenSoftware()

        elif 'open youtube' in query:
            OpenSoftware()
 
        elif 'open google' in query:
            OpenSoftware()

        elif 'open map' in query:
            OpenSoftware()

        elif 'close vlc' in query:
            CloseSoftware() 

        elif 'close littlenightmares' in query:
            CloseSoftware()

        elif 'close chrome' in query:
            CloseSoftware()

        elif 'close Youube' in query:
            CloseSoftware()

        elif 'close google' in query:
            CloseSoftware()

        elif 'close map' in query:
            CloseSoftware()

#chrome Automation
        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t' )

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'downloads' in query:
            keyboard.press_and_release ('ctrl + j')

        elif 'chrome automation' in query:
            ChromeAutomation()
        
        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'how to' in query:
            speak('getting information....')
            go = query.replace("jogindar","")
            max_result = 1
            how_to_func = search_wikihow(go,max_result)
            assert len(how_to_func) == 1
            how_to_func[0]
            speak(how_to_func[0].summary)




TaskExecution()


