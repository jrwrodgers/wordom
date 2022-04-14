

def get_wordom_solutions(wordlist,correct_position_letters,incorrect_position_correct_letters,incorrect_letters,my_guesses):
    possible_words=[]
    # Loop to find words with correct letters in position

    #if any matching letters
    any_letters=True
    if correct_position_letters.count("*")==5:
        any_letters=False

    if(any_letters):
        for word in wordlist:
            match = True
            for i in range(5):
                if correct_position_letters[i]!='*':
                    if word[i]!=correct_position_letters[i]:
                        match=False
            if match:
                possible_words.append(word)
    else:
        possible_words=wordlist

    #loop to find words with correct letters
    possible_words2=[]

    for word in possible_words:
        match = True
        for iword in incorrect_position_correct_letters:
            for s in iword:
                if s != "*":
                    if s in word:
                        if match != False:
                            match = True
                    else:
                        match = False
                for i in range(5):
                    if iword[i]!='*':
                        if word[i]==iword[i]:
                            match=False

        if match==True:
            possible_words2.append(word)
    #print(possible_words2)
    #print(len(possible_words2))

    #loop to eliminate words with incorrect letters
    possible_words3=[]
    for word in possible_words2:
        match = False
        for s in incorrect_letters:
            if s in word:
                match = True
            else:
                if match != True:
                    match = False
        if match == False:
            possible_words3.append(word)
    #print(possible_words3)
    #print(len(possible_words3))

    #remove already guessed form possible
    for word in my_guesses:
        if word in possible_words3:
            possible_words3.remove(word)

    return(possible_words3)




def check_wordom_solution(guess,word,correct_position_letters,incorrect_position_correct_letters,incorrect_letters):
    #correct_position_letters=[]
    #correct_letters=[]
    #incorrect_letters=[]

    for i in range(5):
        if correct_position_letters[i] =="*":
            if(guess[i]==word[i]):
                correct_position_letters[i]=word[i]
            else:
                correct_position_letters[i]="*"

    new_incorrect_pos=[]
    for i in range(5):
        if guess[i] in word:
            if guess[i] != word[i]:
                new_incorrect_pos.append(guess[i])
            else:
                new_incorrect_pos.append("*")
        else:
            new_incorrect_pos.append("*")
    incorrect_position_correct_letters.append(new_incorrect_pos)
    # for myletter in guess:
    #     for letter in word:
    #         if myletter == letter:
    #             if myletter not in incorrect_position_correct_letters:
    #                 if myletter not in correct_letters:
    #                     correct_letters.append(myletter)

    for myletter in guess:
        if myletter not in word:
            if(myletter not in incorrect_letters):
                incorrect_letters.append(myletter)

    return(correct_position_letters,incorrect_position_correct_letters,incorrect_letters)

def create_word_weightings(words):
    letter_freq = [0] * 26
    # get frequency of each letter
    for word in words:
        for letter in word:
            # print(ord(letter))
            letter_freq[ord(letter) - 97] += 1

    for i in range(len(letter_freq)):
        print(chr(i + 97), letter_freq[i])

    word_score = []
    for word in words:
        sum = 0
        unique_letters = ''.join(set(word))
        for s in unique_letters:
            # print(s, ord(s)-97)
            sum += letter_freq[int(ord(s) - 97)]
        word_score.append(sum)

    max_index = word_score.index(max(word.score))
    best_word = words[max_index]
    return word_score, best_word


def pick_word_from_weights(words,weights):
    weightings=[]
    for word in words:
        weightings.append(weights[word])

    max_index=weightings.index(max(weightings))
    best_word=words[max_index]
    return best_word