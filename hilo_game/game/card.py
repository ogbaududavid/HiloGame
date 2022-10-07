import random
class Card:

    def __init__(self):
        """A rectangular card with numbers from 1-13
        The responsibility of card is to keep track of the number on it"""
        self.value = random.randint(1,13)