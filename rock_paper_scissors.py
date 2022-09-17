import sys
from random import choice


class player:
    def __init__(self):
        self.player = None
        self.computer = None
        self.player_score = 0
        self.computer_score = 0
        self.tie = 0
    
    def play(self):
        self.player = input ("\nWhat's your Weapon of Choice? >> 'R' for Rock, 'P' for Paper, 'S' for Scissors: ").lower()
        self.computer = choice(['r', 'p', 's'])
        print (f"\nThe Computer selects {self.computer.capitalize()}\n")

        if self.player == self.computer:
            self.tie += 1
            print ("It\'s a tie!")

        elif self.player == 'r' and self.computer == 's':
            print ("You Won!")
            self.player_score += 1
        
        elif self.player == 's' and self.computer == 'p':
            print ("You Won!")
            self.player_score += 1
            
        elif self.player == 'p' and self.computer == 'r':
            print ("You Won!")
            self.player_score += 1   
        else:
            print ("You Lost!")
            self.computer_score += 1

    def run(self):
        print(f"\n*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*")
        print (f"\n\t~ Welcome to the Classic: ROCK ~ Paper ~ Scissors ~\n")
        print("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*")
        while True:
            self.play()
            print (f"\nPlayer score = {self.player_score}: Computer score = {self.computer_score}: Ties = {self.tie}\n")
            quit = input ("To quit Enter 'Q' or 'C' to continue: ").capitalize()
            if quit == "Q":
                sys.exit()
            else:
                continue
                             

player = player()
player.run()