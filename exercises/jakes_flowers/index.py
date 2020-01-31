import os
# import sys
# sys.path.append('/Users/newuser/python_workspace/python_book_1/exercises/jakes_flowers')
from flowers import Flower, Rose, Daisy, Alstroemeria, Lilly, Baby_breath
from arrangements import Mothers_day_arrangement, Valentines_day_arrangement, Arrangement

bouquet_one = Mothers_day_arrangement()
daisy = Daisy()

bouquet_one.add_flower(daisy)

"""VALENTINES BOUQUET
"""
vday_bouquet = Valentines_day_arrangement()

rose = Rose()
alstro = Alstroemeria()
lilly = Lilly()

vday_bouquet.add_flower(rose)
vday_bouquet.add_flower(alstro)
vday_bouquet.add_flower(lilly)

print(rose.__dict__)


for flower in vday_bouquet.flower_list:
    print(flower.name)



# print("\nRose __dict__", rose.__dict__) Accessing an OBJECTS __dict__ method returns it props

# print(rose.available_colors)
# for color in rose.available_colors:
#     diff_color_rose = Rose(color)
#     print(diff_color_rose)