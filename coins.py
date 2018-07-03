print "You have 0 coins!"
coins = 0
want = "yes"
while want == "yes":
    want = raw_input("Would you like another? Yes or no?")
    if want == "yes":
        coins += 1
        print "You have %i coins" % coins
    if want == "no":
        print "You have %i coins, thanks for playing." % coins
        break