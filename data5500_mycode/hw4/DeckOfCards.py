




# DeckOfCards.py

import random

class Card():
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

class DeckOfCards:
    def __init__(self, deck=[]):
        self.deck = deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def print_deck(self):
        for card in self.deck:
            print(card.face, "of", card.suit)


suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

cards = []
for suit in suits:
    for face in faces:
        cards.append(Card(suit, face))

deck = DeckOfCards(cards)

deck.print_deck()
deck.shuffle_deck()
print("-------------")
deck.print_deck()

#     def __str__(self):
#         return f"{self.value} of {self.suit}"

#     def value(self):
#         if self.value in ['Jack', 'Queen', 'King']:
#             return 10
#         elif self.value == 'Ace':
#             return 11  # Handle Ace as 11 initially
#         else:
#             return int(self.value)

# class DeckOfCards:
#     def __init__(self):
#         self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
#         self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
#         self.cards = [Card(value, suit) for suit in self.suits for value in self.values]

#     def shuffle_deck(self):
#         random.shuffle(self.cards)

#     def get_card(self):
#         return self.cards.pop(0)

#     def __str__(self):
#         return ', '.join(str(card) for card in self.cards)
