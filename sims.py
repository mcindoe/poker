from board import Board
from card import Card
from deck import Deck
from hand import Hand

deck = Deck()
deck.shuffle()

bottom = Hand(Card(2,'h'), Card(3,'S'), Card(4,'d'), Card(5,'h'), Card(6,'s'))
middle = Hand(Card('2c'), Card('Th'), Card('Ts'), Card('Qc'), Card('Qs'))
top = Hand(Card('Ac'), Card('3c'), Card('Tc'))

deck.remove(bottom)
deck.remove(middle)
deck.remove(top)

villain = Board(bottom, middle, top)

hero_bottom = Hand(Card('Ad'),Card('Kd'),Card('Qd'),Card('Jd'),Card('Td'))
hero_middle = Hand(Card('Ks'),Card('Kh'),Card('9s'),Card('8s'))
hero_top = Hand(Card('As'), Card('7s'))

hero = Board(hero_bottom, hero_middle, hero_top)

deck.remove(hero_bottom)
deck.remove(hero_middle)
deck.remove(hero_top)

print('Villain:')
print(villain)
print('')
print('Hero:')
print(hero)

print('\nDealt Cards:')
dealt = deck.deal(3)
print(Hand(*dealt))

class Summary():
    def __init__(self, board, summary):
        self.board = board
        self.summary = summary

    def __str__(self):
        return 'Board: \n' + str(self.board) + '\nSummary:' + str(self.summary)

def final_move(hero, villain, dealt):
    # get the empty slots in each row
    empty = {
        'top': 3 - len(hero.top),
        'middle': 5 - len(hero.middle),
        'bottom': 5 - len(hero.bottom)
    }

    # if one row has two empties
    if 2 in empty.values():
        # get the row with two empties 
        match = [x for x in empty if empty[x] == 2][0]
    
        # get a list of values of game to hero by discarding discard
        # and playing resulting two cards in the top row
        summaries = []
        for discard in dealt:
            remaining = [x for x in dealt if x is not discard]
            new_row = Hand(*(getattr(hero, match).cards + remaining))
            
            if match == 'top':
                new_board = Board(hero.bottom, hero.middle, new_row)
            elif match == 'middle':
                new_board = Board(hero.bottom, new_row, hero.top)
            else:
                new_board = Board(new_row, hero.middle, hero.top)

            summaries.append(Summary(new_board, new_board.compare(villain)))
        
        best_move = max(summaries, key = lambda x: x.summary)
        return best_move.board

    # otherwise two rows have one space, one row is full
    else:
        # get the one complete row
        full = [x for x in empty if empty[x] == 0][0]
        incomplete = [x for x in empty if empty[x] > 0]

        summaries = []
        for discard in dealt:
            remaining = [x for x in dealt if x is not discard]
            
            # consider implications of putting each of the remaining cards
            # in each of the remaining rows
            for card in remaining:
                other = [x for x in remaining if x is not card][0]

                new_0 = Hand(*(getattr(hero, incomplete[0]).cards + [card]))
                new_1 = Hand(*(getattr(hero, incomplete[1]).cards + [other]))
                
                new_board = Board()

                setattr(new_board, full, getattr(hero, full))
                setattr(new_board, incomplete[0], new_0)
                setattr(new_board, incomplete[1], new_1)

                summaries.append(Summary(new_board, new_board.compare(villain)))
        
        best_move = max(summaries, key = lambda x: x.summary)
        return best_move.board

best_move = final_move(hero, villain, dealt)

print('\nbest move:')
print(best_move)
