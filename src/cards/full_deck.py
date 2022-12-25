"""
Module defining classes for a deck of cards that are not tied to any card game.
"""
# Third-party imports

# Global imports

# Local imports
from .cards import (
    CardSuit,
    CardLabel,
    JokerColor,
    Card,
)

################################################################################

class CardDeck:
    """
    Class that generates the state of a full deck. A deck's state can be derived from this by selecting cards in this class in a given order.
    """
    def __init__(
        self,
        cards,
    ):
        self.cards = cards

    @classmethod
    def full_deck_without_jokers(cls):
        return cls(
            [
                *(
                    Card(CardSuit(suit), CardLabel(label))
                    for suit in CardSuit.SUITS
                    for label in CardLabel.LABELS
                ),
            ]
        )

    @classmethod
    def full_deck_with_jokers(cls):
        return cls(
            [
                *(
                    Card(CardSuit(suit), CardLabel(label))
                    for suit in CardSuit.SUITS
                    for label in CardLabel.LABELS
                ),
                *(
                    Card(None, None, JokerColor(color))
                    for color in JokerColor.COLORS
                ),
            ]
        )


    @classmethod
    def portuguese_deck(cls):
        return cls(
            [
                Card(CardSuit(suit), CardLabel(label))
                for suit in CardSuit.SUITS
                for label in CardLabel.PORTUGUESE_LABELS
            ]
        )

    def __repr__(self):
        cards_string = ", ".join(repr(card) for card in self.cards)
        return f"CardDeck({cards_string})"

    def __len__(self):
        return len(self.cards)