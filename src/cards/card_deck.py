"""
Module defining classes for a deck of cards that are not tied to any card game.
"""
# Third-party imports
from random import shuffle

# Global imports

# Local imports

################################################################################

class CardDeck:
    """
    Class that generates the state of a card deck.
    A deck's state can be derived from this by selecting cards in this class in a given order.

    Subclass this class to include or exclude certain cards; the __init__ method will take the list of cards as the possible cards in the deck. If the deck should be sortable, include a __ge__ method.
    """
    def __init__(
        self,
        cards,
    ):
        self.cards = cards

    def __repr__(self):
        cards_string = ", ".join(repr(card) for card in self.cards)
        return f"CardDeck({cards_string})"

    def __len__(self):
        return len(self.cards)

    def sample(self, *sample_sizes):
        """
        Samples len(sample_sizes) sets of cards, each of size sample_sizes[i] for i in range(len(sample_sizes)).
        """
        for index, sample_size in enumerate(sample_sizes):
            if sample_size < 0:
                raise ValueError(f"Use a positive value for the sample sizes. Sample size #{index + 1} equals {sample_size}.")

        if sum(sample_sizes) > len(self):
            raise ValueError(f"Cannot sample more than {len(self)} cards from this deck.")

        cards_to_sample_from = [*self.cards]
        shuffle(cards_to_sample_from)
        
        partial_sums = [sum(sample_sizes[:i+1]) for i in range(len(sample_sizes))]

        return (
            cards_to_sample_from[sample_start:sample_end]
            for sample_start, sample_end in zip([0, *partial_sums], partial_sums)
        )

        