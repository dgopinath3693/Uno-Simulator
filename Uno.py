
import random

playing = True

#generates and returns deck of 108 cards of colors and numbers with repeats of everything
#except 0 per the game setup, and with 4 of each wild cards 
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
def DrawStartCards():
    num_cards = 7
    start_deck = []
    for x in range(num_cards):
        start_deck.append(total_deck.pop(x))
    return start_deck


#shows the player the current hand of cards
def ShowHand():
    print("Current hand: ", start_deck)


#allows a user to place down a card from the deck if matching the color/number/is a wild card
def PlaceCardDown():
    return 0

#takes a new card if player's cards do not match last card's color/number/not wild card
#or if other player puts down a +2 or +4
def AddNewCard():
    return 0

#skips/reverses players turn if either player puts down a skip or reverse card
def Skip():
    return 0


#panel of choices for the user to select
def commandSelect(choice):
    if choice == 1:
        PlaceCardDown()
    if choice == 2:
        AddNewCard()
    

while playing:  
    
    total_deck = BuildCardDeck()
    total_deck = ShuffleCardDeck(total_deck)
    start_deck = DrawStartCards()

    print("Welcome to Uno Simulator!")
    print("First, player 1 will go.") 
    ShowHand() 
    print("Player 1, please select what choice you would like to make: ")
    print("1: place down a card from deck")
    print("2: take a new card")
    choice = int(input("Which choice?"))
    commandSelect(choice)
