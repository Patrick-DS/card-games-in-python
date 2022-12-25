"""
Module defining classes for a card that are not tied to any game.
"""
# Third-party imports
from enum import Enum

# Global imports

# Local imports

################################################################################

LABEL_SYMBOLS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
LABEL_NAMES = {
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
    "J": "Jack",
    "Q": "Queen",
    "K": "King",
    "A": "Ace",
}

class PlayingCardLabel(Enum):
    """
    Class that types the 13 labels (or values) available in a card deck.
    This excludes jokers.
    """
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

    @property
    def suit_name(self) -> str:
        return LABEL_NAMES[self.value]

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.suit_name
