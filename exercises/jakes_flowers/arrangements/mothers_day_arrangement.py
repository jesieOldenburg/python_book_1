from . import Arrangement
from interfaces.not_refrigerated import INotRefrigerated
class Mothers_day_arrangement(Arrangement, INotRefrigerated):
    """
        A class used to represent a arrangement of flowers
        ...

        Attributes
        ----------
        name : str
            the name of the arrangement
        
        stem_length : int
            the length of each flowers stem in the arrangement
        
        @inherited
        flower_list : list
            a list obj that contains the flowers within the arrangement
        
        Methods
        -------
        display_flowers(self)
            prints the flowers in the arrangement
        
        @inherited
        add_flower(self, flower)
            takes a flower and appends it to the flower_list attribute
        
        @inherited
        print_flowers(self)
            iterates through the flowers list and prints each flower
    """
    
    def __init__(self):
        super().__init__()
        INotRefrigerated.__init__(self)
        self.name = "Mother's Day Bouquet"
        self.stem_length = 7
       
    def add_flower(self, flower):
        try:
            if flower.refrigerated == False:
                self.flower_list.append(flower)
                print(f'You added a {flower.name} to the {self.name}')
        except AttributeError:
            raise AttributeError(f'You CANNOT add a refrigerated flower to the {self.name}')