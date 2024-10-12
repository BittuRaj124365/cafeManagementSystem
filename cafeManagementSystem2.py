# we will use Dictionary to store item and price as key value pairs

menu={
    'Salad':19,
    'Tea':29,
    'Coffee':89,
    'Pasta':49,
    'Pizza':69,
    'Burger':39,
    'Momos':59,
}
        # Greetings
print("<----Welcome to the RESTAURANT----->")
    # menu
print("Salad:    Rs19\nTea:    Rs29\nPasta:    Rs49\nCoffee:    Rs89\nPizza:    Rs69\nBurger:    Rs39\nMomos:    Rs59\n")

orderBill=0
while True:
    item_1=input("Order your item --> ")
    if item_1 in menu:
        orderBill+=menu[item_1]
    else:
        print(f"Your order {item_1} is not available in the Menu. Pleas order something else.")
    anotherOrder=input("Do you want to place something else.\n----(yes/no)----\n")
    if anotherOrder=="yes" or anotherOrder=="Yes":
        item_2=("Place your another order. --> ")
        if item_2 in menu:
            orderBill+=menu[item_2]
    else:
        lastOrder=input("Don't you want to place any more orders.\n----(Yes/No)----\n")
        if lastOrder=="Yes" or lastOrder=="yes":
            print("Thank You for visiting this Restaurant.")
            break    
print(f"Your bill is: {orderBill}")
print("Plz, visit again.")