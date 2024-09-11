import random
# from multi_player_gamer import player  




def gameplayA(scoreA):
   
    dice = random.randint(1,6)
    print(f"you scored {dice}")
    if ( dice == 1 ):
        scoreA =0 
        print(f"since you pressed 1 you are back to square 0. No PUN Intended! :D")
    else:
        scoreA+=dice
        print(f"total score now : {scoreA}")
        if ( scoreA >= 50):
            print(f"Hurray you scored {scoreA}. YOU WON!!")
            exit()    
   
    return scoreA

def gameplayB(scoreB):
    dice = random.randint(1,6)
    print(f"you scored {dice}")
    if ( dice == 1 ):
        scoreB =0 
        print(f"since you pressed 1 you are back to square 0. No PUN Intended! :D")
    else:
        scoreB+=dice
        print(f"total score now : {scoreB}")
        if ( scoreB >= 50):
            print(f"Hurray you scored {scoreB}. YOU WON!!")
            exit()    
   
    return scoreB

# def scores_for_a(player):
#     while True:
#         choice = input("Welcome Player-A. Press 'p' to roll the dice or 'q' to quit: ").lower()
#         if choice == 'p':
#             scoreA = gameplayA(scoreA)  
#         elif choice == 'q':
#             print("Goodbye!!")
#             exit()
#         else:
#             print("Invalid input. Please press 'p' to play or 'q' to quit.")