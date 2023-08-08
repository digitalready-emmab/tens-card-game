from card import Card
import random


turn_number = 1
whose_turn = ' '
computer_calculate = False
player_calculate = False

def make_global():
    global turn_number
    global whose_turn
    global computer_calculate
    global player_calculate



class Player():
    def __init__(self,name,table,hand):
        self.name = name
        self.table = table
        self.hand = hand

class User(Player):
    pass

player = Player(input("What is your name? "), Card.new_deck()[0:5], [])
print(player.__dict__)

class Computer(Player):
    def __init__(self,name,table,hand):
        self.name = name
        self.table = table
        self.hand = hand
computer = Computer("Computer", Card.new_deck()[6:11], [])
print(computer.__dict__)

def turn_check():
    if turn_number % 2 == 0:
        whose_turn = 'player'
    else:
        whose_turn = 'computer'
    print(whose_turn)
    draw()
def turn_on_calculations():
    if whose_turn == 'computer':
        computer_calculate = True
    elif whose_turn == 'player':
        player_calculate = True

def draw():
    if whose_turn == 'computer':
        computer.hand.append(Card.new_deck()[1])
        print(computer.__dict__)
    else:
        player.hand.append(Card.new_deck()[1])
        print(player.__dict__)
    turn_number = turn_number + 1
    turn_check()
turn_check()