from Card import Card
from Deck import Deck

def kicker_val(*args):
    # Flatten input into one list
    list_of_lists = []
    for x in args:
        if type(x) != list:
            list_of_lists.append([x])
        else:
            list_of_lists.append(x)

    flat = [item for sublist in list_of_lists for item in sublist]

    ret = 0
    for i, x in enumerate(flat):
        ret += x * 10**(-2*(i+1))

    return round(ret, 2*len(flat))

class Hand():
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        if self.cards == []:
            return 'Hand([])'

        ret = 'Hand(['
        for card in self:
            ret += f"Card({card.rank},'{card.suit[0]}')"
            if card is not self.cards[-1]:
                ret += ', '
            else:
                ret += '])'

        return ret

    def __str__(self):
        if self.cards == []:
            return '[]'

        ret = '['
        for card in self:
            ret += str(card)
            if card is not self.cards[-1]:
                ret += ', '
            else:
                ret += ']'


