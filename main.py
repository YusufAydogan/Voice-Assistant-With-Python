from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            speak("anlayamadım")
        except sr.RequestError:
            print("Sistem Çalışmıyor")
        return voice

def speak(string):
    tts = gTTS(text=string, lang = "tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.system(file)
    os.remove(file)

speak("Nasıl yardımcı olabilirim")

def response(voice):
    if "merhaba" in voice:
        speak("sana da merhaba genç")
    if "nasılsın" in voice:
        speak("ben çok iyiyim sen nasılsın")
    #Buraya istediğiniz kadar etkileşim koyabilirsiniz yukarıdaki iki örnek gibi...

while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice)
        response(voice)
    
