start = int(raw_input("What will be the starting number?\n"))
end = int(raw_input("What will be the ending number?\n"))

while start > end:
    print "Your starting number needs to be lesser than your ending number."
    start = int(raw_input("What will be the starting number?\n"))
    end = int(raw_input("What will be the ending number?\n"))
print "\n"



countup = range(start,(end + 1),+1)
for count in countup:
    print count