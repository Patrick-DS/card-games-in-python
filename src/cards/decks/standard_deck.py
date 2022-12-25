"""
Module defining classes for a deck of cards for standard card games, where all cards are in the deck except the jokers.
"""
# Third-party imports

# Global imports

# Local imports
from ..card_deck import CardDeck
from ..cards import (
    CardSuit,
    CardLabel,
    Card,
)

################################################################################


class StandardCardDeck(CardDeck):
    def __init__(self):
        cards = sorted([
            Card(CardSuit(suit), CardLabel(label))
            for suit in CardSuit.SUIT_SYMBOLS
            for label in CardLabel.LABEL_SYMBOLS
        ])

        super().__init__(cards)