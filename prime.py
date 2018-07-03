#we start with 18
#from 2-18 find largest prime factor
#iterate to find what numbers go in to create a list [2,3,6,9]
#loop into this list to see if anything goes into the numbers, and if so its not a prime factor
#creating a new list with prime factors
#using a range you can start at 2, go up to but not including the factor itself range(2,2) range(2,3)
#by first dividing by two, you cut out many potential iterations (18=2*3*3) it removes 2 and 9
giantnum = 600851475143
potentials = 1

while potentials < giantnum:
    potentials += 1
    while (giantnum % potentials == 0) and (giantnum != 1):
        giantnum = giantnum / potentials

print potentials

####

hugenum = 600851475143

remainder = hugenum
###factor we are starting with
factor = 2
#factors=[]
while remainder != 1:
    if remainder % factor == 0:
        remainder = remainder / factor #remainder/= factor
    else:
        factor += 1 ##next time it loops will be testing what's not 2
    #if remainder ==1:
        #break

print factor


#When you reach the largest prime factor youll realize remainder = 1 and you will have found largest prime factor
#problem will be done when remainder = 1
# Edge case could be 2, or 18, 45 (its divisible by 3 twice and 5 once)
#using a list will use LOTS of RAM so try not to use one for this kinda problem

