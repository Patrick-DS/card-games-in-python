"""
Module defining classes for a full deck of cards, where all the cards are included, including jokers.
"""
# Third-party imports

# Global imports

# Local imports
from ..card_deck import CardDeck
from ..cards import (
    CardSuit,
    CardLabel,
    CardColor,
    Card,
)

################################################################################

class FullCardDeck(CardDeck):
    def __init__(self):
        cards = sorted([
            *(
                Card(CardSuit(suit_symbol), CardLabel(label_symbol))
                for suit_symbol in CardSuit.SUIT_SYMBOLS
                for label_symbol in CardLabel.LABEL_SYMBOLS
            ),
            *(
                Card(None, None, CardColor(color_name))
                for color_name in CardColor.COLORS
            ),
        ])

        super().__init__(cards)