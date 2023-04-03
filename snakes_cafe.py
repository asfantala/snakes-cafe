print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**                                  **")
print("** To quit at any time, type 'quit' **")
print("**************************************\n")

print("Appetizers")
print("----------")
print("Wings")
print("Cookcies")
print("Spring Rolls\n")

print("Entrees")
print("-------")
print("Salmon")
print("Steak")
print("Meat Tornado")
print("A Literal Garden\n")

print("Desserts")
print("--------")
print("Ice Cream")
print("Cake")
print("Pie\n")

print("Drinks")
print("------")
print("Coffee")
print("Tea")
print("Unicorn Tears\n")

print("***********************************")
print("** What would you like to order? **")
print("***********************************")

menu = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0
}

while True:
    order = input("> ")

    if order == "quit":
        print("Here is the order:")
        for item, quantity in menu.items():
          if quantity > 0:
           print(f"{quantity} order(s) of {item}")
        break

    if order in menu:
        menu[order] += 1
        print(f" {menu[order]} order of {order} has been added to your meal ")
        print("***************************************************************")
        print("** What would you like to order, if do not want please quit? **")
        print("***************************************************************")
    else:
        print("Sorry, this item is not on the menu. Please choose another choice or quit.")
