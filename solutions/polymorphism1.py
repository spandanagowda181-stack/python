class calculator:
    def mutiply(self,a=6,b=2,*args):
        result=a*b
        for num in args:
            result*=num
            return result
cal=calculator()
print(cal.mutiply())
print(cal.mutiply(8))
print(cal.mutiply(2,3,4))
print(cal.mutiply(2,5))