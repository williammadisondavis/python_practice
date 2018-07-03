
##smallest

def find_smallest_number(nums):   
    smallest = nums[0]
    for i in nums:
        if i < smallest:
            smallest = i
    return smallest
nums = [14, 62, 75, 6, 9, 2, 350]
smallest = find_smallest_number(nums)
print smallest
print "$$$"

####
nums = [14, 62, 75, 6, 9, 2, 350]
for i in nums:
    if i % 2 == 0:
        print i
###
nums = [14, 62, 75, 6, 9, 2, 350, -5]
for i in nums:
    if i > 0:
        print i
###
nums = [14, 62, 75, 6, 9, 2, 350]
posnums = [0]
for i in nums:
    if i > 0:
        posnums.append(i)
print posnums
###
nums = [14, 62, 75, 6, 9, 2, 350]
posnums = [0]
factor = 4
for i in nums:
    if i > 0:
        posnums.append((i) * factor) 
print posnums
###
list1 = [2, 4, 5]
list2 = [2, 3, 6]

print ">>>>>"
def multiply_lists(list1, list2):
    mpliedlist = []
    for i in range(0,len(list1)):
        mpliedlist.append(list1[i] * list2[i])
    return mpliedlist
mpliedlist = multiply_lists(list1, list2)
print mpliedlist
print "<<<<<<"


###
m1 = [
    [2, 4],
    [3, 5]
]
m2 = [
    [9, 2], 
    [2, 6]
]
result = []
for row in m1:
    currentrow = []
    
    for _ in row:
        currentrow.append(0)
    result.append(currentrow)
## creates a 2x2 matrix with 0's filled in
print "stalling"
##about to add up the matrices and put the results into the new matrix

width = len(result[0])
height = len(result)

for i in range(len(m1)):
    for j in range(len(m1[i])):
        sum = m1[i][j] + m2[i][j]
        result[i][j] = sum
print result
###
