'''
title: making dice
author: garrett
date created: 2019-03-14
'''

class die:
    import random
    def __init__(self, sides):
        self.sides = sides
        self.values = []
        self.setNumSides(sides)

    def getRollVal(self):
        return self.values[die.random.randrange(len(self.values))]

    def setNumSides(self, sides):
        self.sides = sides
        self.setSideVal(self.sides)

    def getNumSides(self):
        return self.sides

    def setSideVal(self, size):
        templi = []
        for i in range(size):
            templi.append(int(input("value")))
        self.values = templi

class player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.dice = [die(3), die(3), die(3), die(3)]

    def getScore(self):
        return self.score

    def calcScore(self):
        for i in range(len(self.dice)):
            self.score += self.dice[i].getRollVal()

garrett = player('garrett')
garrett.calcScore()
print(garrett.getScore())
#die1 = die(5) # constructing object from class
#print(die1.getRollVal())
'''
die2 = die()

print(die1.getNumSides(), die2.getNumSides())

# die1.setNumSides(8)
die2.setNumSides(4)

print(die1.getNumSides(), die2.getNumSides())

# die2.setSideVal(die2.getNumSides())

print(die2.getRollVal())
'''