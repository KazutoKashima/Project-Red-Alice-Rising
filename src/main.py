""" A warm welcome to fellow developers!

Hi there! this is a virtual assistant I started working on back in 8th grade.
It started off very basic but now I'm adding speech recognition and computer manipulation for ease of access and remote user control.

What's the purpose of this thing?
Well simple enough, it's literally designed to help users with imparements, mental instabilities to feel more comfortable using technology.
As there is no GUI (Graphical User Interface), yet I am currently not porting it to anything outside of a computer until I can get a suitable GUI for it.

What are the compatible Operating Systems? (OS Compatibility)
Well so far it's designed for MacOSX, Linux/UNIX, Debian and Windows
and has been tested thoroughly on Windows 10 and Linux Operating Systems.

"""


# required modules
import random 
from datetime import datetime 
from pytz import timezone
import webbrowser
import os
import subprocess
import json
# speech_recoginition as sr
# pyttsx3

lockPC='rundll32.exe user32.dll, LockWorkStation'

# Time
Australia = timezone ('Australia/Sydney') 
au_time = datetime.now (Australia) 
print (au_time.strftime ('%Y/%m/%d %H:%M:%S'))

# Initial greeting
def coreFileCheck():
        dbFile = '../coreFiles/data.log'
        checkFile = os.path.isdir("../coreFiles")
        
        """ 
        checking if the data file is there and has UserData in it,
        otherwise ask for name
        """

        if checkFile == True:
                with open(dbFile) as database:
                        data = json.load(database)
                        for usr in data['UserData']:
                                SIGNATURE1 = "Welcome back "+usr['name']+"!"+" What do you need?"
                                print(SIGNATURE1+'\n')
        else:
                SIGNATURE2 = input("Hi there! I am Alice! Your personal assistant! In order to continue, could you give me a name to call you by? This can be real or fake: ")
                data = {}
                data['UserData'] = []
                data['UserData'].append({
                        'name': SIGNATURE2
                })
                with open(dbFile, 'w+') as outfile:
                        json.dump(data, outfile)
                        
                with open(dbFile) as db:
                    data = json.load(db)
                    for usr in data['UserData']:
                        SIG3 = f"\nHi {usr['name']}! How can I help you?\n"
                        print(SIG3)
                    
""" Greeting """
coreFileCheck()

""" User and VA Q&As """
# User questions marked with #?
# Responses marked with #$
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey', 'sup', 'whats up?', 'oi', 'yo', 'Gday!', 'hallo', 'Hello', 'Hey', 'Yo', 'Sup', 'Oi', 'Hola', 'gday', 'Hallo'] #? 
questions = ['how are you?', 'How are you?','how are you doing?', 'how are you', 'How are you', 'how are you doing', 'how are ya?', 'how are ya'] #$
question_responses = ['Okay', "I'm fine", 'i am great!', "Brilliant!"] #$
greeting_responses = ['Hello!', 'How are you?', 'Good day!', 'Gday mate!'] #$
time = ['What is the time?', 'What time is it?', 'what is the time', 'what time is it', 'whats the time'] #?
QRS = ['thats great', 'nice', 'cool'] #$ QRS = Question Responses
timeResponse = au_time #$
humanEmotionG = ['Great', 'Brilliant', 'Awesome', 'Good', 'nice', 'happy', 'superfluous', 'excited', 'good', 'great', 'Nice', 'Happy', 'Superfluous', 'Excited', 'awesome', 'brilliant'] #$
humanEmotionB = ['upset', 'sad', 'bad', 'ugly', 'stupid', 'like an idiot', 'foolish'] #?
HEGResponse = ['Thats great!', 'Im glad to hear that! :)', 'Thats awesome'] #$
HEBResponse = ['Whats wrong?', 'Im sorry to hear that', 'Can I help you?'] #$
HelpRequestPositive = ['Yes', 'you can'] #?
HelpRequestNegative = ['no', 'unfortunately not', 'you cant'] #?
HRPResponse = ['Ok, what do you want me to do?', 'How can I help'] #$
HRNResponse = ['Oh... Sorry I wish I could help :(', 'Thats sad to hear', 'Thats no good', 'Dont worry! Everything gets better eventually :)', 'I wish you were feeling better'] #$
EmotionQuestion = ['How are you?', 'What are you feeling like?'] #$
thanks = ['thank you', 'Thank you', 'thanks', 'Thanks']  #?
thanksResponse = ['You are welcome!', "You're welcome!", 'No problem!']  #$
goodbye = ["Goodbye", 'cya', 'bye', 'goodbye', 'later'] #? #$
LawsOfRoboticsQ = ['Do you follow the three laws of robotics?', 'do you follows the laws of ai']
LORQA = ['Yes I do', 'Why wouldn\'t I?', 'Why of course I do!']
Help = ['Can you help me?', 'I need help', 'help', 'Help', 'i need your help', 'can you help me?', 'can you help me', 'Can you help me', 'i need help', 'can you help with something', 'can you help me with something?']
searchFor = "I want to search for something"
# PC Controlling 
LogoutPC = ['Logout of my pc', 'logout of pc']
LockMyPC=['Lock my PC', 'Lock PC', 'lock my pc', 'lock pc']
RestartPC=['Restart my PC', 'restart my pc', 'restart pc', 'Restart PC']
ShutdwnPC=['Shutdown my PC', 'shutdown my pc', 'shutdown pc', 'Shutdown PC']

""" Main Logic """
while True:

    #Gotta do a run to check for core memory files
    
    """ Core files are:
        - data.log
        - error.log
        - newWords.log
    """
    core = ['data.log', 'speech.py', 'newWords.log']
    if os.path.isfile('../coreFiles/data.log') == True:
        #print("data.log is ready!")
        pass
    
    else: 
        #print("Sorry but one of the main files are missing, please check that you have data.log, error.log or newWords.log in the coreFiles folder!\n\nIf not, please create whatever is missing EXCEPT FOR data.log")
        break

    if os.path.isfile('../coreFiles/errors.log') == True:
        #print("error.log is ready!")
        pass

    else: 
        print("Sorry but one of the main files are missing, please check that you have data.log, error.log or newWords.log in the coreFiles folder!\n\nIf not, please create whatever is missing EXCEPT FOR data.log")
        break

    if os.path.isfile('../coreFiles/newWords.log') == True:
        #print("newWords.log is ready!")
        pass

    else: 
        print("Sorry but one of the main files are missing, please check that you have data.log, error.log or newWords.log in the coreFiles folder!\n\nIf not, please create whatever is missing EXCEPT FOR data.log")
        break


    try:

        userInput = input ("> ")
    
        if userInput in greetings:
            random_greeting_responses = random.choice(greeting_responses)
            random_emot_question = random.choice(EmotionQuestion)
            #print(random_greeting_responses)
            print(random_emot_question)
                        
        elif userInput in questions:
            random_question_responses = random.choice(question_responses)
            print(random_question_responses)
                        
        elif userInput in time:
            print(timeResponse) 
                        
        elif userInput in humanEmotionG:
            EmotionalSupportPos = random.choice(HEGResponse) 
            print(EmotionalSupportPos) 
                        
        elif userInput in humanEmotionB:
            EmotionalSupportNeg = random.choice(HEBResponse) 
            print(EmotionalSupportNeg)
                        
        elif userInput in thanks:
            randomThanks = random.choice(thanksResponse)
            print(randomThanks)

        elif userInput in LawsOfRoboticsQ:
            LORA = random.choice(LORQA)
            print(LORA)

        elif userInput in Help:
            print("How can I help?")
            
        elif userInput == searchFor:
            print("Ok! what do you want to search for?")
            searchInput = input("(write query here) ")
            url='https://google.com/search?q='+searchInput
            webbrowser.open(url)
            print("Ok searching for: " + searchInput)
            
        elif userInput == "What do you do?":
            print("A simple way of thinking about it is that I am like Siri and Cortana. I am here to help monitor and assist in controlling your device!\nI can also help search for things on the internet!")

        elif userInput in LockMyPC:
            print("Ok! Locking the computer!")
            subprocess.call(lockPC)

        elif userInput in ShutdwnPC:
            print("Ok! Shutting down the computer!")
            subprocess.call(["shutdown", "-f", "-r", "-t", "10", "-c", 'Alice is shutting down the device'])

        elif userInput in RestartPC:
            print("Ok! Restarting the computer!")
            subprocess.call(["shutdown", "/r"])

        elif userInput in LogoutPC:
            print("Ok! Logging you out!")
            subprocess.call(["shutdown", "/l"])

        elif userInput in goodbye:
            print("Goodbye! Have a nice day :)")
            break

        elif userInput in open("../coreFiles/newWords.log", 'r'):
            import nmap

            with open("../coreFiles/newWords.log") as f, \
                nmap.nmap(f.fileno(), access=nmap.ACCESS_READ) as s:
                if s.find(userInput) != -1:
                    print(f"Does {userInput} mean: \"{s.find(userInput.strip(userInput + ' : It means '))}")
        else :
            print("Sorry, I don't know what that means...could you tell me, please?")
            learn = input("Define: ")
            if "It means " in learn:
                with open("../coreFiles/newWords.log", "w+") as f:
                    f.write(f'{userInput} : {learn}')
                f.close()
            else:
                print("Please have \"It means\" at the start of the sentence")

    except KeyboardInterrupt:
        import time
        print("\nOK! closing down!")
        time.sleep(2)
        exit(0)
