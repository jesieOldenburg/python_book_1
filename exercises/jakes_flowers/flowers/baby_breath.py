from . import Flower

class Baby_breath(Flower):
    def __init__(self):
        self.name = "Baby's Breath"
        
    def __str__(self):
        return f'You now have a {self.name}'