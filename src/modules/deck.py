import itertools
import json
import random

from .card import Card
from .ofc_hand import OfcHand

class Deck():
    def __init__(self):
        self.cards = [Card.from_value(n) for n in range(52)]
        self.cards_dealt = 0

    def __str__(self):
        return json.dumps([str(card) for card in self.cards], indent = 2)

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        return iter(self.cards)

    def __getitem__(self, i):
        return self.cards[i]

    def shuffle(self):
        '''Collects remaining and dealt cards together, then shuffles'''
        random.shuffle(self.cards)

    def next(self):
        '''Returns the next card from the top of the deck; updates deck'''

        assert self.cards_dealt < 52, 'no cards leaft to deal'

        card = self.cards[self.cards_dealt]
        self.cards_dealt += 1
        return card

    def deal(self, n_cards):
        '''Deals n_cards cards, returns them as a tuple'''

        if type(n_cards) is not int:
            raise TypeError('n_cards must be an integer')

        assert n_cards <= 52 - self.cards_dealt, 'more cards requested then remaining'

        return (self[i] for i in range(self.cards_dealt, self.cards_dealt + n_cards))
    
    def remove(self, removed):
        '''Removes specified cards from a deck'''
        if type(removed) is OfcHand:
            self.remove(removed.cards)
            return

        for card in removed:
            assert card in self.cards, f'{str(card)} not found in deck'
            self.cards.remove(card)

    def possible_deals(self, n_cards):
        '''Returns all possible n_cards length deals'''
        remaining_values = [x.value() for x in self]
        value_combinations = list(set(itertools.combinations(remaining_values, n_cards)))

        possible_deals = []
        for comb in value_combinations:
            possible_deals.append([Card.from_value(x) for x in comb])

        return possible_deals
