# Pizza Order Homework

def create_order():
    crust = input("please enter what type of crust you would like: ")
    toppings = input("please enter what toppings you would like: ")
    sauce = input("please enter what sauce you would like: ")
    sides = input("please enter what sides you would like: ")

    pizza_order = {
        'crust': crust,
        'toppings': toppings,
        'sauce': sauce,
        'sides': sides
         }

    return pizza_order

print(create_order())