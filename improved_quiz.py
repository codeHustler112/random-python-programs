score =0
total_questions = 10

questions = [{"question" : "What is the capital city of Australia?", "answer" : "Canberra"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "In which year did the Titanic sink?", "answer": "1912"},
    {"question": "What is the chemical symbol for the element gold?", "answer": "Au"},
    {"question": "Who was the first person to walk on the Moon?", "answer": "Neil Armstrong"},
    {"question": "What is the longest river in the world?", "answer": "The Nile River"},
    {"question": "In which country is the Great Pyramid of Giza located?", "answer": "Egypt"},
    {"question": "Who painted the famous artwork 'The Starry Night'?", "answer": "Vincent van Gogh"},
    {"question": "Which element on the periodic table has the atomic number 1?", "answer": "Hydrogen"}
    ]   
def check_ans(correct_ans):
    global score
    ans=input("Your answer: \n").strip()
    if (correct_ans.lower() == ans.lower()):
        score+=1
    return score

for i in questions:
    print(f" {i['question']}")
    check_ans(i['answer'])

    # Final score after the quiz
print(f"\nYou answered {score} out of {total_questions} questions correctly.")
percentage_score = (score / total_questions) * 100
print(f"Your score is {percentage_score:.2f}%")