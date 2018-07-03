boxof = ["nail", "jar", 5, 12, 16, 5, "jar", "dog"]
box3 = []
for items in boxof:
    if items not in box3:
        box3.append(items)
print box3