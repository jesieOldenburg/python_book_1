from . import Flower
from interfaces.refrigerated import IRefrigerated

class Rose(Flower, IRefrigerated):
    def __init__(self, color=''):
        IRefrigerated.__init__(self)
        self.name = "Rose"
        self.available_colors = ['Red', 'Pink', 'Blue']
        self.color = color
        
    def __str__(self):
        return f'You now have a {self.color} {self.name}'