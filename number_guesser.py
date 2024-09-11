# generate a randowm number and we will  track how may tries it takes a user to guess the number
import random

num= random.randint(1,100)
count=0


while True:
    ans = int(input("You have to guess an integer between 1 and 100: "))
    count += 1  # Increment the count with each attempt

    if ans == num:
        print("Hooray! You have guessed it correctly.")
        break  # Exit the loop if the guess is correct
    elif ans > num:
        print("Choose a lower number.")
    else:
        print("Choose a higher number.")
        
print(f"You have guessed the number in {count} attempts.")

