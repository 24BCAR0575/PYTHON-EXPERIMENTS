# Demonstrate various list functions

LIST = [10, 20, 30, 40]

print("Original List:", LIST)

# append()
LIST.append(50)
print("After append:", LIST)

# insert()
LIST.insert(2, 25)
print("After insert:", LIST)

# remove()
LIST.remove(30)
print("After remove:", LIST)

# pop()
LIST.pop()
print("After pop:", LIST)

# extend()
LIST.extend([60, 70])
print("After extend:", LIST)

# sort()
LIST.sort()
print("Sorted List:", LIST)

# reverse()
LIST.reverse()
print("Reversed List:", LIST)

# count()
print("Count of 20:", LIST.count(20))

# index()
print("Index of 40:", LIST.index(40))

# length of list
print("Length of list:", len(LIST))