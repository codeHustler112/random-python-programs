score = 0

def check_ans(correct_answer, score):
    answer = input("Your answer: ").strip()
    if answer.lower() == correct_answer.lower():
        score += 1
    return score

print("Are you ready for the quiz? \nAnswer these 10 questions, I hope you will have fun.\n")

# Question 1
print("Question: What is the capital city of Australia? \n")
Answer = "Canberra"
score = check_ans(Answer, score)

# Question 2
print("Question: Who wrote the play 'Romeo and Juliet'? \n")
Answer = "William Shakespeare"
score = check_ans(Answer, score)

# Question 3
print("Question: What is the largest planet in our solar system? \n")
Answer = "Jupiter"
score = check_ans(Answer, score)

# Question 4
print("Question: In which year did the Titanic sink?\n")
Answer = "1912"
score = check_ans(Answer, score)

# Question 5
print("Question: What is the chemical symbol for the element gold?\n") 
Answer = "Au"
score = check_ans(Answer, score)

# Question 6
print("Question: Who was the first person to walk on the Moon? \n") 
Answer = "Neil Armstrong"
score = check_ans(Answer, score)

# Question 7
print("Question: What is the longest river in the world?\n") 
Answer = "The Nile River"
score = check_ans(Answer, score)

# Question 8
print("Question: In which country is the Great Pyramid of Giza located?\n") 
Answer = "Egypt"
score = check_ans(Answer, score)

# Question 9
print("Question: Who painted the famous artwork 'The Starry Night'?\n") 
Answer = "Vincent van Gogh"
score = check_ans(Answer, score)

# Question 10
print("Question: Which element on the periodic table has the atomic number 1?\n") 
Answer = "Hydrogen"
score = check_ans(Answer, score)

# Final score after the quiz
print(f"\nThe final score is: {score}")
