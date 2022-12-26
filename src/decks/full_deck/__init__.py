"""
Module defining classes for a full deck of cards, where all the cards are included, including jokers.
"""
# Third-party imports
from itertools import product

# Global imports

# Local imports
from ..card_deck import CardDeck
from cards import (
    PlayingCardSuit,
    PlayingCardLabel,
    PlayingCardColor,
)

################################################################################

class FullCardDeck(CardDeck):
    def __init__(self):
        super().__init__(
            deck_name = "FullCardDeck",
            card_properties = [
                *(
                    (suit, label, None)
                    for suit, label in product(PlayingCardSuit, PlayingCardLabel)
                ),
                *(
                    (None, None, joker_color)
                    for joker_color in PlayingCardColor
                ),
            ],
        )