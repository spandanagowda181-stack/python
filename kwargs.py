def fun(**kwargs):
    for k, val in kwargs.items():
        print(f"{k}: {val}")

# Calling the function with keyword arguments
fun(name="Alice", age=30, city="New York")