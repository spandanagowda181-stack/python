def fun1(name):
    def fun2():
        return f"hello {name}"
    return fun2
f=fun1("spandana")
print(f())


