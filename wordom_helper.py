from wordom_functions import get_wordom_solutions

words=[]

with open("wordlist.txt") as f:
    for aword in f:
        words.append(aword.strip("\n"))
words.sort()
print(words)

correct_position_letters = input("Enter known letters in correct position e.g a**r* :")
print(correct_position_letters)
incorrect_position_correct_letters = input("Enter known letters in incorrect position e.g. f**** :")
print(incorrect_position_correct_letters)
incorrect_letters = input("Incorrect letters :")
print(incorrect_letters)

if len(correct_position_letters) != 5:
    print("Error - sum needs to be 5 characters")

print("Input ok ..continuing")


possible_answers=get_wordom_solutions(words,correct_position_letters,[incorrect_position_correct_letters],incorrect_letters,[])

print(possible_answers)
print(len(possible_answers))







