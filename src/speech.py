#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import speech_recognition as sr
from pygame import mixer
import threading
import pyttsx3

v = pyttsx3.init()

# Tkinter app init (using custom ico in the title), using custom theme
icon = ""
root = Tk()                              
root.title('Alice - Voice Input')
#root.iconbitmap('../dataFiles/Alice.ico')
style = ttk.Style()
style.theme_use('alt')

# The image that is used for the speak button

photo = PhotoImage(file='../dataFiles/msg.png').subsample(15,15)

# creating a guiding label widget
label1 = ttk.Label(root, text="Speak! -> Paste (Or CMD/CTRL+V)", font="Courier 11 bold")
label1.grid(row=0, column=1)

# the main logic, defining what clicking of Speak! does
def buttonClick():
    import time
    import os
    import psutil
    import pyperclip
    import pygame


    # using pygame mixer to play prompt.
    mixer.init()
    mixer.music.load('../dataFiles/chime.mp3')
    mixer.music.play(1)

    # start the recognizer, with some optional params that Cristi Vlad identified
    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

    clock = pygame.time.Clock()

    while True: # main loop
        clock.tick(60)

        with sr.Microphone() as source:
            try:
                audio = r.listen(source, timeout=5)

                message = str(r.recognize_sphinx(audio))

                # playing the sound after the recognition

                mixer.music.load('chime.mp3')
                pygame.mixer.play()

                # place the recognized 'message/data' onto the clipboard
                pyperclip.copy(message)

                if "Hello".lower() in message:
                    v.say("Hi there user!")
            
            except sr.UnknownValueError as UnknownValErr:
                print("Sorry! But I couldn't understand you, could you please try again?")
                with open("error.log", "w+") as f:
                    f.write(f"-------------- UnknownValueError ------------\n {UnknownValErr}")
                    f.close()

            except sr.RequestError as ReqErr:
                print("Sorry but I can't seem to connect to my recognition server...are you connected to the internet??")

                with open("error.log", "w+") as f:
                    f.write(f"---------------- RequestError ----------------\n {ReqErr}")
                    f.close()
            
            else:
                pass

# using threading to prevent the app from freezing or becoming unresponsive
def thr():
    t1 = threading.Thread(target=buttonClick, daemon=True)
    t1.start()

# creating the Speak button
SpeakButton = Button(root, image=photo, width=150, command=thr, activebackground='#c1bfbf', bd=0)
SpeakButton.grid(row=0, column=2)

# making sure the app stays open above others? -- Optional
root.wm_attributes('-topmost', 1)

# Woo! Running it!

root.mainloop()
