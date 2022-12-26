"""
Module defining classes for a full deck of cards, where all the cards are included, including jokers.
"""
# Third-party imports

# Global imports

# Local imports
from .card_deck import CardDeck
from ..cards import (
    PlayingCard,
    PlayingCardSuit,
    PlayingCardLabel,
    PlayingCardColor,
)

################################################################################

class FullCardDeck(CardDeck):
    def __init__(self):
        cards = sorted([
            *(
                PlayingCard(suit, label)
                for suit in PlayingCardSuit
                for label in PlayingCardLabel
            ),
            *(
                PlayingCard(None, None, joker_color)
                for joker_color in PlayingCardColor
            ),
        ])

        super().__init__(cards)