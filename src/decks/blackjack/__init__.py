"""
Module for a deck used by a dealer to enable players to play Blackjack against the house. The class comes with a parameter to determine the number of standard decks used by the dealer to host the game.
"""
# Third-party imports
from itertools import repeat, chain

# Global imports
from cards import PlayingCard

# Local imports
from ..standard import StandardCardDeck

################################################################################

def BlackjackCardDeck(n_of_decks = 1):
    """
    Factory function that generates the class for a BlackjackDeck. 

    Arguments
    ---------

    n_of_decks: int
        Number of decks used by the dealer in their set of cards to deal during the game.
    """
    class BJDeck(StandardCardDeck):
        CARD_CLASS = PlayingCard
        CARD_PROPERTIES = chain(*repeat(StandardCardDeck.CARD_PROPERTIES, n_of_decks))


    return BJDeck()

