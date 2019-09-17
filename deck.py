import json
import random

from card import Card
from hand import Hand

class Deck():
    def __init__(self):
        self.cards = [Card.from_value(n) for n in range(52)]
        self.dealt = []

    def __str__(self):
        return json.dumps([str(card) for card in self.cards], indent = 2)

    def __len__(self):
        return len(self.cards)

    def collect_dealt(self):
        '''Adds the dealt cards to the bottom of the deck'''

        self.cards = self.cards + self.dealt
        self.dealt = []

    def shuffle(self):
        '''Collects remaining and dealt cards together, then shuffles'''

        self.collect_dealt()
        random.shuffle(self.cards)

    def next(self):
        '''Returns the next card from the top of the deck; updates deck'''

        assert len(self) > 0, 'no cards left to deal'

        card = self.cards.pop(0)
        self.dealt.append(card)
        return card
    
    def deal(self, n_cards):
        '''Deals n_cards cards, returns them as a tuple'''

        if type(n_cards) is not int:
            raise TypeError('n_cards must be an integer')

        assert n_cards <= len(self), 'more cards requested than remaining'

        ret = []
        for _ in range(n_cards):
            ret.append(self.next())
        return tuple(ret)
    
    def remove(self, removed):
        '''Removes specified cards from a deck, saving them as dealt cards'''
        if type(removed) is Hand:
            self.remove(removed.cards)
            return

        for card in removed:
            if card in self.cards:
                self.dealt.append(card)
                self.cards.remove(card)
            else:
                raise AssertionError(f'{str(card)} not found in deck')


