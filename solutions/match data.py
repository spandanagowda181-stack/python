def data(num):
    match num:
        case[x]:
            print(f"list with one element:{x}")
        case[x,y]:
            print(f"list with two elements:{x},{y}")
        case[x,y,z]:
            print(f"list with three elements :{x},{y},{z}")
        case _:
            print("unknown data format")
data(10)#unknown data format
data([10])
data([10,20])
data([10,20,30])
data([10,20,30,40])
data({10,20})#unknown data format
# it works for both tuple and lists
data((10,20))