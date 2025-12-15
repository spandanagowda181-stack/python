a=10
b=24
c=24

def mult():
    global a
    a=a+(a*b*c)
    print(a)
mult()