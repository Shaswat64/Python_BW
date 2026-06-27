# list is a data type/ same as array

a = [1, 2, 3, 4, 5]
print(a)
print(type(a))

print(a[0])
print(a[-4])

print(len(a))

a = [1, 2, 3]
a[0] = 100
print(a)

a = [1, 2, 3, 4, 5, 6]
print(a[2:4])
print(a[2:])
print(a[:4])
print(a[:])


# append
a = [1, 2, 3]
a.append(4)
print(a)

# insert
a = [1, 2, 3, 5, 6]
a.insert(3, 8)  # (position, element to be added in the list)
a.insert(1, 600)
a.insert(2000, 2)  # last ma rakhdinxa

# extend
a = [1, 2, 3]
b = [4, 5, 6]

b.extend(a)  # b is extended with elements of a
print(b)  # b is changed but a remains the same
print(a)

# concat
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
c = a + b + a
print(c)
