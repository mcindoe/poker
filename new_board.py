from Hand import Hand

class Board():
    def __init__(self, bottom, middle, top):
        self.bottom = bottom
        self.middle = middle
        self.top = top

    def __str__(self):
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

        return self.bottom.royalties() + 2 * self.middle.royalties() + self.top.royalties()

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

