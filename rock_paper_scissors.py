from doctest import TestResults
import random

#We need inputs fromt he user as to what their selection will be
#we also need to have the computer randomly select a game object
def play():
    user = input ("What's your Choice?'r' for Rock, 'p' for Paper, 's' for Scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It\'s a tie"
# We know r>s, s>p, p>r lets build a helper function for this
    if is_win(user, computer):
        return "You won!"
    return "You lost!"

def is_win(player, computer):
    #this will return true if the player wins
    #game rules r>s, s>p, p>r
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True

print(play())





# https://www.youtube.com/watch?v=8ext9G7xspg&t=333s
#time stamp 22:00 mins