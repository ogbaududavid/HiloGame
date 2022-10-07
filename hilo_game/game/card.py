import random
class Card:

    def __init__(self):
        """A rectangular card with numbers from 1-13
        The responsibility of card is to keep track of the number on it"""
        self.current_number = 0
        self.guess_number = 0
    
    def display(self):
        self.current_card=random.randint(1,13)
        self.guess_card = random.randint(1,13)