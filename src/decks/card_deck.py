"""
Module defining classes for a deck of cards that are not tied to any card game.
"""
# Third-party imports

# Global imports
from cards import (
    PlayingCard,
    PlayingCardSuit,
    PlayingCardLabel,
    PlayingCardColor,
)

# Local imports

################################################################################

class CardDeck:
    """
    Class that generates the cards in a card deck for a game.

    Arguments
    ---------
    card_properties: list[tuple[PlayingCardSuit, PlayingCardLabel, PlayingCardColor]]
        The list of the properties defining each card in the deck. 

    card_cls: subclass(PlayingCard) = PlayingCard
        The card_cls is an arbitrary subclass of the PlayingCard class, where additional methods can be added for a game's functionality.

        Subclass PlayingCard to include or exclude certain cards; the __init__ method will take the list of cards as the possible cards in the deck. If the deck should be sortable, include a __ge__ method.
    """
    def __init__(
        self,
        card_cls = PlayingCard,
        card_properties: list[
            tuple[
                PlayingCardSuit,
                PlayingCardLabel,
                PlayingCardColor,
            ]
        ] = [],
        deck_name: str = "CardDeck",
    ):
        self.deck_name = deck_name
        self.cards = sorted([
            card_cls(suit, label, joker_color)
            for suit, label, joker_color in card_properties
        ])

    def __repr__(self):
        cards_string = ", ".join(f"\n\t{repr(card)}" for card in self.cards)
        return f"{self.deck_name}({cards_string},\n)"

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        return iter(self.cards)



        