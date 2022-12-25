"""
Single-player game that consists in beating the house at guessing who has the highest card: you or the house. 

The rules are simple: the player and the house begin with one half of the deck each. 

At each turn, the house and the player pick a card from their pile. The player sees its card, then gets to guess if it's higher or lower than the house's card. If guessed correctly, one point is awarded to the player; if guessed wrong, one point is awarded to the house. Suits don't matter, so ties are possible, in which case there are no points awarded. When a guess is done (also in cases of ties), both cards are discarded and the turn is over. Another turn begins until both players exhausted their pile, in which case the points are counted to determine the winner. 

A tie is possible, in which case there are no winners.
"""

# Third-party imports

# Global imports

# Local imports
from ..decks import StandardCardDeck

################################################################################

class HighCardGame:
    def __init__(self):
        self.card_deck = StandardCardDeck()
        self.player_pile, self.house_pile = tuple(self.card_deck.sample(
            len(self.card_deck)/2,
            len(self.card_deck)/2,
        ))
        self.score = {
            "Player": 0,
            "House": 0,
        }

    def play(self):
        while len(self.player_pile) > 0:
            self.play_turn()

        if self.score["Player"] > self.score["House"]:
            print(f"You won with {self.score['Player']} points! The house had {self.score['House']} points.")
        elif self.score["Player"] < self.score["House"]:
            print(f"You lost with {self.score['Player']} points! The house had {self.score['House']} points.")
        else:
            print(f"It's a tie with {self.score['Player']} points!")

    def play_turn(self):
        player_card = self.player_pile.pop()
        player_input = None
        print(f"\nYour card is a {repr(player_card)} ({player_card}).")
        while player_input not in ["1","2"]:
            player_input = input(
                "\n".join([
                    "Is your card lower or higher than the house's?",
                    "1) Lower",
                    "2) Higher\n\n",
                ])
            )
            
        player_thinks_its_card_is_higher = player_input == "2"

        house_card = self.house_pile.pop()
        print(f"The house's card is: a {repr(house_card)} ({house_card}).")
        if player_thinks_its_card_is_higher == (player_card > house_card):
            print("You get one point!\n")
            self.score["Player"] += 1
        else:
            print("The house gets a point.\n")
            self.score["House"] += 1