from modules.card import Card

def kicker_val(*args):
    '''Encodes a list of card values as a unique float, with two digits
    representing each value in the order of importance, using as many
    digits as required. Input is assumed to be ordered highest to lowest.

    Eg
    [10,5,4] -> 0.100504
    [14,12,5,2] -> 0.14120502

    Parameters:
    args - iterable of kicker values
    '''

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
    def __init__(self, *cards):
        # construction from an iterable of cards
        if type(cards[0]) is not Card:
            self.cards = cards[0]

        # construction from arguments, eg Hand(c1, c2, ...)
        else:
            self.cards = cards
    
    def __repr__(self):
        if not self.cards:
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

        return ret

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        yield from self.cards

    def __eq__(self, other):
        return abs(self.value() - other.value()) < (10**-12)
    
    def __lt__(self, other):
        if self == other:
            return False
        
        return self.value() < other.value()
    
    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        if self == other:
            return False

        return self.value() > other.value()
   
    def __ge__(self, other):
        return self == other or self > other

    def append(self, *cards):
        for card in cards:
            self.cards.append(card)

    def sort(self):
        self.cards = sorted(self.cards, key = lambda x: x.rank, reverse = True)

    def sort_by_suit(self):
        sorted_cards = []
        for suit in reversed(suits):
            suit_cards = [x for x in self if x.suit == suit]
            sorted_cards += sorted(suit_cards, key = lambda x: x.rank)

        self.cards = sorted_cards

    def get_counts(self):
        ranks = [x.rank for x in self]
        uniques = sorted(list(set(ranks)), reverse = True)
        counts = {}
        for val in uniques:
            counts[val] = len(list([x for x in ranks if x == val]))

        return counts

    def value(self):
        '''Assigns a float value to a hand to indicate strength.
        The int() part of the returned val represents hand strength
        category, using the following categories:
        8: Straight Flush
        7: Quads
        6: Full House
        5: Flush
        4: Straight
        3: Trips
        2: Two Pair
        1: One Pair
        0: High Card
        The values following the decimal point are kickers ranked
        from highest to lowest, each occupying 2 decimal places
        '''
        assert len(self) in [3,5]

        self.sort()

        if len(self) == 3:
            a = self.cards[0].rank
            b = self.cards[1].rank
            c = self.cards[2].rank
            
            # no pair
            if len(set([a,b,c])) == 3:
                return kicker_val(a,b,c)

            # one pair
            elif len(set([a,b,c])) == 2:
                if a == b: 
                    pair = a
                    other = c
                elif b == c:
                    pair = b
                    other = a
                else:
                    pair = a
                    other = b

                return 1 + kicker_val(pair, other)
            
            # trips
            else:
                return 3 + kicker_val(a)

        elif len(self) == 5:
            counts = self.get_counts()
            values = sorted(list(counts.keys()), reverse = True)
            uniques = sorted(list(set(values)), reverse = True)
            flush = len(set([x.suit for x in self])) == 1
            ace = 14 in values

            # check if a straight is possible
            straight = True
            
            if ace:
                remaining = set([x for x in values if x != 14])
                if remaining not in [set([2,3,4,5]), set([10,11,12,13])]:
                    straight = False
            else:
                for n in range(len(values)-1):
                    if values[n] - 1 != values[n+1]:
                        straight = False
                        break
            
            # Straight flush
            if flush and straight:
                if ace:
                    if 5 in values:
                        return 8 + kicker_val(5)
                    return 8 + kicker_val(14)
                
                return 8 + kicker_val(values[0])
          
            # Quads
            if len(uniques) == 2:
                for i, val in enumerate(uniques):
                    if counts[val] == 4:
                        quad = val
                        other = uniques[(i-1) * -1]
                        
                        return 7 + kicker_val(quad, other)

                # Full House
                for i, val in enumerate(uniques):
                    if counts[val] == 3:
                        trips = val
                        other = uniques[(i-1) * -1]

                        return 6 + kicker_val(trips, other)
           
            # Flush
            if flush:
                return 5 + kicker_val(values)

            # Straight
            if straight:
                if ace:
                    if 5 in values:
                        return 4 + kicker_val(5)
                    return 4 + kicker_val(14)
                
                return 4 + kicker_val(values[0])

            if len(uniques) <= 3:
                # Trips
                for val in uniques:
                    if counts[val] == 3:
                        others = [x for x in values if x != val]
                        return 3 + kicker_val(val, others)

                # Two pair
                for p1 in uniques:
                    if counts[p1] == 2:
                        remaining = [x for x in values if x != p1]
                        for p2 in remaining:
                            if counts[p2] == 2:
                                other = [x for x in remaining if x != p2]
                                return 2 + kicker_val(p1, p2, other)

            # One pair
            for val in uniques:
                if counts[val] == 2:
                    others = [x for x in values if x != val]
                    return 1 + kicker_val(val, others)

            # High card
            return kicker_val(values)

    def royalties(self):
        assert len(self) in [3,5]
        
        val = self.value()
        counts = self.get_counts()

        if len(self) == 3:
            # no pair
            if int(val) == 0:
                return 0
           
            # one pair
            if int(val) == 1:
                for x in counts:
                    if counts[x] == 2:
                        pair = x
                        break
                
                if pair < 6:
                    return 0
                
                return pair - 5
            
            # trips
            if int(val) == 3:
                trip_value = list(counts.keys())[0]
                return trip_value + 8
        
        if len(self) == 5:
            # worse than a straight
            if int(val) < 4:
                return 0
            
            # straight up to quads inclusive
            if int(val) < 8:
                return [2,4,6,10][int(val) - 4]

            # straight flush. distinguish royal from not royal
            if 14 in list(counts.keys()):
                return 25

            return 15

