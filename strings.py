lower = ["a"," ", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper = ["A"," ", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",]

given = "the cake is a lie"
new_string = ""
for letter in given:
    if letter in lower:
        for j in range(len(lower)): 
            if letter == lower[j]:
                new_string = new_string + upper[j]
                break
    else:
        new_string += letter
print new_string

## Copy spaces over "as is", so long as it's not uppercase, copy it verbatim

message = 'you shall NOT pass'

upcased = ''

for char in message:
    letter = char
    if char == 'a':
        letter = "A"
    elif char == "b"
        letter = "B"
        #etc..
    upcased = upcased + char

print upcased
## "skeleton" for many copying over exercises

#use two lists, same positions. Search in list to see if it happens to be lowercase letter. 
message = 'you shall NOT pass'

upcased = ''
lowercase = ["a"," ", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A"," ", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",]


for char in message:
    letter = char
    #search thru list of lowercase letters
    for i in range(len(lowercase)):
        lowerletter = lowercase[i]
        if lowerletter == char:
            ##if we find a match we replace it with uppercase. we have kept track of index using i
            ##char will be used to override
            letter = uppercase[i]
            break
            ##break is useful in for loops to not keep looking, not useful for while loops
    upcased = upcased + letter

print upcased
