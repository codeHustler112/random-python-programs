# ask users to for bunch of adjectives and add those words to our story

with open("story.txt", 'r') as file:
    story = file.read()

words = set()
start_of_word = -1
target_start ="<"
target_end=">"


for i,char in enumerate(story):
    #print(i,char)
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i+1]
        words.add(word)  # taken a slice of the word we want to replace
        start_of_word =-1

#print(words)

answers ={}
for word in words:
    answer= input("enter a word for" + word + ':')
    answers[word] = answer

#print(answers)

for word in words:
    story =story.replace(word, answers[word])

print(story)