__author__ = 'Eric Ball'
import os
import sys
from TurtleCalc import turtle_calc


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def set_title(title):
    if os.name == "nt":
        os.system("title " + title)
    else:
        sys.stdout.write("\x1b]2;"+title+"\x07")

isRunning = True

while isRunning:

    clear_console()

    print("Eric's Python Scripts")
    print()
    print("====================")
    print("1: Turtle Calculator")
    print("0: Quit")
    print("====================")
    print()
    main_sel = input("Pick One: ")

    if main_sel == "1":
        clear_console()
        turtle_calc()
    elif main_sel == "0":
        isRunning = False
