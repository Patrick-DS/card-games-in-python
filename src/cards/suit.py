"""
Module defining playing card suits and how to render them in different contexts.
"""
# Third-party imports
from enum import Enum

# Global imports

# Local imports
from .color import PlayingCardColor

################################################################################

RED_SUIT_SYMBOLS = ["♥", "♦"]
BLACK_SUIT_SYMBOLS = ["♣", "♠"]
SUIT_NAMES = {
    "♥": "Hearts",
    "♦": "Diamonds",
    "♣": "Clubs",
    "♠": "Spades",
}

class PlayingCardSuit(Enum):
    """
    Class that types the four suits available in a card deck.
    This excludes jokers.
    """
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"

    @property
    def suit_name(self) -> str:
        return SUIT_NAMES[self.value]

    @property
    def suit_color(self) -> PlayingCardColor:
        if self.value in RED_SUIT_SYMBOLS:
            return PlayingCardColor.RED
        elif self.value in BLACK_SUIT_SYMBOLS:
            return PlayingCardColor.BLACK

    def __str__(self):
        return self

    def __repr__(self):
        return self.suit_name