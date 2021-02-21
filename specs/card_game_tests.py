import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Hearts", 10)
        self.card2 = Card("Spades", 1)
        self.cardGame = CardGame()
        self.cards = [self.card1, self.card2]


    def test_check_for_ace(self):
        self.assertEqual(True, self.cardGame.check_for_ace(self.card2))

    def test_highest_card(self):
        self.assertEqual(self.card1, self.cardGame.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 11", self.cardGame.cards_total(self.cards))


    
        
