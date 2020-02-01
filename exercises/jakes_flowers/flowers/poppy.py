from . import Flower
from interfaces import INotRefrigerated
class Poppy(Flower, INotRefrigerated):
    def __init__(self):
        INotRefrigerated.__init__(self)
        self.name = "Poppy"
        
    def __str__(self):
        return f'A {self.name}\n'