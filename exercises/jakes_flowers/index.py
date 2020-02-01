import os
# import sys
# sys.path.append('/Users/newuser/python_workspace/python_book_1/exercises/jakes_flowers')
from flowers import Flower, Rose, Daisy, Alstroemeria, Lilly, Baby_breath, Poppy
from arrangements import Mothers_day_arrangement, Valentines_day_arrangement, Arrangement

# daisies, baby's breath, and poppies NOT REFRIGERATED
mothers_day_bouquet = Mothers_day_arrangement() # Instantiate the mothers day bouquet
# Create instances of the flowers allowed in the arrangement
poppy = Poppy()
daisy = Daisy()
babies_breath = Baby_breath()
test_rose = Rose() # Create an instance of a flower that should not be allowed in mothers day arrangement 

# Add the newly created flowers to the bouquet
mothers_day_bouquet.add_flower(daisy)
mothers_day_bouquet.add_flower(babies_breath)
mothers_day_bouquet.add_flower(poppy)

mothers_day_bouquet.add_flower(test_rose) # The flower is not added into the arrangement
# TODO: Adk why the AttributeError is not showing.

vday_bouquet = Valentines_day_arrangement() # add a poppy, should throw an err

rose = Rose()
alstro = Alstroemeria()
lilly = Lilly()

# Rose, Alstr, lilly refrigerated
vday_bouquet.add_flower(rose)
vday_bouquet.add_flower(alstro)
vday_bouquet.add_flower(lilly)
vday_bouquet.add_flower(poppy)