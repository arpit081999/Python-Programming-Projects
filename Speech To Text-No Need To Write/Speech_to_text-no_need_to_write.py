"""
@author: Arpit Somani
"""

import speech_recognition as sr
AUDIO_FILE =("sample_arpit.wav")
#use audio file as source
r=sr.Recognizer()    #intialise the recogniser

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
#reads the audio file.
    
try:
    print("Audio File Contains :"+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speech recognition could not understand audio")
except sr.RequestError:
    print("Couldn't get the results from google speech recognition")