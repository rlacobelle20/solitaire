# implements solitaire and its rules
import classes.deck as deck
class Solitaire:
    def __init__(self):
        self.deck = deck.Deck()
        self.deck.shuffle() # immediately shuffles for new deck

        # needs 7 piles of card to start game
        self.piles = [[] for _ in range(7)] # creates 7 empty piles
        for i in range(7):
            for j in range(i):
                self.piles[i].append(self.deck.deal_card())

        # needs separate deck for draw and discard piles
        self.draw_pile = self.deck.cards # remaining cards become draw pile
        self.discard_pile = [] # empty discard pile

        # needs to create foundation piles for each suit
        self.foundation_piles = {
            "Clubs": [],
            "Diamonds": [],
            "Hearts": [],
            "Spades": []
        }
    
    # needs to implement rules for card movemebt, draw pile, and win conditions
    # need to represent hidden cards in piles and only show top card
    def start_game(self):
        pass

    # checks stack to see if move is valid
    def check_stack(self, card1, card2):
        # checks if card1 can be placed on card2 based on solitaire rules
        # card1 must be one rank lower than card2 and of opposite color
        rank_order = ["Ace","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        if rank_order.index(card1.rank) != rank_order.index(card2.rank) - 1:
            return False
        red_suits = ["Hearts", "Diamonds"]
        black_suits = ["Clubs", "Spades"]
        if (card1.suit and card2.suit) in red_suits or (card1.suit and card2.suit) in black_suits:
            return False
        return True
    
    # all foundations must be filled in with 13 cards to win
    def check_win(self):
        for suit in self.foundation_piles:
            if len(self.foundation_piles[suit]) != 13:
                return False
        return True

        