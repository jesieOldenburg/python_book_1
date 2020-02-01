class Arrangement:
    def __init__(self):
        self.flower_list = []
        
    def __str__(self):
        return 'This is flower list {self.flower_list}'
    
    def display_flowers(self):
        for flower in self.flower_list:
            print(f'{self.name} contains {flower}\n')
            
    
    # def print_flowers(self):
            # print(self.flower_list[0])
            # print('YOU ARE PRINTING')