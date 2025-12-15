cities=["Hassan","mangalore","mysore","chikamagalore","Davanagare"]
for index,city in enumerate(cities):
    print(f"index of {city} is {index}")

for city in cities:
    if city=="Hassan":
        break
        print('Hasssan is found')
    else:
        print(f"{city} is not found")