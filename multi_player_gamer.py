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

player = input("You can play as Player-A or Player-B, choose either 'A' or 'B'. Play only during your turn: ").lower()

if player == 'a':
    while True:
        choice = input("Welcome Player-A. Press 'p' to roll the dice or 'q' to quit: ").lower()
        if choice == 'p':
            scoreA = gameplayA(scoreA)  
        elif choice == 'q':
            print("Goodbye!!")
            print(f"Total score of Player-A: {scoreA}")
            exit()
        else:
            print("Invalid input. Please press 'p' to play or 'q' to quit.")
    
elif player == 'b':
    while True:
        choice = input("Welcome Player-B. Press 'p' to roll the dice or 'q' to quit: ").lower()
        if choice == 'p':
            scoreB = gameplayB(scoreB)  
        elif choice == 'q':
            print("Goodbye!!")
            print(f"Total score of Player-B: {scoreB}")
            exit()
        else:
            print("Invalid input. Please press 'p' to play or 'q' to quit.")
else:
    print("Invalid player choice! Choose either 'A' or 'B'.")

print(f"Total score of Player-A: {scoreA}")
print(f"Total score of Player-B: {scoreB}")
