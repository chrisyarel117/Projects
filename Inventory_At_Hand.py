class Inventory:
    def __init__(self, name, width, length, height, weight_of_case, UPC, quantity):    #the __init__() is a method. Initializer, constructor.
        self.name = name  #parameters are the variables attached to the method.
        self.width = width
        self.length = length
        self.height = height
        self.weight_of_case = weight_of_case
        self.UPC = UPC
        self.quantity = quantity
        product_description = ""

    def product_description(self):
        print("Item brand: {name}, Product Description: {width}, {length}, {height}, {weight_of_case}, {UPC}, {quantity}"
              .format(name = self.name, width = self.width, length = self.length, height = self.height,
                      weight_of_case = self.weight_of_case, UPC = self.UPC, quantity = self.quantity))

class Toilet_Paper(Product):
    pass

Charmin = Toilet_Paper("Charmin", "Width: 4", "length: 10", "height: 3", "weight_of_case: 2",
                           "UPC: 1234500", "Quantity: 100")

Great_Value = Toilet_Paper("Great Value", "Width: 3", "length: 6", "Height: 4", "weight_of_case: 8",
                           "UPC: 543211", "Quantity: 10")

Charmin.product_description()
Great_Value.product_description()

#Create a function that displays the amount of product that is stored in file.

