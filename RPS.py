'''
title: RPS
author: garrett
date created: 2019-03-20
'''
'''
import random
class hands:

    symbols = {
        0 : "Rock",
        1 : "Paper",
        2 : "Scissors"
    }

    conditions = {
        1 : "win",
        2 : "loss",
        3 : "tie"
    }
    def __init__(self, choice):
        self.choice = choice

    def defeats(self):
        if self.symbols[0]

class player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def getChoice(self,choice):
        return hands.symbols[choice]

    def getScore(self):
        exit

a = player('a')
b = player('b')
print(a.getChoice(1))
print(b.getChoice(random.randrange(len(hands.symbols))))
'''

class thing:
    def __init__(self, name):
        selection = ['Rock', 'Paper', 'Scissors']
        beats = {
            'Rock': 'Scissors',
            'Paper': 'Rock',
            'Scissors': 'Paper'
        }
        self.name = selection[name]
        self.defeats = beats[self.name]

    def getName(self):
        return self.name

    def getDefeat(self):
        return self.defeats

    def __str__(self):
        return self.name

class player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = None

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def getChoice(self):
        return self.choice

    def setChoice(self, choice):
        self.choice = thing(choice)

    def addScore(self):
        self.score += 1

# Functions

def menu():
    print('''
    1) Rock
    2) Paper
    3) Scissors
    4) Quit
        ''')
    choice = int(input('> '))
    choice -= 1
    return choice

def findWinner(play1, play2):
    if play1.getChoice().getName() == play2.getChoice().getName():
        return 0
    elif play1.getChoice().getDefeat() == play2.getChoice().getName():
        play1.addScore()
        return 1
    elif play1.getChoice().getName() == play2.getChoice().getDefeat():
        play2.addScore()
        return 2

def displayWinner(result, play1, play2):
    # print player choices
    print('%s chose %s.' %(play1.getName(), play1.getChoice()))
    # print(f'{play1.getName()} chose {play1.getChoice()}')
    print('%s chose %s.' % (play2.getName(), play2.getChoice()))
    # print result
    if result == 0:
        print('tie')
    elif result == 1:
        print(play1.getName() + ' wins')
    elif result == 2:
        print(play2.getName() + ' wins')
    print('%s : %s | %s : %s' %(play1.getName(), play1.getScore(), play2.getName(), play2.getScore()))
### Main Code Starts

import random

player1 = player('n')
computer = player('comp')

running = True
while running:
    select = menu()
    if select == 3:
        running = False
    else:
        player1.setChoice(select)
        computer.setChoice(random.randrange(3))

        win = findWinner(player1, computer)
        displayWinner(win, player1, computer)