def check_number(num):
    match num:
        case 1|2|3|4|5 :
            print(f"number: {num} is in between 1 nad 5")
        case 10|20|30 :
            print(f"number:{num} is in bwtween 10 and 30")
        case _:
            print(f"match not found for number:{num}") 
check_number(3)
check_number(20)
check_number(50) 