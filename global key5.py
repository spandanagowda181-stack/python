a = [10, 20, 30]


def fun():
    for i in range(len(a)):
        a[i] += 10


print("before",a)
fun()
print("after", a)