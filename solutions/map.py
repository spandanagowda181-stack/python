
s=['1','4','8','9']
res=map(int,s)
print(list(res))
r=[1,2,3,4,5,6]
re=map(float,r)
print(list(re))

#by using functions
def square(var):
    return var**2
a=[1,2,3,4]
resu=list(map(square,a))
print(resu)
#example 2
def mul(num):
    return num*2
t=[2,4,7,8]
f=list(map(mul,t))
print(f)
