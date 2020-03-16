'''
Provides a class to represent entire OFC board, i.e. top, middle
and bottom hands.
'''


class OfcBoard():
    def __init__(self, bottom = None, middle = None, top = None):
        self.bottom = bottom
        self.middle = middle
        self.top = top

    def __str__(self):
        self.sort()

        ret = ''
        for x in [self.top, self.middle, self.bottom]:
            ret += ' '.join([str(card) for card in x])
            if x is not self.bottom:
                ret += '\n'

        return ret

    def __repr__(self):
        return f'Board({repr(self.bottom)}, {repr(self.middle)}, {repr(self.top)})'

    def sort(self):
        self.top.sort()
        self.middle.sort()
        self.bottom.sort()

    def valid(self):
        return self.top <= self.middle and self.middle <= self.bottom

    def royalties(self):
        if not self.valid():
            return 0

        return self.bottom.royalties(middle = False) + \
                self.middle.royalties(middle = True) + \
                self.top.royalties()

    def scoop(self, other):
        '''Checks a board for scoopage against another board
        Returns
         0 - no scoop
         1 - self scoops other
        -1 - other scoops self
        '''
        
        if self.valid():
            if not other.valid():
                return 1
            else:
                if self.bottom > other.bottom and self.middle > other.middle and self.top > other.top:
                    return 1
                if self.bottom < other.bottom and self.middle < other.middle and self.top < other.top:
                    return -1
                return 0

        if not other.valid():
            return 0
        return -1

    def compare(self, other):
        '''Compares each row against other's row and returns the
        number of points self scores against other'''

        total = 0
        scoop_bonus = 3
        
        if self.valid():
            # self valid, other invalid
            if not other.valid():
                return 3 + scoop_bonus + self.royalties()
            # both valid
            total = self.royalties() - other.royalties()
            for x in ['bottom', 'middle', 'top']:
                if getattr(self, x) > getattr(other, x):
                    total += 1
                elif getattr(self, x) < getattr(other, x):
                    total -= 1

            return total + self.scoop(other) * scoop_bonus
        
        # self invalid, other valid
        if other.valid():
            return -3 - scoop_bonus - other.royalties()
        
        # both invalid
        return 0
