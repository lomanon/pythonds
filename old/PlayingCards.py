import random

numbers = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

suits = ["Clubs","Diamonds","Hearts","Spades"]

class PlayingCard:
    def __init__(self,suit,number):
        if suit in suits:
            self.suit = suit
        else:
            raise RuntimeError("Please make sure suit is H, C, D,or S")
        if number in numbers:
            self.number = number
        else:
            raise RuntimeError("Please make sure number is either 2-10 or A,K,Q,J")

    def getValue(self):
        return self.number

    def __str__(self):
        return "{} - {}".format(self.number, self.suit)

    def __repr__(self):
        return "{} - {}".format(self.number, self.suit)


class DeckOfCards:
    def __init__(self):
        self.cards = [PlayingCard(suit,number) for suit in suits for number in numbers]

    def getLength(self):
        return len(self.cards)


    def shuffle(self):
        random.shuffle(self.cards)

    def dealCards(self,num_cards):
        dealt_cards = [self.cards.pop() for i in range(1, num_cards+1)]
        return dealt_cards

    def addCard(self,card):
        self.cards.append(card)

tp_deck = DeckOfCards()
tp_deck.shuffle()

player_dict = {}

# num_players = int(input("Please input number of players --> "))
num_players = 4
# Initialise player decks
for i in range(1, num_players + 1):
    player_dict[i] = {"points": 0, "cards": tp_deck.dealCards(int(52 / num_players))}

while True:
    # Each player takes a turn
    cards_this_turn = []
    for player in player_dict.keys():
        card_value = player_dict[player]["cards"].pop().getValue()
        cards_this_turn.append(card_value)

    card_indexes = [numbers.index(item) for item in cards_this_turn]
    winning_player = card_indexes.index(max(card_indexes)) + 1

    player_dict[winning_player]["points"] += 1

    # print("{} - {} wins".format(cards_this_turn,winning_player))

    if len(player_dict[player]["cards"]) == 0:
        for key in player_dict.keys():
            print("{} - {} points".format(key,player_dict[key]["points"]))
        break


