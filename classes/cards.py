# card class
class Card:
    # initializes cards
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # outputs full card name as string
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    # used for base game
    def short_str(self):
        suit_symbols = {
            "Clubs": "♣",
            "Diamonds": "♦",
            "Hearts": "♥",
            "Spades": "♠"
        }
        return f"{self.rank[0]}{suit_symbols[self.suit]}"