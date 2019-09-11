import json
import random

from Card import Card

class Deck():
    def __init__(self):
        self.cards = [Card.from_value(n) for n in range(52)]
        self.discards = []

    def __str__(self):
        return json.dumps([str(card) for card in self.cards], indent = 2)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        self.cards = self.cards + self.discards
        self.discards = []
        random.shuffle(self.cards)

    def next(self):
        card = self.cards.pop(0)
        self.discards.append(card)
        return card
    
    def deal(self, n_cards):
        ret = []
        for _ in range(n_cards):
            ret.append(self.next())
        return ret

