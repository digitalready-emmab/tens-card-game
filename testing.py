from card import Card
import random
import time


def main():
    global turn_number, whose_turn, computer_calculate, player_calculate, hand_index, table_index, deck
    turn_number = 0
    whose_turn = ' '
    computer_calculate = False
    player_calculate = False
    hand_index = 0
    table_index = 0
    deck = 52
main()

def lose_cards(decrease):
    global deck
    deck = deck - decrease
lose_cards(10)



class Player():
    def __init__(self,name,table,hand):
        self.name = name
        self.table = table
        self.hand = hand
player = Player(input("What is your name? "), Card.new_deck()[0:5], [])

class User(Player):
    pass

class Computer(Player):
    def __init__(self,name,table,hand):
        self.name = name
        self.table = table
        self.hand = hand
computer = Computer("Computer", Card.new_deck()[6:11], [])

def turn_check():
    global turn_number, whose_turn
    if turn_number % 2 == 0:
        whose_turn = 'player'
        print("It is your turn.")
    else:
        whose_turn = 'computer'
        print("It is the computer's turn.")
    time.sleep(2)
def turn_on_calculations():
    global computer_calculate, player_calculate
    if whose_turn == 'computer':
        computer_calculate = True
        player_calculate = False
    elif whose_turn == 'player':
        player_calculate = True
        computer_calculate = False
    calculate()
def draw():
    global turn_number, deck
    if whose_turn == 'computer':
        computer.hand.append(Card.new_deck()[1])
        lose_cards(1)
        print(computer.hand)
    else:
        player.hand.append(Card.new_deck()[1])
        lose_cards(1)
        print(player.hand)
    turn_number = turn_number + 1

def begin_turn(table):
    turn_check()
    draw()
    turn_on_calculations()
    print(table.table)

def calculate():
    global computer_calculate, player_calculate, table_index, hand_index
    table_index = 0
    hand_index = 0
    card_played = False
    if computer_calculate == True:
        for card in computer.hand:
            for table_card in computer.table:
                if (card.value * table_card.value) % 10 == 0:
                    print(computer.table[table_index])
                    print(computer.hand[hand_index])
                    computer.table[table_index] = computer.hand[hand_index]
                    computer.hand.remove(card)
                    card_played = True
                    print("The computer played their card. They played " + str(card.value) + " on " + str(table_card.value) + " because " + str(card.value) + " multiplied by " + str(table_card.value) + " equals " + str((card.value * table_card.value)) + ", which is a multiple of ten.")
                    time.sleep(5)
                elif (card.value / table_card.value) % 10 == 0:
                    print(computer.table[table_index])
                    print(computer.hand[hand_index])
                    computer.table[table_index] = computer.hand[hand_index]
                    computer.hand.remove(card)
                    card_played = True
                    print("The computer played their card. They played " + str(card.value) + " on " + str(table_card.value) + " because " + str(card.value) + " divided by " + str(table_card.value) + " equals " + str((card.value / table_card.value)) + ", which is a multiple of ten.")
                    time.sleep(5)
                elif (card.value + table_card.value) % 10 == 0:
                    print(computer.table[table_index])
                    print(computer.hand[hand_index])
                    computer.table[table_index] = computer.hand[hand_index]
                    computer.hand.remove(card)
                    card_played = True
                    print("The computer played their card. They played " + str(card.value) + " on " + str(table_card.value) + " because " + str(card.value) + " added to " + str(table_card.value) + " equals " + str((card.value + table_card.value)) + ", which is a multiple of ten.")
                    time.sleep(5)
                elif (card.value - table_card.value) % 10 == 0:
                    print(computer.table[table_index])
                    print(computer.hand[hand_index])
                    computer.table[table_index] = computer.hand[hand_index]
                    computer.hand.remove(card)
                    card_played = True
                    print("The computer played their card. They played " + str(card.value) + " on " + str(table_card.value) + " because the difference of " + str(card.value) + " and " + str(table_card.value) + " equals " + str(abs(card.value - table_card.value)) + ", which is a multiple of ten.")
                    time.sleep(3)
        if card_played == False:
            print("The computer could not find a legal move. The card has been added to its hand.")
    if player_calculate == True:
        print(player.table)
        print(player.hand)
        player_turn()
        time.sleep(3)

def player_turn():
    global hand_index
    change = input("Where will you play your card? Choose a number from 1 to 5. If you decide you can't play it, pick 0. ")
    for card in player.hand:
        if int(change) == 0:
            print("This card has been added to your hand.")
        else:
            for table_card in player.table:
                if table_card == player.table[int(change)-1]:
                    if (card.value * table_card.value) % 10 == 0:
                        player.table[int(change)-1] = player.hand[hand_index]
                        player.hand.remove(card)
                        print("You played your card. You played " + str(card.value) + " on " + str(table_card.value) + " because " + str(card.value) + " multiplied by " + str(table_card.value) + " equals " + str((card.value * table_card.value)) + ", which is a multiple of ten.")
                    elif (card.value / table_card.value) % 10 == 0:
                        player.table[int(change)-1] = player.hand[hand_index]
                        player.hand.remove(card)
                        print("You played your card. You played " + str(card.value) + " on " + str(table_card.value) + " because " + str(card.value) + " divided by " + str(table_card.value) + " equals " + str((card.value / table_card.value)) + ", which is a multiple of ten.")
                    elif (card.value + table_card.value) % 10 == 0:
                        player.table[int(change)-1] = player.hand[hand_index]
                        player.hand.remove(card)
                        print("You played your card. You played " + str(card.value) + " on " + str(table_card.value) + " because " + str(card.value) + " plus " + str(table_card.value) + " equals " + str((card.value + table_card.value)) + ", which is a multiple of ten.")
                    elif (card.value - table_card.value) % 10 == 0:
                        player.table[int(change)-1] = player.hand[hand_index]
                        player.hand.remove(card)
                        print("You played your card. You played " + str(card.value) + " on " + str(table_card.value) + " because the difference of " + str(card.value) + " and " + str(table_card.value) + " equals " + str(abs(card.value - table_card.value)) + ", which is a multiple of ten.")
                    else:
                        print("That's an illegal move. Try again.")
                        time.sleep(1.5)
                        player_turn()

## run functions

def deck_function():
    global deck
    while deck > 1:
        begin_turn(computer)
        begin_turn(player)
deck_function()