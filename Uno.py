
import random

#generates and returns deck of 108 cards of colors and numbers with repeats of everything
#except 0 per the game setup
def BuildCardDeck():
    card_deck = []
    card_colors = ["Red", "Green", "Blue", "Yellow"]
    card_values = [0,1,2,3,4,5,6,7,8,9, "Draw 2", "Skip", "Reverse"]
    card_wilds = ["Select Color", "Select Color & Draw 4"]
    for color in card_colors:
        for value in card_values:
            card_value = "{} {}". format(color, value)
            card_deck.append(card_value)
            if value != 0:
                card_deck.append(card_value)
    for i in range(4):
        card_deck.append(card_wilds[0])
        card_deck.append(card_wilds[1])
    
    return card_deck


#manually shuffles deck and swaps position with random card position 
def ShuffleCardDeck(deck):
    for card_position in range(len(deck)):
        random_position = random.randint(0,107)
        temp = deck[card_position]
        deck[card_position] = deck[random_position]
        deck[random_position] = temp
    return deck


#draws cards for start of game
def drawCards(num_cards):
    #test
    



deckz = BuildCardDeck()
deckz = ShuffleCardDeck(deckz)
print(deckz)