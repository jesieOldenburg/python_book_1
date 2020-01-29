from . import Flower
from interfaces.refrigerated import IRefrigerated
class Alstroemeria(Flower, IRefrigerated):
    def __init__(self):
        IRefrigerated.__init__()
        self.name = "Alstroemeria"
        
    def __str__(self):
        return f'You now have a {self.name}'