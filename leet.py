message = "this is a string that will be converted to leetspeak"

def leet(message):
    leet = ["a", "e", "g", "i", "o", "s", "t"]
    l33t = ["4", "3", "6", "1", "0", "5", "7"]
    new_string = ""
    for letter in message:
        if letter in leet:
            for j in range(len(leet)): 
                if letter == leet[j]:
                    new_string += l33t[j]
                    break
        else:
            new_string += letter
    return new_string

print leet(message)

############################

def l33t(paragraph):
    subs = {
        'A': '4',
        'E': '3',
        'G': '6',
        'I': '1',
        'O': '0',
        'S': '5',
        'T': '7'
    }
    new_paragraph = ''
    for letter in paragraph:
        upper = letter.upper()
        if upper in subs:
            #paragraph[i] = subs[letter]
            letter = subs[upper]
        new_paragraph += letter
        
    return new_paragraph

sentence = 'Hello World'
result = l33t(sentence)
print result

#!!! understand iterators and whether they take the index or the value