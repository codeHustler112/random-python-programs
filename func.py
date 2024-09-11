import random

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