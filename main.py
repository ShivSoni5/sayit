#!/usr/bin/env python

import speech_recognition as sr
import webbrowser as wb
from termcolor import colored
from time import sleep

BOLD = "\033[1m"   #use to bold the text
END = "\033[0m"    #use to close the bold text

r = sr.Recognizer()
with sr.Microphone() as source:
	print colored(BOLD+"Say your Query!"+END,"red")
	audio = r.listen(source)


try:
	sayit = r.recognize_google(audio)
	you_say = "Searching for "+sayit
	print colored(BOLD+you_say+END,"green")
	sleep(2)
	wb.open("https://www.google.com/search?q="+sayit+"")

except sr.UnknownValueError:
	print("I could not understand this audio")

except sr.RequestError as e:
	print("I could not request results from Google Speech Recognition service; {0}".format(e))

