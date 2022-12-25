"""
Module defining classes for a card that are not tied to any game.
"""
# Third-party imports
from typing import Optional

# Global imports

# Local imports

################################################################################


class CardSuit:
    """
    Class that types the four suits available in a card deck.
    This excludes jokers.
    """
    SUITS = ["♥", "♦", "♣", "♠"]
    SUITS_NAMES = {
        "♥": "Hearts",
        "♦": "Diamonds",
        "♣": "Clubs",
        "♠": "Spades",
    }
    SUIT_COLORS = {
        "♥": "Red",
        "♦": "Red",
        "♣": "Black",
        "♠": "Black",
    }

    def __init__(self, suit_symbol: str):
        if (suit_symbol not in self.SUITS):
            raise ValueError(f"The value of the suit '{suit_symbol}' needs to be in the following list: ♥, ♦, ♣, or ♠.")
        else:
            self.suit_symbol = suit_symbol
            self.suit_color = self.SUIT_COLORS[suit_symbol]
    
    def __str__(self):
        return self.suit_symbol

    def __repr__(self):
        return self.SUITS_NAMES[self.suit_symbol]


class CardLabel:
    """
    Class that types the 13 labels (or values) available in a card deck.
    This excludes jokers.
    """
    LABELS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    PORTUGUESE_LABELS = ["2","3","4","5","6","Q","J","K","7","A"]
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

    def __init__(self, label: str):
        if (label not in self.LABELS):
            raise ValueError(f"The value of the label '{label}' needs to be in the following list: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, or A.")
        else:
            self.label = label
    
    def __str__(self):
        return self.label

    def __repr__(self):
        return self.LABEL_NAMES[self.label]


class JokerColor:
    """
    Class that types the 2 joker colors available in a card deck.
    """
    COLORS = ["Red", "Black"]

    def __init__(self, color: str):
        if (color not in self.COLORS):
            raise ValueError(f"The value of the color '{color}' needs to be either 'Red' or 'Black'.")
        else:
            self.color = color


class Card:
    """
    A generic class to define the cards in a full deck.
    Subclass this class in various games to enable the features of the game.
    """
    def __init__(
        self,
        suit: CardSuit,
        label: CardLabel,
        joker_color: Optional[JokerColor] = None,
    ):
        if (joker_color is not None):
            self.joker_color = joker_color
            self.suit = None
            self.label = None
        else:
            self.joker_color = None
            self.suit = suit
            self.label = label


    def __str__(self):
        if (self.joker_color is not None):
            return f"{self.joker_color.color[0]}J"
        else:
            return f"{self.label}{self.suit}"

    def __repr__(self):
        if (self.joker_color is not None):
            return f"{self.joker_color.color} Joker"
        else:
            return f"{self.label} of {repr(self.suit)}"