from . import Flower

class Rose(Flower):
    def __init__(self):
        self.name = "Rose"
        
    def __str__(self):
        return f'You now have a {self.name}'