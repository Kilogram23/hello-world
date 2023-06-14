import os
import numpy as np
import sys
import webbrowser as wb

User = input("Enter user of program here: ") 

if (User == "Rushi" or "Akanksha"):
    print(f"Welcome, {User}, to your personalized workspace!")  
    wb.open('https://chat.openai.com/', new = 2)

