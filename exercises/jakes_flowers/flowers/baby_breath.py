from . import Flower
from interfaces import INotRefrigerated
class Baby_breath(Flower, INotRefrigerated):
    def __init__(self):
        INotRefrigerated.__init__(self)
        self.name = "Baby's Breath"
        
    def __str__(self):
        return f'A {self.name}\n'