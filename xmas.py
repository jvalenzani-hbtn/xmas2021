#!/usr/bin/python3
from random import randint
from time import sleep

def esc(code):
    return f'\033[{code}m'

def loadTree(file):
    tree = []
    with open(file, 'r') as f:
        tree = f.readlines()
    return tree

def switchChar(char):
    color = randint(90,97) if randint(0,1) == 1 else randint(30, 39)
    switcher = {
        'X': f'{esc(93)}{char}{esc(0)}',
        '*': f'{esc(32)}{char}{esc(0)}',
        '$': f'{esc(color)}0{esc(0)}',
    }
    if char in switcher:
        return switcher[char]
    else:
        return f'{esc(0)}{char}'

def colorPrint(tree):
    for l in tree:
        for ch in l:
            print(switchChar(ch), end='')
    print()

def clearScreen():
    print(f'\033[2J')

def goto00():
    print(f'\033[0;0H')

def hideCursor():
    print(f'\033[?25l')

def showCursor():
    print(f'\033[?25h')

if __name__ == '__main__':
    tree = loadTree('tree.txt')
    clearScreen()
    hideCursor()
    while(1 == 1):
        try:
            goto00()
            colorPrint(tree)
            sleep(0.5)
        except KeyboardInterrupt:
            showCursor()
            exit()