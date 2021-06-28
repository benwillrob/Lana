import os
from re import S
import time
from typing import AsyncGenerator
import pyfiglet

from pyfiglet import Figlet

age = 0

while int(age) < 17:

    os.system("cls")
    ascii_banner = pyfiglet.figlet_format("Hello.")
    print(ascii_banner)

    input()
    os.system('cls')

    ascii_banner = pyfiglet.figlet_format("Lana")

    print("I am \n"+ascii_banner+"your person assistent.")
    input()
    os.system("cls")

    ascii_banner = pyfiglet.figlet_format("First,")
    print(ascii_banner)
    age = input("I need to verify your age. \n \nAGE >>")

    if int(age) < 17:
        ascii_banner = pyfiglet.figlet_format("Sorry,")
        print(ascii_banner+ "your not old enough")

print("Congratulations!")