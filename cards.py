
'''
title: 
author: garrett
date created: 2019-03-15
'''

class card:
    faces = {
        1 : "Ace",
        2 : "2",
        3 : "3",
        4 : "4",
        5 : "5",
        6 : "6",
        7 : "7",
        8 : "8",
        9 : "9",
        10 : "10",
        11 : "Jack",
        12 : "Queen",
        13 : "King"
    }
    suits = {
        0 : "Spades",
        1 : "Diamonds",
        2 : "Clubs",
        3 : "Hearts"
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.faces[self.value] + ' of ' + self.suits[self.suit]

class deck:
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range (1,14):
                self.cards.append(card(j,i))

    def getRandCard(self):
        from random import randrange
        return self.cards.pop(randrange(len(self.cards)))

    def getDeckSize(self):
        return (len(self.cards))

class player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name

    def addCard(self, obj): #Setter Method
        self.hand.append(obj)

    def getHand(self):
        tempLi = []
        for i in range(len(self.hand)):
            tempLi.append(str(self.hand[i]))
        strHand = ', '.join(tempLi)
        return self.name + "'s Hand contains the following cards: " + strHand
myDeck = deck()
player1 = player('num2')

# Interface
for i in range(52):
    player1.addCard(myDeck.getRandCard())

print(player1)
print(myDeck.getDeckSize())
print(player1.getHand())