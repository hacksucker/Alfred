import requests
import speech_recognition as sr
import sys
import json
import os, sys
import decimal
from pygame import time
from pygame import mixer
from datetime import datetime
from threading import Timer
import time
from os import path
mixer.init()
#wichtige anweisungen
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Elmshorn,de&appid=1315c24fc8fb891ac85226068eb95b0b')




#data = r.json()
#Wetter23 = (data['weather'][0]['main'])
#Celsius = (float(data["main"]['temp'])-273.15)





    

def playPop():
    mlist=[]
    
    for file in os.listdir("Playlists/Masterlist"):
        
        if file.endswith('.mp3'):
            mlist.append(file)
            
            
            mixer.music.load("Playlists/Masterlist/"+file)
            mixer.music.play()
            mixer.get_busy()
            while mixer.music.get_busy() == True:
                continue




def main():
    print("Was brauchen sie Sir \n 1.)Wetter() \n 2.)Licht An/Aus()")


def Wetter():
    
    print(round(Celsius))
    print(Wetter23)
    Celsius =str(Clesius)

def licht():
    r = requests.get('http://192.168.178.97/ay?o=1', auth=('fin', 'root'))


def close():
    sys.exit()

def vorstellung():
    mixer.music.load("Sprachbeispiele/Vorstellung.mp3")
    mixer.music.play()


x=datetime.today()
y=x.replace(day=x.day+1, hour=6, minute=0, second=0, microsecond=0)
delta_t=y-x

def gutenMorgen():
    Satz = str("Guten Morgen Sir! Es ist 6 Uhr Morgens, Draußen sind es "+Celsius+" grad Celsius mit einem klaren Himmel. Das ist das Ideale wetter zum zocken!")
    Name="gutenmorgen"
    
    
    path="Sprachbeispiele/"+Name+".mp3"
    fo=open(path,"wb")
    fo.write(r.content)
    fo.close()
    mixer.music.load(path)
    mixer.music.play()





secs=delta_t.seconds+1


t = Timer(secs, gutenMorgen)
t.start()















#1315c24fc8fb891ac85226068eb95b0b


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="de_DE")
        print('Ihr Befehl: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Ich kontte dich nicht verstehen')
        command = myCommand()

    return command







def assistant(command):
    "if statements for executing commands"
    

    

    if "Wetter" in command:
        Wetter()

    if "Licht an" in command:
        licht()

    if "Licht aus" in command:
        licht()


    if "schließen" in command:
        close()
    
    if "stell dich vor" in command:
        vorstellung()

    #if "Spiel Musik" in command:
    #    playlist()

    if "Lieblingsmusik" in command:
        playPop()















    
while True:
    assistant(myCommand())









