"""
Module defining classes for a card that are not tied to any game.
"""
# Third-party imports
from typing import Optional

# Global imports

# Local imports

################################################################################


class CardColor:
    COLORS = ["Red", "Black"]

    def __init__(self, color_name: str):
        if (color_name not in self.COLORS):
            raise ValueError(f"The value of the color '{color_name}' needs to be either 'Red' or 'Black'.")
        else:
            self.color_name = color_name


class CardSuit:
    """
    Class that types the four suits available in a card deck.
    This excludes jokers.
    """
    SUIT_SYMBOLS = ["♥", "♦", "♣", "♠"]
    SUIT_NAMES = {
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
        if (suit_symbol not in self.SUIT_SYMBOLS):
            raise ValueError(f"The value of the suit '{suit_symbol}' needs to be in the following list: ♥, ♦, ♣, or ♠.")
        else:
            self.suit_symbol = suit_symbol
            self.suit_color = self.SUIT_COLORS[suit_symbol]
    
    def __str__(self):
        return self.suit_symbol

    def __repr__(self):
        return self.SUIT_NAMES[self.suit_symbol]


class CardLabel:
    """
    Class that types the 13 labels (or values) available in a card deck.
    This excludes jokers.
    """
    LABEL_SYMBOLS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    PORTUGUESE_LABEL_SYMBOLS = ["2","3","4","5","6","Q","J","K","7","A"]
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

    def __init__(self, label_symbol: str):
        if (label_symbol not in self.LABEL_SYMBOLS):
            raise ValueError(f"The value of the label '{label_symbol}' needs to be in the following list: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, or A.")
        else:
            self.label_symbol = label_symbol
    
    def __str__(self):
        return self.label_symbol

    def __repr__(self):
        return self.LABEL_NAMES[self.label_symbol]


class Card:
    """
    A generic class to define the cards in a full deck.
    Subclass this class in various games to enable the features of the game.
    """
    COLOR_ORDERS = CardColor.COLORS
    SUIT_ORDERS = CardSuit.SUIT_SYMBOLS
    LABEL_ORDERS = CardLabel.LABEL_SYMBOLS

    def __init__(
        self,
        suit: CardSuit,
        label: CardLabel,
        joker_color: Optional[CardColor] = None,
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
    def is_joker(self):
        return self.joker_color is not None

    def __str__(self):
        if (self.is_joker):
            return f"{self.joker_color.color_name[0]}J"
        else:
            return f"{self.label}{self.suit}"

    def __repr__(self):
        if (self.joker_color is not None):
            return f"{self.joker_color.color_name} Joker"
        else:
            return f"{self.label} of {repr(self.suit)}"

    def __lt__(self, other):
        # First deal with jokers:
        if self.is_joker:
            if other.is_joker:
                self_joker_color_index = self.COLOR_ORDERS.index(self.joker_color.color_name)
                other_joker_color_index = self.COLOR_ORDERS.index(other.joker_color.color_name)
                return self_joker_color_index < other_joker_color_index
            else:
                return False
        elif other.is_joker:
            return True

        # Then deal with suits
        self_suit_index = self.SUIT_ORDERS.index(self.suit.suit_symbol)
        other_suit_index = self.SUIT_ORDERS.index(other.suit.suit_symbol)
        if (self_suit_index != other_suit_index):
            return self_suit_index < other_suit_index

        # Then deal with labels
        self_label_index = self.LABEL_ORDERS.index(self.label.label_symbol)
        other_label_index = self.LABEL_ORDERS.index(other.label.label_symbol)
        return self_label_index < other_label_index