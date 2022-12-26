"""
Module defining classes for a deck of cards for the Queen of Spades card game, where only numbered cards with an 8 or above are kept, and there are no jokers.
"""
# Third-party imports

# Global imports
from cards import (
    PlayingCard,
    PlayingCardLabel,
)

# Local imports

################################################################################

class QueenOfSpadesPlayingCard(PlayingCard):
    """
    Do not use this method for playing; it is only used for sorting. For playing, create a GameCard class that has a PlayingCard as a property, and order the game cards according to game rules instead of by the sorting of the playing cards.
    """
    LABEL_ORDERS = [
        PlayingCardLabel.EIGHT,
        PlayingCardLabel.NINE,
        PlayingCardLabel.TEN,
        PlayingCardLabel.JACK,
        PlayingCardLabel.QUEEN,
        PlayingCardLabel.KING,
        PlayingCardLabel.ACE,
    ]
