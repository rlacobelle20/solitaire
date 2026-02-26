# deck class
import classes.cards as cards
class Deck:
    # initializes deck using card class
    # NOTE: this is a standard 52-card deck -- does not including jokers as they are not used in solitaire
    def __init__(self):
        self.cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(cards.Card(suit, rank))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
