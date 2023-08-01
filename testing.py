from card import Card
import random


turn_number = 1
whos_turn = ''
print(whos_turn)

class Player():
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

class User(Player):
    pass

player = Player(input("What is your name? "), Card.new_deck()[0:5])
print(player.__dict__)

class Computer(Player):
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
computer = Computer("Computer", Card.new_deck()[6:10])
print(computer.__dict__)

def player_turn():
    if turn_number % 2 == 0:
        whos_turn = 'player'
    else:
        whos_turn = 'computer'

