from . import Arrangement

class Valentines_day_arrangement(Arrangement):

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
        super().__init__(name)
        self.name = "Valentines's Day Bouquet"
        self.stem_length = 7
        
    def display_flowers(self):
        print(f'Your {self.name} contains => {self.print_flowers}')