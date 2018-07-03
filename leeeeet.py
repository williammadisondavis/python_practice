leet = ["a", "e", "g", "i", "o", "s", "t"]
l33t = ["4", "3", "6", "1", "0", "5", "7"]
    newstring = ""
    for letter in message:
        if letter in leet:
            for j in range(len(leet)): 
                if letter == leet[j]:
                    new_string += l33t[j]
                    break
        else:
            new_string += letter
    return newstring