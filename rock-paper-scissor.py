import random

computer = random.randint(1,3)


human = int(input("Let's Play rock, paperm scissor:\n \
      Choose 1 for Rock \n Choose 2 for Paper \n Choose 3 for Scissor\n" ))


options = {1: "Rock", 2: "Paper", 3: "Scissors"}

print(f"Computer chose: {options[computer]}")
print(f"You chose: {options[human]}")

if computer == human:
    print(f"It's a tie. We both chose {options[computer]}")

# Check for win conditions
elif (computer == 1 and human == 2) or (computer == 2 and human == 3) or (computer == 3 and human == 1):
    print("Yeh! You win.")
else:
    print("You lose.")