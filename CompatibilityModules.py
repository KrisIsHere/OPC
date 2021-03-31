import os
from sys import platform

def clearscreen():
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

def copy(origin, destination):
    if platform == "win32":
        os.system('copy' + str(origin) + " " + str(destination))
    else:
        os.system('cp -r' + str(origin) + " /" + str(destination))

def readfile():
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')
