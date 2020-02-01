import os
# import sys
# sys.path.append('/Users/newuser/python_workspace/python_book_1/exercises/jakes_flowers')
from flowers import Flower, Rose, Daisy, Alstroemeria, Lilly, Baby_breath, Poppy
from arrangements import Mothers_day_arrangement, Valentines_day_arrangement, Arrangement

# daisies, baby's breath, and poppies NOT REFRIGERATED
bouquet_one = Mothers_day_arrangement() # add a rose, should throw an err
poppy = Poppy()
daisy = Daisy()
babyies_breath = Baby_breath()

bouquet_one.add_flower(daisy)
bouquet_one.add_flower(babyies_breath)
bouquet_one.add_flower(poppy)

"""VALENTINES BOUQUET
"""
vday_bouquet = Valentines_day_arrangement() # add a poppy, should throw an err

rose = Rose()
alstro = Alstroemeria()
lilly = Lilly()
# Rose, Alstr, lilly refrigerated
vday_bouquet.add_flower(rose)
vday_bouquet.add_flower(alstro)
vday_bouquet.add_flower(lilly)
vday_bouquet.add_flower(poppy)
vday_bouquet.display_flowers()


# for flower in vday_bouquet.flower_list:
#     print(flower.name)
#     pass


# print("\nRose __dict__", rose.__dict__) Accessing an OBJECTS __dict__ method returns it props

# print(rose.available_colors)
# for color in rose.available_colors:
#     diff_color_rose = Rose(color)
#     print(diff_color_rose)