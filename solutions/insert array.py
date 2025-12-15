import array as arr
a=arr.array('i',[1,3,4,6,7,9])
# print("array elements before insertion:",a)
# a.insert(1,5)
# print(a)
print(*a)
a.insert(2,8)
print(*a)