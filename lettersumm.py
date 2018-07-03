#Please enter a word: banana
#{'a': 3, 'b': 1, 'n': 2}

prompt = raw_input("Please enter a word:\n")

dicto = {}

for char in prompt:
    if char not in dicto:
        dicto[char] = 1
    else:
        dicto[char] = dicto[char] + 1