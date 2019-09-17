suits = ['club', 'diamond', 'heart', 'spade']

class Card():
    def __init__(self, rank, suit = None):
        # allow construction from a string, e.g. Card('T','h') or Card('Th')
        if type(rank) is str:
            if suit is None:
                suit = rank[1]
                rank = rank[0]

            if rank not in ['2','3','4','5','6','7','8','9']:
                assert rank.upper() in ['T','J','Q','K','A']
                rank = 10 + ['T','J','Q','K','A'].index(rank.upper())
            else:
                rank = int(rank)

        assert rank in range(2, 15)

        # allow construction by first letter of suit
        if len(suit) == 1:
            assert suit.lower() in [x[0] for x in suits]
            suit = suits[[x[0] for x in suits].index(suit.lower())]

        assert suit in suits
        self.suit = suit
        self.rank = rank

    @staticmethod
    def from_value(val):
        '''Maps a value in [0, 51] onto a Card instance

        Parameters:
        val (int) - a number in [0,51]

        Returns:
        Card - 0 maps to 2c, 51 to As
        '''
        
        if type(val) is not int:
            raise TypeError('val must be an integer')

        if val not in range(52):
            raise ValueError('val must be in [0, 51]')

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
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit  


