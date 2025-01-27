import speech_recognition as sp
import webbrowser
import pyttsx3
import music

Recognizer=sp.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)

    engine.runAndWait()
def processcommand(a):
     if "open google" in a.lower():
          webbrowser.open("https://google.com")
     elif("open instagram" in a.lower()):
            webbrowser.open("https://instagram.com")
     elif("open github" in a.lower()):
          webbrowser.open("https://github.com/Ansh1803") 
     elif("open youtube" in a.lower()):
          webbrowser.open("https://youtube.com")
     elif a.lower().startswith("play"):
          song= a.lower().split(" ")[1]
          link=music.music[song]
          webbrowser.open(link) 
     elif ""== a.lower():
          speak("fine how about you sir")      





if __name__ == "__main__" :
    speak("Initializing jarvis....")
    while True:
        r = sp.Recognizer()
        
        print("recognizing.....") 

        try:
            with sp.Microphone() as source:
             print("listening!")
             audio = r.listen(source,timeout=2,phrase_time_limit=1)
            
            word=r.recognize_google(audio)
            if (word.lower()== "jarvis"):
                 speak("yes sir")
                 
                 with sp.Microphone() as source:
                      print("jarvis active")
                      audio = r.listen(source)
                      command =r.recognize_google(audio)

                      processcommand(command)


        except Exception as e:
                    print("error:| {0}".format(e))
        




