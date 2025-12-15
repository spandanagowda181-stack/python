# Without list comprehension
a = []
for i in range(8):
    a.append(i**2)

# With list comprehension
b = [i**2 for i in range(8)]

print("Using Loop: ", a)
print("Using List Comprehension: ", b)