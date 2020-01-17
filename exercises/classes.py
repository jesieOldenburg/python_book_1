class Pizza: # Declare a new Class for pizza's
    # Define the init function, adding the self param to ensure each created instance is assigned the correct properties and values.
    def __init__(self): 
      self.name = ''
      self.crust = ''
      self.size = 14
      self.toppings = list()
      
    # Create a method to add toppings to the Classe's toppings property.
    def add_topping(self, topping):
        """Method to add toppings to the Class property named toppings 
        
        Arguments:
            topping {[list]} -- List of string types
        """
        self.toppings.append(topping)
    
    # Create a method to describe the Classes 
    def describe_pizza(self):
        all_the_fixins = ', '.join(self.toppings)
        print(f'You ordered a {self.size} inch {self.name} with a {self.crust} crust. Your toppings are {all_the_fixins}. Enjoy your hot zaa!\n')


pepperoni = Pizza() # Create a new instance of the Pizza Class

# Assign values to the classes properties
pepperoni.name = 'Pepperoni' 
pepperoni.crust = 'Thin'
pepperoni.add_topping('Cheese')
pepperoni.add_topping('Pepperoni')
pepperoni.add_topping('Pizza Sauce')
pepperoni.describe_pizza()

supreme_pizza = Pizza()

supreme_pizza.name = 'Supreme'
supreme_pizza.crust = 'Chicago Deep Dish'
supreme_pizza.add_topping('Bell Peppers')
supreme_pizza.add_topping('Olives')
supreme_pizza.add_topping('Sausage')
supreme_pizza.add_topping('Onions')
supreme_pizza.add_topping('Tomato')
supreme_pizza.add_topping('Feta Cheese')
supreme_pizza.add_topping('Bacon')
supreme_pizza.describe_pizza()