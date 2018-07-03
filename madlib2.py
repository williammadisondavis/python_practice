name = raw_input("What's your name?\n")
sport = raw_input("What is your favorite sport?\n")

def makedict(name,sport):
    maddict = {
        'hisname': '',
        'hissport': '',
    }

    maddict['hisname'] = name
    maddict['hissport'] = sport
    return maddict

bio = makedict(name,sport)



def madlib(name,sport):  
    message = "%s's favorite sport is %s" % (bio['hisname'], bio['hissport'])
    return message
madfunc = madlib(name,sport)


###combine functions
def finalmad(madfunc, makedict):
    name = raw_input("What's your name?\n")
    sport = raw_input("What is your favorite sport?\n")
    