from . import Flower
from interfaces.refrigerated import IRefrigerated

# Goes in valentines day arrangement
# Is refrigerated
class Lilly(Flower):
    def __init__(self):
        super().__init__()
        IRefrigerated.__init__(self)
        self.name = "Lilly"
        
    def __str__(self):
        return f'The new instance of {self.name} has the following properties => {self.__dict__}\n'