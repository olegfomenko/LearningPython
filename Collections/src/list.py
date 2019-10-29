######## SIMPLE ARRAY ########
##############################

a = [0, 1, 1, 2, 3, 5]
# prints 0
print(a[0])

print("the sum is: ", sum(a))
print("the reverse arr is: ", list(reversed(a)))
print(a)

print("the count of 1: ", a.count(1))

a.append(8)
# [0, 1, 1, 2, 3, 5, 8]
print(a)

# erase the 4th element
a.pop(4)
print(a)

# erase the 8
a.remove(8)
print(a)

# search the element in array
if 1 in a:
    print("Found!")

a.sort()
a.reverse()
print(a)

a.clear()
print(a)

b = list()
print(len(b))

c = [0] * 5
print(c)


