# import sys
# sys.path.append('/Users/newuser/python_workspace/python_book_1/exercises/jakes_flowers')
from flowers import Flower, Rose, Daisy
from arrangements import Mothers_day_arrangement, Valentines_day_arrangement, Arrangement

rose = Rose()
bouquet_one = Mothers_day_arrangement()
bouquet_one.add_flower(rose)
bouquet_one.print_flowers()