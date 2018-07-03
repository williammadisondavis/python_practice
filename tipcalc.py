tip = raw_input('Be honest m8, how was the service? good, bad, or fair?\n')
if tip.lower() == "good": 
    tip_amt = float(0.20)
elif tip.lower() == "fair":
    tip_amt = float(0.15)
elif tip.lower() == "bad": 
    tip_amt = float(0.10)
#Asks for meal total
bill_input = raw_input('How much was the bill?\n$')
bill = float(bill_input)
#Calculates total tip
tip_ratio = tip_amt * bill
#Calculates total bill including tip and meal
exactotal = tip_ratio + bill
#Prints to user exact tip and new total
print   "Your exact tip should be $%.2f" % tip_ratio
print "Your total will become $%.2f" % exactotal
#Asks about splitting new bill and calculates it
friends = int(raw_input('How many people are you splitting the bill between?\n'))
indtotal = float(exactotal) / friends
#Gives split bill cost
print "Your individual totals will be: $%.2f" % indtotal 