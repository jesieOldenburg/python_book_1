from . import Flower

class Lilly(Flower):
    def __init__(self):
        self.name = "Lilly"
        
    def __str__(self):
        return f'You now have a {self.name}'