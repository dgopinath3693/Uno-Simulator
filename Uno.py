
import random

playing = True

#generates and returns deck of 108 cards of colors and numbers with repeats of everything
#except 0 per the game setup, and with 4 of each wild cards 
def BuildCardDeck():
    card_deck = []
    card_colors = ["Red", "Green", "Blue", "Yellow"]
    card_values = [0,1,2,3,4,5,6,7,8,9, "Draw 2", "Draw 4", "Skip", "Reverse"]
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


#draws cards for start of game for player 1
def DrawStartCardsPlayer1():
    num_cards = 7
    start_deck_1 = []
    for x in range(num_cards):
        start_deck_1.append(total_deck.pop(x))
    return start_deck_1

#draws cards for start of game for player 2
def DrawStartCardsPlayer2():
    num_cards = 7
    start_deck_2 = []
    for x in range(num_cards):
        start_deck_2.append(total_deck.pop(x))
    return start_deck_2


#shows the player the current hand of cards
def ShowHand(start_deck):
    print("Current hand: ", start_deck)


#allows a user to place down a card from the deck if matching the color/number/is a wild card
def PlaceCardDown(last_card, card_to_play):
    if "Select Color" in card_to_play:
       card_to_play_parts = card_to_play
    else:
        last_card_parts = last_card.split()
        card_to_play_parts = card_to_play.split()

    #if the color matches
    if last_card_parts[0] == card_to_play_parts[0]:
        print("Color:", card_to_play_parts[0], ",", "Number:", card_to_play_parts[1])
    #if the number matches
    elif last_card_parts[1] == card_to_play_parts[1]:
         print("Color:", card_to_play_parts[0], ",", "Number:", card_to_play_parts[1])
    #if its a wild card 
    elif ["Select Color", "Select Color & Draw 4", "Draw 2", "Draw 4"] in card_to_play_parts:
        new_color = input("What color do you want to change to?")
        print("Color: " + new_color, "Also, next player draw cards!") 
    #if the card is none of the above
    else:
        print("This card is not eligible to be put down!")

#takes a new card if player's cards do not match last card's color/number/not wild card
#or if other player puts down a +2 or +4
def AddNewCard():
    #  if card_to_play == "Select Color & Draw 4":
            
    #     elif card_to_play == "Draw 2":
    #         finally
    #     elif card_to_play == "Draw 4":
        
    #     #select color
    #     else:
    #         card_to_play_parts = card_to_play
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
    playing = False
    

while playing:  
    
    total_deck = BuildCardDeck()
    total_deck = ShuffleCardDeck(total_deck)
    start_deck_1 = DrawStartCardsPlayer1()
    start_deck_2 = DrawStartCardsPlayer2()

    print("Welcome to Uno Simulator!")
    print("First, player 1 will go.") 
    ShowHand() 
    print("Player 1, please select what choice you would like to make: ")
    print("1: place down a card from deck")
    print("2: take a new card")
    choice = int(input("Which choice?"))
    commandSelect(choice)

    print("Now, player 2 will go.") 
    ShowHand() 
    print("Player 2, please select what choice you would like to make: ")
    print("1: place down a card from deck")
    print("2: take a new card")
    choice = int(input("Which choice?"))
    commandSelect(choice)
