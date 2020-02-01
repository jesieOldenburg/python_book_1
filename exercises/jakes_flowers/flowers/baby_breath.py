from . import Flower
from interfaces import IRefrigerated
class Baby_breath(Flower, IRefrigerated):
    def __init__(self):
        IRefrigerated.__init__(self)
        self.name = "Baby's Breath"
        
    def __str__(self):
        return f'A {self.name}\n'