import os
import json
import sys
import webbrowser as wb

User = input("Enter user of program here: ") 
userdata = {}

if (User == "Rushi" or "Akanksha"):
    print(f"Welcome, {User}, to your personalized workspace!")  
    wb.open('https://chat.openai.com/', new = 2)
    userdata[User] = 'https://chat.openai.com/'



with open('userdata.txt', 'w') as convert_file:
     convert_file.write(json.dumps(userdata))