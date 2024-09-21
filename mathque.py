'''generate a bunch of random math quetions and ask user to answer them and won't let them procede till 
they answer correctly '''

# Here are 5 simple math questions:

# What is 8×7?
# If you have 12 apples and give away 5, how many apples do you have left?
# What is the square root of 64?
# Solve for x: 3𝑥 + 5= 14

# What is 25÷5?

answer = int(input("Answer the question : "))

questions = [
    {1 : "What is 8×7?", answer : 56},
    {2 : "If you have 12 apples and give away 5, how many apples do you have left?", answer : 7},
    {3 : "What is the square root of 64?", answer : 8},
    {4 : "Solve for x: 3𝑥 + 5= 14", answer : 3 },
    {5 : "What is 25÷5?", answer : 5}
    ]



#...to be continued