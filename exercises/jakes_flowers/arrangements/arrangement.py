class Arrangement:
    def __init__(self):
        self.flower_list = []
        
    def __str__(self):
        return 'This is flower list {self.flower_list}'
        
    def print_flowers(self):
        for flower in self.flower_list:
            print(self.flower_list[0])