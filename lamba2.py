# without lambda function
def check(x):
    if x%2==0:
        print("x is even ")
    else:
        print("x is odd")
check(8)
check(9)
#with lambda function
check=lambda x:"even" if x%2==0 else "odd"
print(check(5))
add=lambda a,b: a+b
print(add(1,4))