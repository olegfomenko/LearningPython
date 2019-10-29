if 5 > 4:
    print("YES")
else:
    print("NO")


a, b = 1, 2
print(a > b)
print(a == b)

if a == b:
    print("Equals!")
else:
    print("No")


t = True
f = False

#######################################################

# True
print(not f)
# False
print(not t)
# True
print(not (t == f))

#######################################################

# True
print(t or f)
# False
print(f or f)

# 1
print(0 or 1)
# 0
print(0 or 0)

#######################################################

# False
print(t and f)
# True
print(t and t)

#######################################################

# prints Ok
if (t and t) or (f and f):
    print("OK")
else:
    print("OOPS")