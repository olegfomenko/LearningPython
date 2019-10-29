x = 10
y = 4

print("y in bin:", bin(y))
print("y in hex:", hex(y))

z = x | y
print(bin(x), " OR ", bin(y), " = ", bin(z))

z = x & y
print(bin(x), " AND ", bin(y), " = ", bin(z))

z = x ^ y
print(bin(x), " XOR ", bin(y), " = ", bin(z))
