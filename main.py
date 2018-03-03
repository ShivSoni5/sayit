#!/usr/bin/env python

import speech_recognition as sr
import os
from termcolor import colored

BOLD = "\033[1m"   #use to bold the text
END = "\033[0m"    #use to close the bold text

r = sr.Recognizer()
while True:
	with sr.Microphone() as source:
		print colored(BOLD+"Say it!"+END,"red")
		audio = r.listen(source)


	try:
		sayit = "You said "+r.recognize_google(audio)

	except sr.UnknownValueError:
		sayit = "I could not understand this audio"

	except sr.RequestError as e:
		sayit = "I could not request results from Google Speech Recognition service; {0}".format(e)

	print colored(BOLD+sayit+END,"green")
	os.system("espeak -s 120 '"+sayit+"'")
