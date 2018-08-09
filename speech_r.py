#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 10:09:59 2018

@author: afnity_computer
"""

from gtts import gTTS
import os

import pygame
from pygame import mixer
mixer.init()





import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text="hey What'sup", lang='en')
    tts.save("sp.mp3")
    os.system("mpg321 hello.mp3 -quiet")

def recordAudio():
    #RecordAudio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say Something')
        audio = r.listen(source)
        
        
        
        
        
    #Speech recognition using Google Speech recognition
    data = " "
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("you said: " + data)
    except sr.UnknownValueError:
        print("Google speech recognition could not understand audio")
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
    return data
        
def jarvis(data):
    print(data)
    if "Black Sheep" in data:
        mixer.music.load('/Users/afnity_computer/Documents/voice_assistant/va_prototype/Baa-Baa-Black-Sheep-.mp3')
        mixer.music.play()


data = recordAudio()
jarvis(data)
        
        
#def pause(data):
#    if "matrix" in data:
#        pygame.mixer.music.pause()
 
        
        
        
#def paused():
#    pygame.mixer.music.pause()
            
    
"""
def jarvis(data):
    if "Bangalore" in data:
        location = 'bangalore'
        print('https://www.mapsofindia.com/maps/karnataka/bangalore-large.htm')
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
        #speak("I am fine")
        
"""

#data = recordAudio()
#jarvis(data)
#pause(data)


#import pygame
#from pygame import mixer
#mixer.init()
#mixer.music.load('/Users/afnity_computer/Documents/voice_assistant/va_prototype/harvard.wav')
#mixer.music.play()