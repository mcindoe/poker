suits = ['club', 'diamond', 'heart', 'spade']

class Card():
    def __init__(self, rank, suit):
        assert rank in range(2, 15)

        # allow construction by first letter of suit
        if len(suit) == 1:
            assert suit in [x[0] for x in suits]
            suit = suits[[x[0] for x in suits].index(suit)]

        assert suit in suits
        self.suit = suit
        self.rank = rank

    @staticmethod
    def from_value(val):
        '''Maps a value in [0, 51] onto a Card instance'''

        suit = suits[int(val/13)]
        rank = val % 13 + 2
        return Card(rank, suit)

    def __repr__(self):
        return f"Card({self.rank},'{self.suit[0]}')"

    def __str__(self):
        if self.rank >= 10:
            card_name = ['T', 'J', 'Q', 'K', 'A'][self.rank - 10]
        else:
            card_name = self.rank

        return f'{card_name}{self.suit[0]}'


