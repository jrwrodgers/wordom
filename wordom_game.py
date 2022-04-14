from wordom_functions import get_wordom_solutions,check_wordom_solution,create_word_weightings,pick_word_from_weights
import random
words=[]
ngames=10000
max_attempts=15
debug = False
automated = True
scores=[0]*max_attempts


def input_wordom(words):
    word_not_ok = True
    while word_not_ok:
        my_guess = input("What is your guess?")
        if(my_guess in words) : word_not_ok = False
        else: print("Word not recognised, please try again")
        if(len(my_guess) !=5): print("length is not 5")
    return my_guess

if  not automated: debug = True

with open("wordlist.txt") as f:
    for aword in f:
        words.append(aword.strip("\n"))
words.sort()
word_dict = {}
word_dict = {words[i]: 0 for i in range(len(words))}
#print(word_dict)


word_weights={}
with open("word_scores_bruteforce.txt") as f:
    for line in f:
        #print(line.split(",")[0],line.split(",")[1])
        word_weights[line.split(",")[0]]=int(line.split(",")[1])

#print(word_weights)
#answer_word=random.choice(words)
#print(answer_word)

correct_guess = False
my_guess=[]
my_guesses = []

for n in range(ngames):

    answer_word = random.choice(words)
    #answer_word = "abbey"
    if debug: print("answer=",answer_word)
    # guess a word
    random.seed(100+n)
    if automated:
        my_guess = random.choice(words)
    else:
        #my_guess = input_wordom(words)
        my_guess ="crane"
    #my_guess = pick_word_from_weights(words,word_weights)
    if debug: print(my_guess)

    correct_guess = False
    #my_guess = input("Enter you guess:")

    my_guesses.append(my_guess)

    correct_position_letters=["*","*","*","*","*"]
    incorrect_position_correct_letters=[]
    incorrect_letters=[]
    possible_answers=[]
    iterations=1
    while correct_guess == False:

        if my_guess==answer_word:
            correct_guess = True
            break
        #check how close
        correct_position_letters,incorrect_position_correct_letters, incorrect_letters = check_wordom_solution(my_guess,answer_word,correct_position_letters,incorrect_position_correct_letters,incorrect_letters)
        if debug: print(correct_position_letters)
        if debug: print(incorrect_position_correct_letters)
        if debug: print(incorrect_letters)
        #check for new possible solutions

        possible_answers=get_wordom_solutions(words,correct_position_letters,incorrect_position_correct_letters,incorrect_letters,my_guesses)
        if debug: print(len(possible_answers),possible_answers)

        iterations+=1
        #new_guess
        if automated:
            my_guess = random.choice(possible_answers)
        else:
            my_guess = input_wordom(words)
        #Use a scored guess
        #my_guess = pick_word_from_weights(possible_answers, word_weights)

        my_guesses.append(my_guess)
        if debug: print("my guesses =", my_guesses)
        #print(f"New guess: {my_guess}")

        if(iterations==max_attempts):
            break

    if correct_guess:
        print(f"Game {n+1} : Correct, you took {iterations} attempts to get {my_guess}")
    else:
        print(f"Sorry you ran out of guesses to get {my_guess}")
    scores[iterations-1]+=1
    #print(my_guesses)
    for guess in my_guesses:
        word_dict[guess]+=iterations
        #print(word_dict[guess],iterations)
    my_guesses = []

# print(word_dict)
#

# sort_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
# with open('word_scores_from_game.txt','w') as f:
#     for iword in sort_dict:
#         write_string=str(iword[0]) + ", " + str(iword[1]) + "\n"
#         f.write(write_string)

print("Attempts","Score")
for i in range(len(scores)):
    print(str(i+1),scores[i])