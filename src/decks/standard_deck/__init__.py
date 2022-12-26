"""
Module defining classes for a standard deck of cards, where all the cards are included, excluding jokers.
"""
# Third-party imports
from itertools import product

# Global imports

# Local imports
from ..card_deck import CardDeck
from cards import (
    PlayingCardSuit,
    PlayingCardLabel,
)

################################################################################

class StandardCardDeck(CardDeck):
    def __init__(self):
        super().__init__(
            deck_name = "FullCardDeck",
            card_properties = [
                (suit, label, None)
                for suit, label in product(PlayingCardSuit, PlayingCardLabel)
            ]
        )