item1={
    "name":"spandana",
    "age":19,
    "height":5.6
}
item2={
    "name":"manoj",
    "age":15,
    "height":5.7
    
}
item=[item1,item2]
print(item1)
print(item2)
print(item)
print(f"totalage:{item1 ["age"] +item2 ["age"]}")
print(f"average height:{item1["height"]+item2["height"]/2}")
print(f"{item1["name"],item2["name"]}")
item.clear()
d1=dict(name="spandana",age=190)
d2=dict(name="manoj",age=15)
print(d1)
print(d2)
d3=[d1,d2]
print(d3)
print(d2.get("name"))
print(d1.get("age"))
del d1["age"]
print(d1)