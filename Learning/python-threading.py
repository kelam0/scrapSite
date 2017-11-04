# -*- coding: utf-8 -*-

import threading, time

print('Starting')

def takeANap():
    time.sleep(5)
    print('Wake up!')
    
threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('Ending')

threadObj2 = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj2.start()

print('Really Ending')


import subprocess

#start a program with no inputs
calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
# check if program is done
if calcProc.poll() == None:
    print('Not done yet')
else:
    print('Ended with exit code: ' + calcProc.poll())
    
#wait until calcProc is done before continuing with script. Will return exit code when done.
calcProc.wait()

#start a program with an input
noteProc = subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])

#run another python script from python
pythonProc = subprocess.Popen(['C:\\python34\\python.exe', 'hello.py'])

#open an item with default program
deftProc = subprocess.Popen(['start', 'hello.txt'], shell=True)