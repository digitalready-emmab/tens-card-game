# tens-card-game

# Ten Cards Game
# Names: Bernisha, Veronica, Stephanie, Emma, Joi
# Date: 7/27/2023

# Objective: Make a 10 cards game
# Main Function:

# Create a deck of random-numbered cards from 1-13
def deck_of_cards():
    return list(range(1,53))
# Create 5 random-numbered cards from 1-13
def your_cards():
    return list(range(6))
# Display 5 random cards to Player and Computer
# Take a user's input to retrieve a card from the deck
# Allow Computer to retrieve a card from the deck
# Check if Users hand and Users pick from deck equals a multiple of 10
# Check if Computer hand and Computer pick from deck equals a multiple of 10
# If Users hand and users pick from deck does not equal multiple of 10, add +1 to their hand
# If Comp hand and comp pick from deck not equal multiple of 10, add +1 to their hand
#If User hand and user pick DOES equal multiple of 10 
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