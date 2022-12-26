"""
Module defining card colors.
"""
# Third-party imports
from enum import Enum

# Global imports

# Local imports

################################################################################

COLORS_ORDERING = ["Red", "Black"]

class PlayingCardColor(Enum):
    """
    Color associated with a playing card.
    """
    RED = "Red"
    BLACK = "Black"

    def __lt__(self, other):
        """
        Enables sorting values.
        """
        return COLORS_ORDERING.index(self.value) < COLORS_ORDERING.index(other.value)