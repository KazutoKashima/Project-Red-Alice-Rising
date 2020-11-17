#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

""" ---------------------- Importing Required Modules ---------------- """
from tkinter import *
from tkinter import ttk
import speech_recognition as sr
from pygame import mixer
import threading
import pyttsx3

# initialising PyTTSx3
v = pyttsx3.init()

""" ------------------------- Setting up the GUI --------------------- """
# Tkinter app init (using custom ico in the title), using custom theme
icon = ""
root = Tk()                              
root.title('Alice - Voice Input')
root.iconbitmap('../dataFiles/Alice.ico')
style = ttk.Style()
style.theme_use('alt')

# The image that is used for the speak button

photo = PhotoImage(file='../dataFiles/msg.png').subsample(15,15)

# creating a guiding label widget
label1 = ttk.Label(root, text="Speak! -> Paste (Or CMD/CTRL+V)", font="Courier 11 bold")
label1.grid(row=0, column=1)


""" ---------------------- Possible Commands ------------------------ """
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey', 'sup', 'whats up?', 'oi', 'yo', 'Gday!', 'hallo', 'Hello', 'Hey', 'Yo', 'Sup', 'Oi', 'Hola', 'gday', 'Hallo']   
questions = ['how are you?', 'How are you?','how are you doing?', 'how are you', 'How are you', 'how are you doing', 'how are ya?', 'how are ya']   
question_responses = ['Okay', "I'm fine", 'i am great!', "Brilliant!"]   
greeting_responses = ['Hello!', 'How are you?', 'Good day!', 'Gday mate!']   
time = ['What is the time?', 'What time is it?', 'what is the time', 'what time is it', 'whats the time']  
QRS = ['thats great', 'nice', 'cool'] # Question Response # not really needed.
humanEmotionG = ['Great', 'Brilliant', 'Awesome', 'Good', 'nice', 'happy', 'superfluous', 'excited', 'good', 'great', 'Nice', 'Happy', 'Superfluous', 'Excited', 'awesome', 'brilliant']   
humanEmotionB = ['upset', 'sad', 'bad', 'ugly', 'stupid', 'like an idiot', 'foolish']  
HEGResponse = ['Thats great!', 'Im glad to hear that! :)', 'Thats awesome']   
HEBResponse = ['Whats wrong?', 'Im sorry to hear that', 'Can I help you?']   
HelpRequestPositive = ['Yes', 'you can']  
HelpRequestNegative = ['no', 'unfortunately not', 'you cant']  
HRPResponse = ['Ok, what do you want me to do?', 'How can I help']   
HRNResponse = ['Oh... Sorry I wish I could help :(', 'Thats sad to hear', 'Thats no good', 'Dont worry! Everything gets better eventually :)', 'I wish you were feeling better']   
EmotionQuestion = ['How are you?', 'What are you feeling like?']   
thanks = ['thank you', 'Thank you', 'thanks', 'Thanks']   
thanksResponse = ['You are welcome!', "You're welcome!", 'No problem!']    
goodbye = ["Goodbye", 'cya', 'bye', 'goodbye', 'later']     
LawsOfRoboticsQ = ['Do you follow the three laws of robotics?', 'do you follows the laws of ai']
LORQA = ['Yes I do', 'Why wouldn\'t I?', 'Why of course I do!']
Help = ['Can you help me?', 'I need help', 'help', 'Help', 'i need your help', 'can you help me?', 'can you help me', 'Can you help me', 'i need help', 'can you help with something', 'can you help me with something?']
searchFor = "I want to search for something"
# PC Controlling 
LogoutPC = ['Logout of my pc', 'logout of pc']
LockMyPC=['Lock my PC', 'Lock PC', 'lock my pc', 'lock pc']
RestartPC=['Restart my PC', 'restart my pc', 'restart pc', 'Restart PC']
ShutdwnPC=['Shutdown my PC', 'shutdown my pc', 'shutdown pc', 'Shutdown PC']

""" ---------------------- Main Logic ------------------------------- """
# the main logic, defining what clicking of Speak! does
def buttonClick():
    import time
    import os
    import psutil
    import pyperclip
    import pygame
    import pyttsx3
    import random

    v = pyttsx3.init()  

    # using pygame mixer to play prompt.
    mixer.init()
    mixer.music.load('../dataFiles/chime.mp3')
    #mixer.music.play(1)

    # start the recognizer, with some optional params that Cristi Vlad identified
    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

    try:

        with sr.Microphone() as source:
            
                audio = r.listen(source, timeout=5)

                message = str(r.recognize_sphinx(audio))

                # playing the sound after the recognition

                mixer.music.load('../dataFiles/chime.mp3')
                #pygame.mixer.play()

                # place the recognized 'message/data' onto the clipboard
                pyperclip.copy(message)

                if message in greetings:
                    response = random.choice(greetings)
                    v.say(response)
                    print(response)

    except sr.UnknownValueError as UnknownValErr:
        print("Sorry! But I couldn't understand you, could you please try again?")
        with open("../coreFiles/errors.log", "w+") as f:
            f.write(f"\n-------------- UnknownValueError ------------\n {UnknownValErr}\n")
            f.close()

    except sr.RequestError as ReqErr:
        print("Sorry but I can't seem to connect to my recognition server...are you connected to the internet??")

        with open("../coreFiles/errors.log", "w+") as f:
            f.write(f"\n---------------- RequestError ----------------\n {ReqErr}\n")
            f.close()

    except OSError as OSErr:
        print("Sorry but I can't seem to find and Audio Input Device?")
        v.say("Sorry but I can't seem to find your microphone?")

        with open("../coreFiles/errors.log", "w+") as f:
            f.write(f"\n---------------- OSError --------------------\n {OSErr}\n")
            f.close()

    except sr.WaitTimeoutError as TimeOutErr:
        print("Sorry but there was a time out error! See the logs for more information!")
        v.say("Sorry but there was a timeout error, please try again in a few seconds!")

        with open("../coreFiles/errors.log", "w+") as f:
            f.write(f"\n------------------ TimeoutError ------------------\n {TimeOutErr}\n")
            f.close()

""" ---------------- Preventing the App from Freezing (as best as possible) --------------- """
# using threading to prevent the app from freezing or becoming unresponsive
def thr():
    t1 = threading.Thread(target=buttonClick, daemon=True)
    t1.start()


""" ---------------------- Aligning the Speak Input Button ------------------------------ """
# creating the Speak button
SpeakButton = Button(root, image=photo, width=150, command=thr, activebackground='#c1bfbf', bd=0)
SpeakButton.grid(row=0, column=2)

""" --------------- Setting if the App is on the Forescreen or not ---------------- """
# making sure the app stays open above others? -- Optional
root.wm_attributes('-topmost', 1)

""" ----- Run it ----- """
# Woo! Running it!
root.mainloop()
