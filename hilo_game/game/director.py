import random
from game.card import Card

class Director:
    """A person who directs the game
    The responsibility of the Director is to control the actions of the game
    Attributes: 
        points (int): The starting points of a player at the biginning of the game, the points 
        increases or decreases as the play guesses correctly or incorrectly the next card
        play_again (boolean): A string that holds the default value of "y" and can be updated by the 
        user if they will like to continue playing the game."""
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.points=300
        self.play_again= True

    def start_game(self):
        """Starts the game by calling the main loop and the individal methods in the Director class

        Args: self(Director): An instance of Director """

        while self.play_again == True and self.points >0:
            self.get_input()
            self.calculate_points()
            self.show_result()

    def get_input(self):
        """Displays the current card to the user and prompts the user to enter a guess
        to determine if the next card will he higher or lower.

        Arg: self(Director): An instance of Director"""

        card= Card()
        card2= Card()
        self.current_card= card.value
        self.guess_card= card2.value
        print(f"The card is: {self.current_card}")
        self.guess = input("Higher or lower (h/l): ").lower()
        
    
    def calculate_points(self):
        """Determine if the user guessed correctly or not. If the users guess was correct add +100 to the score
        else remove -70 from the score.
        Ask the user if they will like to play again.
        When the user's point is less than 0, display game over.

        Arg: self(Director): An instance of Director"""

        if self.guess_card > self.current_card and self.guess == "h":
            self.points += 100
        elif self.guess_card < self.current_card and self.guess == "l":
            self.points += 100
        elif self.points == 0:
            print("Game over! You do not have enough points to play again.")
        elif self.play_again== "n":
            print("Game over!")
        else:
            self.points-= 70

    def show_result(self):
        """ Print the last card, the user's score and ask the user if they will like to play again

        Arg: self(Director): An instance of Director"""

        print(f"The card was: {self.guess_card}")
        print(f"yourscore is: {self.points} points")
        play_question=input("Play again (y/n): ").lower()
        self.play_again = (play_question == "y")
        if self.points <= 0:
            print("Game Over! You do not have enough points to play again")
        elif play_question == "n":
             print("Game Over!")
        elif play_question != "n":
            print("Invalid input! Game Over.")
        print()

