"""
Module defining classes for a deck of cards for Portuguese card games, where 8's, 9's and 10's are removed, the 7's value is between the King and the Ace, the Jack is considered of higher value than the Queen, and there are no jokers.
"""
# Third-party imports
from itertools import product

# Global imports
from cards import PlayingCardSuit

# Local imports
from ..card_deck import CardDeck
from .playing_card import (
    PortuguesePlayingCard,
    PORTUGUESE_CARD_LABELS,
)

################################################################################

class PortugueseCardDeck(CardDeck):
    def __init__(self):
        super().__init__(
            deck_name = "PortugueseCardDeck",
            card_properties = [
                (suit, label, None)
                for suit, label in product(PlayingCardSuit, PORTUGUESE_CARD_LABELS)
            ],
            card_cls = PortuguesePlayingCard
        )