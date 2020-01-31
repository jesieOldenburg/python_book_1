from . import Flower
from interfaces.refrigerated import IRefrigerated

# Goes in the valentines day arrangement
# Is refrigerated
class Rose(Flower, IRefrigerated):
    def __init__(self, color=''):
        super().__init__()
        IRefrigerated.__init__(self)
        self.name = "Rose"
        self.available_colors = ['Red', 'Pink', 'Blue']
        self.color = color
        
    def __str__(self):
        return f'The new instance of {self.name} has the following properties => {self.__dict__}\n'