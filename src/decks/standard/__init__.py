"""
Module defining classes for a standard deck of cards, where all the cards are included, excluding jokers.
"""
# Third-party imports
from itertools import product

# Global imports
from cards import (
    PlayingCard,
    PlayingCardSuit,
    PlayingCardLabel,
)

# Local imports
from ..card_deck import CardDeck

################################################################################

class StandardCardDeck(CardDeck):
    CARD_CLASS = PlayingCard
    CARD_PROPERTIES = [
        (suit, label, None)
        for suit, label in product(PlayingCardSuit, PlayingCardLabel)
    ]
