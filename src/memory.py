import os
import sys
import json

def coreFileCheck():
        dbFile = './data.txt'
        checkFile = os.path.isfile(dbFile)

        """ 
        checking if the data file is there and has UserData in it,
        otherwise ask for name
        """

        if checkFile == True:
                with open(dbFile) as database:
                        data = json.load(database)
                        for usr in data['UserData']:
                                SIGNATURE1 = "Welcome back "+usr['name']+"!"+" What do you need"
                                print(SIGNATURE1)
        else:
                SIGNATURE2 = input("Hi there! I am Alice! Your personal assistant! In order to continue, could you give me a name to call you by? This can be real or fake: ")
                data = {}
                data['UserData'] = []
                data['UserData'].append({
                        'name': SIGNATURE2
                })
                with open(dbFile, 'w') as outfile:
                        json.dump(data, outfile)
                
                with open(dbFile) as db:
                    data = json.load(db)
                    for usr in data['UserData']:
                        SIG3 = f"Hi there,{usr['name']}! How can I help you?"
                        print(SIG3)