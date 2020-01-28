from . import Flower

class Daisy(Flower):
    def __init__(self):
        self.name = "Daisy"
        
    def __str__(self):
        return f'You now have a {self.name}'