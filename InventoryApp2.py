class Product:
    def __init__(self, name, width, length, height, weight_ofcase, UPC, quantity):   #the __init__() is a method. Initializer, constructor.
        self.name = name  #parameters are the variables attached to the method.
        self.width = width
        self.length = length
        self.height = height
        self.weight_ofcase = weight_ofcase
        self.UPC = UPC
        self.quantity = quantity
        print("Product Created")
        
class New_Product:
    def __init__(self, new_name, new_width, new_length, new_height, new_weight_ofcase, new_UPC, new_quantity):
        self.new_name = new_name  # parameters are the variables attached to the method.
        self.new_width = new_width
        self.new_length = new_length
        self.new_height = new_height
        self.new_weight_ofcase = new_weight_ofcase
        self.new_UPC = new_UPC
        self.new_quantity = new_quantity
        print("New Product Created.")

class Inventory:
    def __init__(self, name, max_products):
        self.name = name
        self.max_products = max_products
        self.products = []

    def add_product(self):
        if len(self.products) < (self.max_products):
            self.products.append(self.products)
            return True
        return False


p = Product(input("Name of Product: "), float(input("Width of case: ")), float(input("Length of case: ")), float(input("Height of case: ")),
            float(input("Weight of case: ")), input("Enter UPC: "), input("Enter amount of pieces: "))  #This is how you create a new product.

"""
inventory = Inventory(float(input("Enter name of Product: ", 10)))
inventory.add_product(p)
inventory.add_product(p1)
"""

weightofcase = p.weight_ofcase #This gets the attribute within p.

#I need to figure out how to add more product and for it to select on the different products.

def casesremaining(total_cases, cases_selected):
    return total_cases - cases_selected

def totalweight(weightofcase, total_cases):
    return weightofcase * total_cases

def weightofcasesselected(cases_selected, weightofcase ):
    return cases_selected * weightofcase

#total_cube_pallet_capacity = float(input("Enter cube capacity of a pallet: ")) ***NOT TO BE INCLUDED, YET***
total_cases = int(input("Enter amount of total cases on pallet: ")) #problem is not changing the value after input.
total_weight = totalweight(float(weightofcase), float(total_cases))
application = 1
yes = "Yes"
no = "no"

print("Product added to pallet.")
print("Total weight of pallet is: ", total_weight)
print("Total amount of cases on a pallet is: ", total_cases)

while application == 1: #COuld use "for cases in pallet():"
    case_selection = (input("Do you want to select a case? y/n: "))
    if case_selection == "y":
        select = int(input("How many cases would you like to select? "))
        cases_selected = select
        totalweigthofcasesselected = weightofcasesselected(float(cases_selected), float(weightofcase))

        def remainingweight(total_weight, totalweigthofcasesselected):
            return total_weight - totalweigthofcasesselected

        remaining_weight = remainingweight(float(total_weight), float(totalweigthofcasesselected))
        if cases_selected == select:
            totalcasesremaining = casesremaining(int(total_cases), int(cases_selected))
            total_cases = totalcasesremaining #Forgot to update the original variable from input.
            total_weight = remaining_weight #Same here. Remember to update variables as the program goes.
            print("Total weight now is: ", remaining_weight)
            print("You know have ", totalcasesremaining, " cases remaining.")
            #continue -this needed to be commented out to keep the program going into the next statement.
        if total_cases == 0: #new part 10/1/2020
            print("Your total amount of cases on the pallet is ", totalcasesremaining, ".")
            print("You have no more cases on the pallet.")
            no = "no"
            add = "add"
            change = "change"
            add_cases = input("Would you like to add more cases on the pallet, or change product? (add/change/n) ")
            if add_cases == add:
                cases_to_add = int(input("How many cases would you like to add? "))
                total_cases = cases_to_add+totalcasesremaining
                total_weight = weightofcase*cases_to_add
                print("You have added to your pallet, ", cases_to_add, " more cases.")
                print("Your total cases on pallet now is: ", total_cases, ".")
                print("Your total weight of pallet now is: ", total_weight, ".")
            elif add_cases == change: #added on 10/12/2020 - May not work.
                new_p = New_Product(input("Name of Product: "), float(input("Width of case: ")), float(input("Length of case: ")), float(input("Height of case: ")),
                                    float(input("Weight of case: ")), input("Enter UPC: "), input("Enter amount of pieces: "))
                weightofcase = new_p.new_weight_ofcase  # This gets the attribute within p.
                total_cases = int(input("Enter amount of total cases on pallet: "))  # problem is not changing the value after input.
                total_weight = totalweight(float(weightofcase), float(total_cases))
                print("New Product added to pallet.")
                print("Total weight of pallet is: ", total_weight)
                print("Total amount of cases on a pallet is: ", total_cases)
                continue
            else:
                if add_cases == no:
                    print("Thank you for using our application.")
                    break
    else:
        if case_selection == no or application == 0:
            print("Thank you for using our application.")
            break

#add option to add more products.



"""
    "Also add the time each change has happened with date."
    "The app should be able to calculate total amount of cases by the weight of each individual case.\n",
    "\n",
    "App should recognize different amount of cases per pallet, due to the weight. \n",
    "\n",
    "When you remove a case it should subtract the case from total amount. \n",
    "\n",
    "When you add a case it should add a case to the total amount. \n",
    "\n",
    "**Maybe you can add dimensions to specify the different types of products???**\n",
    "\n",
    "You should be able to input the product ID.\n",
    "\n",
    "You should be able to add UPC.\n",
    "\n",
    "**Potentially both should be linked.**\n",
    "\n",
    "Possibly inputting the amount of cases a pallet can hold? Then divide?\n",
    "\n",
    "**It should be subtract due to you should be able to input total initial cases and go from there.**\n",
    "\n",
    "Where or what can you use in order to keep multiple values(multiple locations holding cases) so that the app can continue to keep track of inventory? \n",
"""
