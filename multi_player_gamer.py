#you get a turn, roll a dice, you get anything b/w 1 to 6,\
#  for any number other than 1 we add it our score and at 1, you decide how many times \
#you want to roll the dice, catch is when you hit 1 your sscore becomes 0, who ever reaches 50\
#will win
#STEPS  
# we need to ask reader if they want to roll a dice, random num gebnerator, then ask reader if they want to 
# continue to stop their turn and add their score then compare their score ith other player, anyone with 50 or 
# above 50 should be declared  a winner.

from func import gameplayA, gameplayB

scoreA = 0
scoreB = 0

def go_to_playerA(scoreA, scoreB):
    while True:
        choice = input("Welcome Player-A. Press 'p' to roll the dice, 'b' to switch to Player-B, or 'q' to quit: ").lower()
        if choice == 'p':
            scoreA = gameplayA(scoreA)  
        elif choice == 'b':
            print(f"Total score of Player-A: {scoreA}")
            return scoreA, scoreB  # Switch back to Player B
        elif choice == 'q':
            print("Goodbye!!")
            print(f"Total score of Player-A: {scoreA}")
            print(f"Total score of Player-B: {scoreB}")
            exit()
        else:
            print("Invalid input. Please press 'p' to play, 'b' to switch, or 'q' to quit.")

def go_to_playerB(scoreA, scoreB):
    while True:
        choice = input("Welcome Player-B. Press 'p' to roll the dice, 'a' to switch to Player-A, or 'q' to quit: ").lower()
        if choice == 'p':
            scoreB = gameplayB(scoreB)  
        elif choice == 'a':
            print(f"Total score of Player-B: {scoreB}")
            return scoreA, scoreB  # Switch back to Player A
        elif choice == 'q':
            print("Goodbye!!")
            print(f"Total score of Player-A: {scoreA}")
            print(f"Total score of Player-B: {scoreB}")
            exit()
        else:
            print("Invalid input. Please press 'p' to play, 'a' to switch, or 'q' to quit.")

# Main game loop
while True:
    player = input("You can play as Player-A or Player-B. Choose 'A' or 'B' (press 'q' to quit): ").lower()
    
    if player == 'a':
        scoreA, scoreB = go_to_playerA(scoreA, scoreB)
        
    elif player == 'b':
        scoreA, scoreB = go_to_playerB(scoreA, scoreB)
        
    elif player == 'q':
        print("Goodbye!!")
        exit()

    else:
        print("Invalid player choice! Choose either 'A' or 'B'.")


