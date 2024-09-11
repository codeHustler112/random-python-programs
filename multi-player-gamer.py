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
player = input("You can play as  Player-A or Player-B, choose either 'A' or 'B',play only during your turn \n ").lower()


    
if (player == 'a'):
    
    while True:
        choice=input("Welcome Player-A. Roll the dice and see what you get. Press 'p' to play and 'q' to quit.\n").lower()
        if ( choice == 'p'):
            total_score=gameplayA(scoreA)
            print(f"Total score {total_score}")
        elif choice == 'q':
            print("Goodbye!!")
            exit()  
        else:
            print("Invalid input. Please press 'p' to play or 'q' to quit.")       

else: 
     while True:
        choice=input("Welcome Player-B. Roll the dice and see what you get. Press 'p' to play and 'q' to quit.\n").lower()
        if ( choice == 'p'):
            total_score=gameplayA(scoreA)
            print(f"Total score {total_score}")
        elif choice == 'q':
            print("Goodbye!!")
            exit()  
        else:
            print("Invalid input. Please press 'p' to play or 'q' to quit.")     
                                
        

    


        


