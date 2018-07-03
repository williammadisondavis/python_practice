today_seats = [
    "Xavier",
    "Clinton",
    "Andrew",
    "Jimmy"
]

yesterday_seats = [
    "Xavier",
    "Andrew",
    "Clinton",
    "Jimmy"
]

current_row = 0

for student in today_seats:
    print student

while current_row < len(today_seats):
    if today_seats[current_row] == yesterday_seats[current_row]:
        print "Move to another seat, %s" % today_seats[current_row]
    current_row += 1

for i in range(len(today_seats)):
    print today_seats[i]