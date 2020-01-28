from . import Flower

class Poppy(Flower):
    def __init__(self):
        self.name = "Poppy"
        
    def __str__(self):
        return f'You now have a {self.name}'