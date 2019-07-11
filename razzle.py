##Welcome to Razzle, a task automater made by Asuna
import os
import random
import time
import socket
#creats and defines the variables for Socket to print them for later
hn = socket.gethostname()
ip = socket.gethostbyname(hn)
#this is the list for the "Good Morning" messages for printing when the program opens, mostly a printf if you would.
foo = ['Guten Morgen Asuna!', 'Bonjour Asuna!', 'Ohayou Asuna!']
#Remember that good morning variable well, no where going to randomly a word and print it
print(random.choice(foo))
time.sleep(2)
#Okay, now we print out the hostname and ip, I put the sleeps here case the machine is slow
print('Your current hostname is: ' + hn)
time.sleep(1)
print('Your current local IP is: ' + ip)
time.sleep(1)
#Now it gets fun, we're going to open a program
print('Let me open some stuff for you')
time.sleep(3)
#Basically this just opens a .exe found in the directory
os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
print('Opened: Chrome')
time.sleep(2)
#And again!
os.startfile('C:\Program Files\Microsoft Office\Root\Office16\OUTLOOK.EXE')
time.sleep(2)
print('Opened: Outlook')
time.sleep(2)
print('Finished!')