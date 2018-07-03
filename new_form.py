name = raw_input('What is your name?\n')
message = ("Hello %s !" % name).upper()
length = len(name)
print message
print "YOUR NAME HAS " + str(length) + " " + "LETTERS IN IT!"