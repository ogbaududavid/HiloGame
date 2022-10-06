import random

class Director:
    def __init__(self):
        self.points=300
        self.play_again="y"

    def start_game(self):
        while self.play_again.lower() == "y" and self.points >0:
            self.get_input()
            self.higher_lower()
            self.show_result()

    def get_input(self):
        self.current_card=random.randint(1,13)
        print(f"The card is: {self.current_card}")
        self.guess_card = random.randint(1,13)
        self.guess = input("Higher or lower (h/l): ").lower()
        
    
    def higher_lower(self):
        if self.guess_card > self.current_card and self.guess == "h":
            self.points += 100
        elif self.guess_card < self.current_card and self.guess == "l":
            self.points += 100
        elif self.points == 0:
            print("Game over! You do not have enough points to play again.")
        elif self.play_again=="n":
            print("Game over!")
        else:
            self.points-= 70

    def show_result(self):
        print(f"The card was: {self.guess_card}")
        print(f"yourscore is: {self.points} points")
        self.play_again=input("Play again {y/n): ").lower()
        if self.points <= 0:
            print("Game Over! You do not have enough points to play again")
        elif self.play_again=="n":
             print("Game Over!")
        print()

