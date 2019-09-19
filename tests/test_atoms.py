import unittest

from ./card import Card
from deck import Deck
from hand import Hand

class TestCard(unittest.TestCase):

    def test_valid(self):
        with self.assertRaises(ValueError):
            Card.from_value(55)

        with self.assertRaises(TypeError):
            Card.from_value('str')

    def test_print(self):
        card = Card(10,'h')
        self.assertEqual(str(card), 'Th')


class TestDeck(unittest.TestCase):
    
    def setUp(self):
        self.deck = Deck()

    def test_valid(self):
        with self.assertRaises(TypeError):
            self.deck.deal(3.5)

        with self.assertRaises(TypeError):
            self.deck.deal('str')

    def test_deal(self):
        self.assertEqual(type(self.deck.next()), Card)

class TestHand(unittest.TestCase):

    def setUp(self):
        c1 = Card(2,'c')
        c2 = Card(3,'c')
        c3 = Card(4,'c')
        c4 = Card(5,'c')
        c5 = Card(6,'c')
        c6 = Card(9,'h')
        c7 = Card('A','s')
        
        self.hand1 = Hand(c1, c2, c3)
        self.hand2 = Hand(c2, c3, c4)
        self.hand3 = Hand(c2, c3, c4)

        self.hand4 = Hand(c1,c2,c3,c4,c5)
        self.hand5 = Hand(c1,c2,c3,c4,c7)
        self.hand6 = Hand(c7,c1,c2,c3,c4)
        self.hand7 = Hand(c3,c4,c5,c6,c7)
    
    def test_comparisons(self):
        self.assertLess(self.hand1, self.hand2)
        self.assertEqual(self.hand2, self.hand3)
        self.assertLessEqual(self.hand1, self.hand2)
        self.assertGreaterEqual(self.hand3, self.hand1)
        self.assertGreater(self.hand6, self.hand7)

    def test_values(self):
        self.assertGreater(self.hand4.value(), 8)

        self.assertGreater(self.hand6.value(), 4)
        self.assertLess(self.hand6.value(), 5)

        self.assertLess(self.hand7.value(), 1)


if __name__ == '__main__':
    unittest.main()
