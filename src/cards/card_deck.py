"""
Module defining classes for a deck of cards that are not tied to any card game.
"""
# Third-party imports

# Global imports

# Local imports
from .cards import (
    CardSuit,
    CardLabel,
    CardColor,
    Card,
)

################################################################################

class CardDeck:
    """
    Class that generates the state of a card deck.
    A deck's state can be derived from this by selecting cards in this class in a given order.

    Subclass this class to include or exclude certain cards; the __init__ method will take the list of cards as the possible cards in the deck. If the deck should be sortable, include a __ge__ method.
    """
    def __init__(
        self,
        cards,
    ):
        self.cards = cards

    def __repr__(self):
        cards_string = ", ".join(repr(card) for card in self.cards)
        return f"CardDeck({cards_string})"

    def __len__(self):
        return len(self.cards)

        