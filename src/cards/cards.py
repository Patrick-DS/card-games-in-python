"""
Module defining classes for a card that are not tied to any game.
The variables and methods here are meant to serve as data sources to create game cards. So nothing should tie them to a specific game; the data in the classes is meant to be used to generate other classes that would have the properties that a card needs for a game.
"""
# Third-party imports
from typing import Optional

# Global imports

# Local imports
from .color import (
    PlayingCardColor,
    COLORS_ORDERING,
)
from .suit import (
    PlayingCardSuit,
    SUITS_ORDERING,
)
from .label import (
    PlayingCardLabel,
    LABELS_ORDERING,
)

################################################################################

class PlayingCard:
    """
    A generic class to define the cards in a full deck.
    Subclass this class in various games to enable the features of the game.
    """
    COLOR_ORDERS = COLORS_ORDERING
    SUIT_ORDERS = SUITS_ORDERING
    LABEL_ORDERS = LABELS_ORDERING

    def __init__(
        self,
        suit: PlayingCardSuit,
        label: PlayingCardLabel,
        joker_color: Optional[PlayingCardColor] = None,
    ):
        if (joker_color is not None):
            self.joker_color = joker_color
            self.suit = None
            self.label = None
        else:
            self.joker_color = None
            self.suit = suit
            self.label = label

    @property
    def is_joker(self) -> bool:
        return self.joker_color is not None

    @property
    def card_color(self) -> PlayingCardSuit:
        if self.is_joker:
            return self.joker_color
        else:
            return self.suit.suit_color 

    def __str__(self):
        if (self.is_joker):
            return self.joker_color.value[0] + "J"
        else:
            return f"{self.label}{self.suit}"

    def __repr__(self):
        if (self.joker_color is not None):
            return f"{self.joker_color.value} Joker"
        else:
            return f"{self.label} of {repr(self.suit)}"

    def __eq__(self, other):
        """
        Used to determine if two playing cards represent exactly the same card (value and suit, and in the case of jokers, including color).
        """
        if self.is_joker:
            return self.joker_color == other.joker_color
        else:
            return (
                self.suit == other.suit 
                and 
                self.label == other.label
            )

    def __lt__(self, other):
        """
        Used only to produce a sorted deck. Do not use in games.
        For this, create another class and use PlayingCard instances as data sources.
        """
        if self.is_joker: # First deal with jokers
            if other.is_joker:
                return self.joker_color < other.joker_color
            else:
                return False
        elif (self.suit != other.suit): # Then deal with suits
            return self.suit < other.suit
        else: # Then deal with labels
            return self.label < other.label