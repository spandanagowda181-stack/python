def person_info(person):
    match person:
        case {"name": name,"age":age}:
            print(f"name:{name},age:{age}")
        case {"name": name}:
            print(f"name:{name},age is not provided")
        case {"age":age}:
            print(f"age:{age},name is not provided")
        case _:
            print("unknown person data")
person_info({"name":"spandana", "age": 19 })
person_info({"name":"manoj"})
person_info({"age":25}) 
person_info({"height":4.6})  
