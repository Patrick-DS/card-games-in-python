"""
Module defining a function to sample from a list. It is kept detached from any class to enable sampling from any iterable (in our context, any kind of class defining a pile of cards of any kind).
"""
# Third-party imports
from typing import TypeVar
from random import shuffle

# Global imports

# Local imports

################################################################################

T = TypeVar("T")

def sample(
    item_list: list[T],
    *sample_sizes: list[int],
) -> list[list[T]]:
    """
    Samples len(sample_sizes) lists of items in the item_list, each of size sample_sizes[i] for i in range(len(sample_sizes)).
    """
    # Type check
    for index, sample_size in enumerate(sample_sizes):
        if sample_size < 0:
            raise ValueError(f"Use a positive value for the sample sizes. Sample size #{index + 1} equals {sample_size}.")

    if sum(sample_sizes) > len(item_list):
        raise ValueError(f"Cannot sample more than {len(item_list)} cards from this deck.")

    items_to_sample_from = [*item_list]
    shuffle(items_to_sample_from)
    
    partial_sums = [int(sum(sample_sizes[:i+1])) for i in range(len(sample_sizes))]

    return (
        items_to_sample_from[sample_start:sample_end]
        for sample_start, sample_end in zip([0, *partial_sums], partial_sums)
    )

        