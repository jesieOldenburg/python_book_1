from animals import Penguin, PaintedDog
from habitats import Habitat, Aquarium

hank = Penguin("Hank")
scott = PaintedDog("Scott")
    
sea_world = Aquarium("Sea World")
sea_world.add_swimmer_pythonic(scott)
sea_world.add_swimmer_pythonic(hank)

for animal in sea_world.animals:
    print(f'{animal} lives in Seaworld')