from flowers import Flower, Rose, Daisy
from arrangements import Mothers_day_arrangement, Valentines_day_arrangement, Arrangement

rose = Rose()
print(rose)
bouquet_one = Mothers_day_arrangement()
print('Bouquet attrs', bouquet_one.flower_list)
bouquet_one.add_flower(rose)
dim = Daisy()
bouquet_one.add_flower(dim)
bouquet_one.print_flowers()