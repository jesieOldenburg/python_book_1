from . import Flower

class Alstroemeria(Flower):
    def __init__(self):
        self.name = "Alstroemeria"
        
    def __str__(self):
        return f'You now have a {self.name}'