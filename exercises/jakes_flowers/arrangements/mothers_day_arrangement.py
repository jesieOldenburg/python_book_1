from . import Arrangement

class Mothers_day_arrangement(Arrangement):
    def __init__(self):
        super().__init__()
        self.name = "Mother's Day Bouquet"
        
    def display_flowers(self):
        print(f'Your {self.name} contains => {self.print_flowers}')
        