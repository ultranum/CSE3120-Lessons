'''
title: making dice
author: garrett
date created: 2019-03-14
'''
import random
class die:
    def __init__(self):
        self.sides = 6
        self.values = [1, 2, 3, 4, 5, 6]

    def getRollVal(self):
        return self.values[random.randrange(len(self.values))]

    def setNumSides(self, sides):
        self.sides = sides

    def getNumSides(self):
        return self.sides

    def setSideVal(self, size):
        templi = []
        for i in range(size):
            templi.append(int(input("value")))
        self.values = templi

die1 = die() # constructing object from class
die2 = die()

print(die1.getNumSides(), die2.getNumSides())

die1.setNumSides(8)
die2.setNumSides(4)

print(die1.getNumSides(), die2.getNumSides())

die2.setSideVal(die2.getNumSides())

print(die2.getRollVal())