last = 1
current = 2
total = 0
while total < 400000000000000:
    nxt = last + current
    total = total + current
    last = current
    current = nxt
print total