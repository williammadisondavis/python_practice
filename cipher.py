shift_num = 13
message = raw_input("What message do you want to encrypt?")
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",]
output = ""
for char in message:
    if char in lowercase:
        for i in range(len(lowercase)):
            if char == lowercase[i]:
                ##append something
                newindex = i + shift_num
                newcharacter = lowercase[newindex]
                output += newcharacter
    elif char in uppercase:
        if char in uppercase:
            for i in range(len(uppercase)):
                if char == uppercase[i]:
                    newindex = i + shift_num
                    newcharacter = uppercase[newindex]
                    output += newcharacter
    else:
        output += char
print output

while newindex > 25:
                    spill = newindex - 25
                    newcharacter = lowercase[spill]
                    output += newcharacter

