zoo = ('Lion', 'Giraffe', 'Chimpanzee', 'Rhino', 'Koala', 'Zebra', 'Tiger', 'Gorilla', 'Panda', 'Kodiak Bear')
zoo.index('Zebra')

animal_to_find = 'Gorilla'


if animal_to_find in zoo:
    print(animal_to_find)
          

my_fam = ('Owen', 'Me', 'Dad', 'Mom')

(son, myself, father, mother) = my_fam

# print(son)
# print(myself)
# print(father)
# print(mother)

animal_party = (an_one, an_two, an_three, an_four, an_five, an_six, an_seven, an_eight, an_nine, an_ten) = zoo

# print(animal_party)

animal_list = list(animal_party)
print(animal_list)
three_more_animals = ['Flamingo', 'Polar Bear', 'Lemur']
animal_list.extend(three_more_animals)
print(animal_list)

animal_list = tuple(animal_list)
print(animal_list)