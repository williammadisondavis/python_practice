maxrows = int(raw_input("How tall do you want your pyramid?"))
for rownum in range(1,maxrows + 1):
    spaces = " " * (maxrows - rownum)
    stars = "*" * (rownum * 2 - 1)
    print spaces + stars + spaces
for rownum in range(maxrows -1, 0, -1):
    spaces = " " * (maxrows - rownum)
    stars = "*" * (rownum * 2 - 1)
    print spaces + stars + spaces