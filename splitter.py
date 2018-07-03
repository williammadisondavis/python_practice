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