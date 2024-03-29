# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../nbs/01_deck.ipynb 4
from card import *

# %% ../nbs/01_deck.ipynb 5
import random

class Deck:
    """Represents a standard playing card deck."""

    def __init__(self):
        self.cards = [Card(suit,rank) for suit in range(4) for rank in range(1,14)]

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def sort(self):
        self.cards.sort()
    
