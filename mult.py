print "This is a multiplication Table!"
height = int(raw_input("How high do you want to get?"))
for i in range(1,height + 1):
    for j in range(1,height + 1): 
        print "%d X %d = %d" % (i,j,i*j)
    print "*" * 10