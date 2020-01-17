class Car:
    def __init__(self):
        self._price = 0
        
    @property
    def price(self):
        print('Getter method called for')
        return self._price
    
    @price.setter # this syntax is always the property you want to set followed by the .setter decorator
    def price(self, price):
        print('Setter method called')
        self._price = price
            
dodge = Car()
dodge.price = 47000
print(dodge.price)

chevy = Car()
chevy.price = 34000
print(chevy.price)