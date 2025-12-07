name={
    "spandu":"future engineer",
    "manoj":"future developer",
    "s data":"24-08-2006",
    "m data":"3-01-2010"
}
print(name)
print(name["spandu"])
print(name["manoj"])
print(name.get("spandu"))
print(name.get("s data"))
print(name.get("spandu","not found"))
print(name.get("man","1-5-9088"))
print(name.keys())
print(name.values())
name["john"]="future scientist"
name["spandu"]="future data analyst"
print(name)
name.pop("manoj")
print(name)
newname={
    "ram":"future doctor",
    "shyam":"future lawyer",
    "sayan":"future teacher"
}
name.update(newname)
print(name)
new2name={
    "prema":"future pilot",
    "anjali":"future chef",
    "siya":"future artist"
}
name.update(new2name)
print(name)
name.clear()
print(name)
spa={
    "name":"spandu",
    "age":7,
    "class":"2nd",
    "section":(1,3,4,),
    "werfgh":[1,3,4,5] #mutable therefore not allowed

    }
print(spa)
spa.clear()
print(spa)
