class Wings:
    def __init__(self, wings, sauce, flour, seeds):
        self.wings = wings
        self.sauce = sauce
        self.flour = flour
        self.seeds = seeds

    def calculate_rating(self):
        if (self.wings >= 5) and (self.sauce >= 5) and (self.flour >= 5):
            print("Good")
        else:
            print("Avg")

def get_wings():
    try:
        print("-" * 30)
        wings_no = int(input("Please enter number of wings: "))
        if (wings_no < 0):
            raise Exception

        sauce_no = int(input("Please enter number of sauce: "))
        if (sauce_no < 0):
            raise Exception

        flour_no = int(input("Please enter number of flour: "))
        if (flour_no < 0):
            raise Exception

        seeds_no = int(input("Please enter number of seeds: "))
        if (seeds_no < 0):
            raise Exception

        item = Wings(wings_no, sauce_no, flour_no, seeds_no)

        print("Your wings are: ")
        item.calculate_rating()

    except Exception:
        print(f"Invalid input. Please enter positive numbers.")



def main():
    exit = False

    while not exit:
        get_wings()
        choice = input("Do you want to continue? (y/n): ")

        if choice == "n":
            exit = True

main()