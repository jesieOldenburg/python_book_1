from movements import IWalking, ISwimming # Import the INTERFACES from the movements package

# DEFINE a new class...
class Penguin(IWalking, ISwimming): # Pass the 2 interfaces & a CLASS CONSTRUCTION ARGUMENT {name} (initialize the properties on each object of the the class)
    def __init__(self, name):
        IWalking.__init__(self)
        ISwimming.__init__(self)
        self.name = name

    def run(self):
        print(f'{self.name} waddles')
    
    def __str__(self):
        return f'{self.name} the Penguin'