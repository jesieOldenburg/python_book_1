from . import Flower
from interfaces.refrigerated import IRefrigerated

# Goes in valentines day arrangement
# Is refrigerated
class Alstroemeria(Flower, IRefrigerated):
    def __init__(self):
        super().__init__()
        IRefrigerated.__init__(self)
        self.name = "Alstroemeria"
        
    def __str__(self):
        return f'A {self.name}\n'