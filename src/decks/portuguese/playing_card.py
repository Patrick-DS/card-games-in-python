"""
Module defining classes for a deck of cards for Portuguese card games, where 8's, 9's and 10's are removed, the 7's value is between the King and the Ace, the Jack is considered of higher value than the Queen, and there are no jokers.
"""
# Third-party imports

# Global imports
from cards import (
    PlayingCard,
    PlayingCardLabel,
)

# Local imports

################################################################################

PORTUGUESE_CARD_VALUES = {
    PlayingCardLabel.TWO: 0,
    PlayingCardLabel.THREE: 0,
    PlayingCardLabel.FOUR: 0,
    PlayingCardLabel.FIVE: 0,
    PlayingCardLabel.SIX: 0,
    PlayingCardLabel.QUEEN: 2,
    PlayingCardLabel.JACK: 3,
    PlayingCardLabel.KING: 4,
    PlayingCardLabel.SEVEN: 10,
    PlayingCardLabel.ACE: 11,
}

class PortuguesePlayingCard(PlayingCard):
    """
    Do not use this method for playing; it is only used for sorting. For playing, create a GameCard class that has a PlayingCard as a property, and order the game cards according to game rules instead of by the sorting of the playing cards.

    The value property is added because it's the same in all portuguese games.
    """
    LABEL_ORDERS = [
        PlayingCardLabel.TWO,
        PlayingCardLabel.THREE,
        PlayingCardLabel.FOUR,
        PlayingCardLabel.FIVE,
        PlayingCardLabel.SIX,
        PlayingCardLabel.QUEEN,
        PlayingCardLabel.JACK,
        PlayingCardLabel.KING,
        PlayingCardLabel.SEVEN,
        PlayingCardLabel.ACE,
    ]

    @property
    def value(self):
        return PORTUGUESE_CARD_VALUES[self.label]

