from Card import Card
from Deck import Deck
from Hand import Hand

deck = Deck()
deck.shuffle()

n_players = 1
n_cards = 5

def deal(deck, hands, n_cards):
    for _ in range(n_cards):
        for hand in hands:
            hand.append(deck.next())

hands = []
for _ in range(n_players):
    hands.append(Hand([]))

deal(deck, hands, n_cards)

test = hands[0]
test.sort()

flush = list(set([x.suit for x in test.cards])) == 1
if flush:
    print('Flush possible!')

print(test)
print(test.value())

