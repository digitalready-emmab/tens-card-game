# Ten Cards Game
# Names: Bernisha, Veronica, Stephanie, Emma, Joi
# Date: 7/27/2023

# Objective: Make a 10 cards game
# Main Function:

# import statements
from card import Card
import random

##BASIC EXPLANATION
# Check if Users deck and Users pick equals a multiple of 10
# Check if Computer deck and Computer pick  equals a multiple of 10
# If Users deck and users pick  does not equal multiple of 10, add +1 to their hand
# If Comp deck and comp pick not equal multiple of 10, add +1 to their hand
#If User deck and user pick DOES equal multiple of 10,  replace one user card from deck to user pick
#If Comp deck and Comp pick DOES equal multiple of 10,  replace one comp card from deck to comp pick
# Repeat pattern until deck=0.
# At the end of the game, the player (or computer) with the least amount of cards is the winner.
#When deck=0 check if user hand is greater than, less than or equal to computer
#Depending on whether it is greater, less, or equal to computer, it will print the result

### Pseudocode
#   import functions from card.py
#   import random
#   create Class Player
#       assign name and hand to player
#   initialize player's deck
#       give player 5 random cards
#   create Class Computer
#       assign name and hand to computer
#       give Computer 5 random cards from the deck using new_deck function
#   put the rest of the deck aside
#   player always goes first, drawing one card from the pile that we set aside.
#   add card to player's hand
#   check card1, card2, card3, card4, and card5
#   can any card in player's hand compute to a multiple of ten (% 10 == 0)
#   if yes:
#       put card down on top of computing card
#   if no:
#       card remains in player's hand
#   turn continues until there are no legal moves or the player has no cards in their hand
#   play continues until there are no more cards in the deck
#   winner is determined by least amount of cards in their hand

# Create a deck of random-numbered cards from 1-13
def deck_of_cards():
    return Card.new_deck()

# Create 5 random-numbered cards from 1-13
def your_cards():
    the_cards = Card.new_deck()
    the_cards[0:4]

# Display 5 random cards to Player and Computer
def show_cards():
    print (your_cards)

# Take a user's input to retrieve a card from the deck
def user_input():
    while True:
        user = input('Select a card that can create a multiple of 10: ' + deck_of_cards())
        if user.isnumeric():
            your_cards.pop(user)

        
# Allow Computer to retrieve a card from the deck    
def comp_turn():
    draw_deck= random.choice((deck_of_cards))
      
    print ('Computer chose: ' + draw_deck + 'from the deck!')
    

# Program your game here!
def tens_card_game():
    deck = Card.new_deck()
    print(deck)

# Code that runs when script is called from terminal
# ex: python my_card_game.py
turn_number = 1
whose_turn = ' '
computer_calculate = False
player_calculate = False

if __name__ == "__main__":
    tens_card_game()

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
computer = Computer("Computer", Card.new_deck()[6:11])
print(computer.__dict__)

def turn_check():
    if turn_number % 2 == 0:
        whose_turn = 'player'
    else:
        whose_turn = 'computer'
    print(whose_turn)
def turn_on_calculations():
    if whose_turn == 'computer':
        computer_calculate = True
    elif whose_turn == 'player':
        player_calculate = True

def draw():
    if whose_turn == 'computer':
        computer.hand.append(Card.new_deck()[1])
        print(computer.__dict__)

def calculate(a,s,m,d):
    if computer_calculate == True:
        pass
turn_check()
draw()