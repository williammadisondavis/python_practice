###takes the split function from splitter
from splitter import split
### imports all functions
import splitter
sentence = raw_input("Please enter a sentence:\n")
list_of_words = sentence.split()
dicto = {}


for word in list_of_words:
    if word not in dicto:
        dicto[word] = 1
    else:
        dicto[word] = dicto[word] + 1

##could do

for word in list_of_words:
    if word in dicto:
        dicto[word] = dicto[word] + 1
        # / dicto[word] += 1
    else:
        dicto[word] = 1
print dicto




##### not using split
# turn string into a list of words
#iterate over list and add a new entry for each word not encountered, set value to 1
#for each word that has been seen, add one to the value of the key

sentence = 'to be or not to be'
padded_sentence = sentence + ' '
words = []
curr_word = ''
for char in padded_sentence:
    if char == " ":
        words.append(curr_word)
        curr_word = ''
    else:
        curr_word += char

#there be magic
#append each and every letter into a string variable, once you reach a space you add string to a list, and reset the variable
## append an extra space to the end of the string to deal with end
#words = ['to','be','or','not','to','be']

word_count = {}

for word in sentence:
    if word in word_count:
        word_count[word] = word_count[word] + 1
        # / word_count[word] += 1
    else:
        word_count[word] = 1

