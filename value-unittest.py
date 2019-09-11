from Card import Card
from Hand import Hand

c1 = Card(3,'h')
c2 = Card(3,'d')
c3 = Card(3,'c')
c4 = Card(3,'s')

c5 = Card(4,'h')
c6 = Card(4,'d')

c7 = Card(5,'h')
c8 = Card(6,'h')
c9 = Card(7,'h')
c10 = Card(9, 'h')

c11 = Card(14, 'h')
c12 = Card(2, 'h')

hands = [
    Hand([c1, c6, c7, c8, c10]),
    Hand([c1, c2, c7, c8, c9]),
    Hand([c1, c2, c5, c6, c9]),
    Hand([c1, c2, c3, c6, c9]),
    Hand([c1, c6, c7, c8, c9]),
    Hand([c1, c5, c7, c8, c10]),
    Hand([c1, c2, c3, c5, c6]),
    Hand([c1, c2, c3, c4, c10]),
    Hand([c1, c5, c7, c8, c9]),

    Hand([c11, c12, c2, c5, c7]),
    Hand([c11, c12, c1, c5, c7]),
]

for hand in hands:
    hand.sort()
    print(hand)
    print(hand.value())
    print()
