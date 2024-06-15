import random # Shuffle the deck

# All lists
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}
suits = ('Hearts','Diamonds','Clubs','Spades')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

# Card class and properties
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank  = rank
        self.value = values[rank] # Getting the integer value of the rank using the values dictionary

    def __str__(self):
        return self.suit + " " + self.rank

# Creating a deck of 52 cards with the Card class
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create a card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    # Function to shuffle the deck
    def shuffle(self):
        random.shuffle(self.all_cards)

    # Function to draw cards from the deck to players
    def draw_card(self):
        return self.all_cards.pop()

# Player class
class Player:
    def __init__(self,name):
        self.name = name
        self.player_cards = [] # Player's cards

    # Function for the player to lay down a card
    def play_card(self):
        return self.player_cards.pop(0)

    # Function to add cards when the player takes them
    def add_card(self,new_cards):
        # If the player is taking cards as a list, we extend it
        if type(new_cards) == type([]):
            self.player_cards.extend(new_cards)

        else:
            # If the player is taking a single card, we append it
            self.player_cards.append(new_cards)


# Start of the game
def game():

    # Creating players
    player_one = Player("One")
    player_two = Player("Two")

    # Creating and shuffling the deck
    new_deck = Deck()
    new_deck.shuffle()

    # Distributing the shuffled deck evenly among the players
    for i in range(26):
        player_one.add_card(new_deck.draw_card())
        player_two.add_card(new_deck.draw_card())

    game_on = True
    round_number = 0
    while game_on:

        round_number += 1
        print(f"Round {round_number}")

        # If a player runs out of cards, the game ends
        if len(player_one.player_cards) == 0:
            print("Player one is out of cards")
            print("PLAYER TWO WINS!!!")
            game_on = False
            break

        if len(player_two.player_cards) == 0:
            print("Player two is out of cards")
            print("PLAYER ONE WINS!!!")
            game_on = False
            break

        # Cards laid down by the players
        player_one_cards = []
        player_one_cards.append(player_one.play_card())

        player_two_cards = []
        player_two_cards.append(player_two.play_card())

        # Control conditions
        war = True
        while war:

            # The player with the higher value card (the last card, i.e., -1 index) wins
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_card(player_one_cards)
                player_one.add_card(player_two_cards)
                war = False

            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_card(player_one_cards)
                player_two.add_card(player_two_cards)
                war = False

            # If it's a tie, initiate war
            else:
                print("WAR!!")

                # If a player cannot afford to put down 5 cards, they lose
                if len(player_one.player_cards) < 5:
                    print("Player one cannot wage war")
                    print("PLAYER TWO WINS!!")
                    game_on = False
                    break

                elif len(player_two.player_cards) < 5:
                    print("Player two cannot wage war")
                    print("PLAYER ONE WINS!!")
                    game_on = False
                    break

                # If a player can afford to put down 5 cards, they lay them down
                else:
                    for num in range(5):
                        player_one_cards.append(player_one.play_card())
                        player_two_cards.append(player_two.play_card())


game()
