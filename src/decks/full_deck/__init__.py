"""
Module defining classes for a full deck of cards, where all the cards are included, including jokers.
"""
# Third-party imports
from itertools import product

# Global imports
from cards import (
    PlayingCard,
    PlayingCardSuit,
    PlayingCardLabel,
    PlayingCardColor,
)

# Local imports
from ..card_deck import CardDeck

################################################################################

class FullCardDeck(CardDeck):
    CARD_CLASS = PlayingCard
    CARD_PROPERTIES = [
        *(
            (suit, label, None)
            for suit, label in product(PlayingCardSuit, PlayingCardLabel)
        ),
        *(
            (None, None, joker_color)
            for joker_color in PlayingCardColor
        ),
    ]