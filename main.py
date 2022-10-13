
# -*- coding: utf-8 -*-
# encoding: utf-8
import encodings
from importlib import *
import os
import unicodedata
import speech_recognition as sr
import pyaudio
import requests
import json
import sys
from naoqi import *

IP = "172.30.77.82"
PORT = 9559
def configNao(Name):
    try:
        tts = ALProxy(Name, IP, PORT)
    except Exception as e:
        print ("Could not create proxy ")
        print ("Error was: ",e)
    
    return tts

url = "https://api.openai.com/v1/completions"

headers = {
'Content-Type': 'application/json',
'Authorization': 'Bearer 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'
}
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
init_ai = "Ce qui suit est une conversation avec un assistant d IA qui s'appelle Nao en francais. L assistant est serviable, creatif, intelligent et tres sympathique. L assistant peu faire des blagues. "

def openai(text):
    promt = init_ai + restart_sequence + format(text)
    print(promt)
    payload = json.dumps({
    "model": "text-davinci-002",
    "prompt": promt,
    "temperature": 0.9,
    "max_tokens": 400,
    "top_p": 1,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,
    "stop": [ " Human:", " AI:"]
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    
    y = json.loads(response.text)
    
    parse = (y["choices"][0]["text"]).encode('utf-8')
    z = parse.split("Nao:")
    # z = z[0].split("Assistant:")
    print(z)
    return str(z[len(z)-1])

def recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, timeout=10, phrase_time_limit=5)
        
        print("Time over, thanks")
        text =""
        try:
            text = r.recognize_google(audio, language="fr-FR")
            print("You said: {}".format(text))
            return text

        except:
            print("Sorry could not recognize what you said")
            text =""
            return text
        
def naoSay(proxy,text):
    proxy.say(text)

proxySpeech = configNao("ALTextToSpeech")
proxySpeech.setParameter("pitchShift", 1.5)
proxySpeech.setParameter("doubleVoice", 0.0)


while True:
    question_humain = ""
    text = recognize()

    if text != "":
        print("You said: {}".format(text))
        
        naoSay(proxySpeech, openai(text))
        
    else: 
        print("je vous ecoute")
        naoSay(proxySpeech, "je ne vous ai pas compris")

    if text == "stop" or text == "Stop":
        break