"""
Module defining classes for a deck of cards for Portuguese card games, where 8's, 9's and 10's are removed, the 7's value is between the King and the Ace, the Jack is considered of higher value than the Queen, and there are no jokers.
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

class PortugueseCard(Card):
    LABEL_ORDERS = CardLabel.PORTUGUESE_LABEL_SYMBOLS


class PortugueseCardDeck(CardDeck):
    def __init__(self):
        cards = sorted([
            PortugueseCard(CardSuit(suit_symbol), CardLabel(label_symbol))
            for suit_symbol in CardSuit.SUIT_SYMBOLS
            for label_symbol in CardLabel.PORTUGUESE_LABEL_SYMBOLS
        ])

        super().__init__(cards)