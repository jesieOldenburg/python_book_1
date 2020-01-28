from . import Arrangement

class Valentines_day_arrangement(Arrangement):
    def __init__(self):
        super().__init__(name)
        self.name = "Valentines's Day Bouquet"
        
    def display_flowers(self):
        print(f'Your {self.name} contains => {self.print_flowers}')