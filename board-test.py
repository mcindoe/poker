from Card import Card
from Hand import Hand
from Deck import Deck
from Board import Board

test = Deck()
test.shuffle()

boards = []

for n in range(2):
    boards.append(Board(Hand(test.deal(5)), Hand(test.deal(5)), Hand(test.deal(3))))

boards[0].sort()
boards[1].sort()

print(boards[0])
print()
if boards[0].valid():
    print('Valid')
    print(f'Royalties: {boards[0].royalties()}')
else:
    print('Foul')

print()

print(boards[1])
print()
if boards[1].valid():
    print('Valid')
    print(f'Royalties: {boards[1].royalties()}')
else:
    print('Foul')

print('\nSummary:')
print(boards[0].compare(boards[1]))
