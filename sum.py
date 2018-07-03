numbers = range(10)
def sum(list1):
    total = 0
    for i in list1:
        if i%3 == 0 or i%5 == 0:
            total+=i
    return total
print(sum(numbers))

#------------- fibonacci
