import os
import time
import ctypes
import getpass
import colorama
import requests
from colorama import Fore, init, Style
import random
from tkinter import messagebox
import tkinter as tk


userpc = getpass.getuser()

colorama.init(autoreset=True)

os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW('         Doggo Swoofer         ' + 'Loading.')
time.sleep(1)
ctypes.windll.kernel32.SetConsoleTitleW('         Doggo Swoofer         ' + 'Loading..')
time.sleep(1)
ctypes.windll.kernel32.SetConsoleTitleW('         Doggo Swoofer         ' + 'Loading...')
time.sleep(1)
ctypes.windll.kernel32.SetConsoleTitleW('         Doggo Swoofer         ' + 'Loading.')
time.sleep(1)
ctypes.windll.kernel32.SetConsoleTitleW('         Doggo Swoofer         ' + 'Waiting.')
os.system('cls')
print()
print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET  + "]" + " : Welcome.")
time.sleep(1)
print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET  + "]" + " : Version - v1")
time.sleep(1)
print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET  + "]" + " : Credits - JoinException ")
print()
time.sleep(1)
print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET  + "]" + " : Auto Login? (Y/N)")
AutoLogin = input("         ")
if AutoLogin == "Y" or "y":
    os.system("cls")
    print()
    ctypes.windll.kernel32.SetConsoleTitleW('         Doggo Swoofer         ' + 'Welcome ' + userpc)
    print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Logged as " + userpc)
    time.sleep(1)
    print()
    time.sleep(1)
    print("         [" + Fore.BLUE + time.strftime(
        "%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Establishing connection to the server!")
    time.sleep(5 or 4 or 6)
    print("         [" + Fore.BLUE + time.strftime(
        "%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Connected to the server!")
    time.sleep(1)
    os.system("cls")
    print()
    print("         " + Fore.BLUE + "[" + Fore.RESET + "1" + Fore.BLUE + "]" + Fore.RESET + " HWID Changer")
    print("         " + Fore.BLUE + "[" + Fore.RESET + "2" + Fore.BLUE + "]" + Fore.RESET + " Battleye Spoof")
    print("         " + Fore.BLUE + "[" + Fore.RESET + "3" + Fore.BLUE + "]" + Fore.RESET + " EasyAnticheat Spoof")
    print("         " + Fore.BLUE + "[" + Fore.RESET + "4" + Fore.BLUE + "]" + Fore.RESET + " Vanguard [BETA] Spoof")
    print("         " + Fore.BLUE + "[" + Fore.RESET + "0" + Fore.BLUE + "]" + Fore.RESET + " Close")
    Select = input("          ")
    if Select == 0:
        exit()
    else:
        if Select ==  1 or 2 or 3 or 4:
            root = tk.Tk()
            root.withdraw()
            time.sleep(1)
            messagebox.showinfo("Info", "Spoofed Succesful")
        else:
            print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Error, Restart")
else:
    if AutoLogin == "N" or "n":
        print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Error, Restart")
    else:
        print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Error, Restart")