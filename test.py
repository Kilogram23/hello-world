import os
import json
import sys
import webbrowser as wb

userdata = {}


with open('userdata.txt') as f:
    teststring = f.read()

if os.path.getsize('userdata.txt') > 0:
    userdata = json.loads(teststring)

subject = {}

if os.path.getsize('userdata.txt') == 0: 
    option = '2'
else:
    option = input("Select whether you would like to: \n 1. Choose an existing user preset \n 2. Create a new user \n 3. Add link to existing user \n ")

if option == '1':
    User = input("Enter user of program here: ") 
    if User != None:
        study = input("Enter a program of study: ") 
        print(f"Welcome, {User}, to your personalized workspace for {study}!") 
        topic = f"{study}" 
        # wb.open('https://chat.openai.com/', new = 2)
        link = userdata[User][study]
        for i in range(len(link)):
            wb.open(link[i], new = 2)
                
if option == '2':
    User = input("Enter user of program here: ") 
    if User not in userdata:
        study = input("Enter a program of study: ")
        
        if len(userdata) == 0:
            topic = {study: []}
            userdata = {User: topic}
            links = True
            while (links == True):
                link = input("Please copy the link(s) you would like to add to your preset or type no to halt: ")
                if link == 'no':
                        break
                else:
                    topic[study].append(link)
    else: 
        print('User already found!')

if option == '3':
    User = input("Enter user of program here: ")
    if User in userdata:
        study = input("Enter a program of study: ")
        linktoadd = userdata[User][study]
        links = True
        while (links == True):
            link = input("Please copy the link(s) you would like to add to your preset or type no to halt: ")
            if link == 'no':
                    break
            else:
                linktoadd.append(link)

with open('userdata.txt', 'w') as convert_file:
     convert_file.write(json.dumps(userdata)) 

     # for topic in userdata:
         # convert_file.write('\n')
         # convert_file.write(json.dumps(userdata[topic]))