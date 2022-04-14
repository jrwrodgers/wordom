import itertools
words=[]

with open("wordlist.txt") as f:
    for aword in f:
        words.append(aword.strip("\n"))
words.sort()
#print(words)

letter_freq=[0]*26

#get frequency of each letter
for word in words:
    for letter in word:
        #print(ord(letter))
        letter_freq[ord(letter)-97]+=1

for i in range(len(letter_freq)):
    print(chr(i+97),letter_freq[i])

#assign a density number to each word
word_score=[]
for word in words:
    sum=0
    unique_letters=''.join(set(word))
    for s in unique_letters:
        #print(s, ord(s)-97)
        sum+=letter_freq[int(ord(s)-97)]
    word_score.append(sum)

# for i in range(100):
#     print(words[i],word_score[i])

word_dict={}
# for key in words:
#     for value in letter_freq:
#         word_dict[key] = value
#         letter_freq.remove(value)

word_dict = {words[i]: word_score[i] for i in range(len(words))}

print(str(word_dict))
#order by best words
sort_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

for i in sort_dict:
       print(i[0],i[1])

with open('word_scores.txt','w') as f:
    for i in sort_dict:
        write_string=str(i[0]) + ", " + str(i[1]) + "\n"
        print(write_string)
        f.write(write_string)