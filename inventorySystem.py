import logging
from datetime import datetime

# logger

def logger_helper():
    logging.basicConfig(filename='/Users/hammdone/PycharmProjects/PythonProject/codeLogs.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s')
    return logging.getLogger(__name__)

logger = logger_helper()

# categories set
categories = {}

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

# inventory dictionary for storing items throughout
inventory = {}

# decorator
def decorator(func, m):
    def wrapper(*args, **kwargs):
        logger.info(f"Action: {m}")
        func(*args, **kwargs)
    return wrapper

# helper functions
def add_product(name, price, quantity, category):
    inventory[name] = Product(name, price, quantity, category)
    logger.info(f"Product {name} added to inventory.")

def update_quantity(name, change):
    inventory[name].quantity += change
    logger.info(f"Quantity for {name} is updated to {inventory[name].quantity}")

def remove_product(name):
    if name in inventory:
        del inventory[name]
        logger.info(f"Product {name} removed from inventory.")
    else:
        logger.info(f"Product {name} not found in inventory.")

def display_inventory():
    print("\n------------------- Inventory -------------------")
    for name in inventory.values():
        name.display_info()
        print("-" * 40)

def search_product(name):
    if name in inventory:
        print("-" * 30)
        inventory[name].display_info()
        print("-" * 30)
    else:
        logger.info(f"Product {name} not found in inventory.")

def update_actions(newActions, myList):
    if len(myList) > 2:
        del myList[0]
    myList.append(newActions)

    logger.info(f"Last 3 Actions: {myList}")
    for i in myList:
        # print(i)
        logger.info(i)

# applying decorator
add_product = decorator(add_product, "Adding a product")
update_quantity = decorator(update_quantity, "Updating quantity")
remove_product = decorator(remove_product, "Removing a product")
display_inventory = decorator(display_inventory, "Displaying inventory")
search_product = decorator(search_product, "Searching product")

def main():
    exit = False
    lastActions = ()

    while not exit:
        try:
            print("\n\nMenu: \n1. Add Product \n2. Update Quantity \n3. Remove Product \n4. Display Inventory \n5. Search Product \n6. Exit")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                n = str(input("\nEnter new product name: ")).title()

                if n in inventory:
                    raise ValueError("Name already exists")

                p = float(input("Enter new product price: "))
                q = int(input("Enter new quantity: "))
                category = str(input("Enter category of item: "))
                add_product(n.title(), p, q, category.title())

                newActions = (f"Added {n}")
                my_list = list(lastActions)
                update_actions(newActions, my_list)
                lastActions = tuple(my_list)

            elif choice == "2":
                n = str(input("\nEnter product name: ")).title()
                if n in inventory:
                    print(inventory[n].display_info())
                else:
                    raise Exception("Product not found")

                c = int(input("Enter number to +- from existing quantity: "))

                update_quantity(n, c)

                newActions = (f"Changed quantity of {n}")
                my_list = list(lastActions)
                update_actions(newActions, my_list)
                lastActions = tuple(my_list)


            elif choice == "3":
                n = input("\nEnter product name that you want to remove: ")
                remove_product(n.title())

                newActions = (f"Removed {n}")
                my_list = list(lastActions)
                update_actions(newActions, my_list)
                lastActions = tuple(my_list)

            elif choice == "4":
                display_inventory()

                newActions = ("Displayed inventory.")
                my_list = list(lastActions)
                update_actions(newActions, my_list)
                lastActions = tuple(my_list)

            elif choice == "5":
                search_product(str(input("Enter product name: ")).title())

                newActions = ("Searched for a product.")
                my_list = list(lastActions)
                update_actions(newActions, my_list)
                lastActions = tuple(my_list)

            elif choice == "6":
                exit = True

            else:
                raise Exception("Invalid choice. Choose a number between 1 and 6.")

        except Exception as e:
            # print(f"\nError: {e} \nTry again.")
            logger.error(e)

main()