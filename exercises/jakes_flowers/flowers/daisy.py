from . import Flower
from interfaces import INotRefrigerated

class Daisy(Flower, INotRefrigerated):
    def __init__(self):
        INotRefrigerated.__init__(self)
        self.name = "Daisy"
        
    def __str__(self):
        return f'You now have a {self.name}'