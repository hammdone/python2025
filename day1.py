categories = {"Electronics", "Food"}

class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def display_info(self):
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Quantity: ", self.quantity)
        print("Category: ", self.category)

inventory = {}

def add_product(inventory, name, price, quantity, category):
    inventory[name] = Product(name, price, quantity, category)
    print(f"Product {name} added to inventory.")

def update_quantity(inventory, name, change):
    inventory[name].quantity += change
    print(f"Quantity for {name} is updated to {inventory[name].quantity}")

def remove_product(inventory, name):
    del inventory[name]
    if name in inventory:
        print(f"Product {name} removed from inventory.")
    else:
        print(f"Product {name} not found in inventory.")

def display_inventory(inventory):
    print("\n------------------- Inventory -------------------")
    for name in inventory.values():
        name.display_info()
        print("-" * 20)

def search_product(inventory, name):
    if name in inventory:
        print("-" * 30)
        inventory[name].display_info()
        print("-" * 30)
    else:
        print("\nProduct was not found.")

def updateActions(newActions, myList):
    if len(myList) > 2:
        del myList[0]
    myList.append(newActions)

    print("\nLast Actions: ")
    for i in myList:
        print(i)

def main():
    exit = False
    lastActions = ()

    while not exit:
        print("\n\nMenu: \n1. Add Product \n2. Update Quantity \n3. Remove Product \n4. Display Inventory \n5. Search Product \n6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            n = str(input("\nEnter new product name: ")).title()
            p = int(input("Enter new product price: "))
            q = int(input("Enter new quantity: "))
            category = str(input("Enter category of item: ")).title()

            add_product(inventory, n, p, q, category)

            newActions = (f"Added {n}")
            my_list = list(lastActions)
            updateActions(newActions, my_list)
            lastActions = tuple(my_list)

        elif choice == "2":
            n = str(input("Enter product name: ")).title()
            if n in inventory:
                print(inventory[n].display_info())
            else:
                print("Product not found")
            c = int(input("Enter number to +- from existing quantity: "))
            update_quantity(inventory, n, c)

            newActions = (f"Changed quantity of {n}")
            my_list = list(lastActions)
            updateActions(newActions, my_list)
            lastActions = tuple(my_list)

        elif choice == "3":
            n = input("Enter product name that you want to remove: ")
            remove_product(inventory, n.title())

            newActions = (f"Removed {n}")
            my_list = list(lastActions)
            updateActions(newActions, my_list)
            lastActions = tuple(my_list)

        elif choice == "4":
            display_inventory(inventory)

            newActions = ("Displayed inventory.")
            my_list = list(lastActions)
            updateActions(newActions, my_list)
            lastActions = tuple(my_list)

        elif choice == "5":
            search_product(inventory, str(input("Enter product name: ")).title())

            newActions = ("Searched for a product.")
            my_list = list(lastActions)
            updateActions(newActions, my_list)
            lastActions = tuple(my_list)

        else:
            exit = True

main()