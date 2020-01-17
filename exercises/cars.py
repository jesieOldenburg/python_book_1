"""
    # Using set() to create a set
    languages = set()

    # Using curly braces allows you to initialize the set with values
    languages = { 'english', 'mandarin chinese', 'spanish', 'english', 'spanish', 'portugese' }

    print(languages)

    showroom = set()

    showroom.add('F-150 Lightning')
    showroom.add('Nissan Skyline')
    showroom.add('Datsun 510')
    showroom.add('Ford GT-40')
    print(len(showroom))
    print(showroom)
    showroom.add('Nissan Skyline')
    print(showroom)

    new_cars = {'Acura NSX', 'Ferarri GT-40'}
    showroom.update(new_cars)
    print(showroom)

    showroom.remove('F-150 Lightning')
    print(showroom)

    junkyard = set()
    junkyard.add('Mustang')
    junkyard.add('Camaro')
    junkyard.add('El Camino')
    junkyard.add('Datsun 510')
    junkyard.add('Nissan Skyline')

    comparison_set = junkyard.intersection(showroom)
    print(comparison_set)

    purchased_inventory = junkyard.union(showroom)
    print(purchased_inventory)

    purchased_inventory.remove('Mustang')
    print(purchased_inventory)
"""

makes = (
  (1, "Toyota"), (2, "Nissan"),
  (3, "Ford"), (4, "Mini"),
  (5, "Honda"), (6, "Dodge"),
)

models = (
  (1, "Altima", 2), (2, "Thunderbird", 3),
  (3, "Dart", 6), (4, "Accord", 5),
  (5, "Prius", 1), (6, "Countryman", 4),
  (7, "Camry", 1), (8, "F150", 3),
  (9, "Civic", 5), (10, "Ram", 6),
  (11, "Cooper", 4), (12, "Pilot", 5),
  (13, "Xterra", 2), (14, "Sentra", 2),
  (15, "Charger", 6)
)

colors = (
  (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
  (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

available_car_colors = (
  (1, 1), (1, 2), (1, 7),
  (2, 1), (2, 3), (2, 7),
  (3, 2), (3, 3), (3, 7),
  (4, 3), (4, 5), (4, 8),
  (5, 2), (5, 4), (5, 8),
  (6, 2), (6, 6), (6, 7),
  (7, 1), (7, 3), (7, 7),
  (8, 1), (8, 5), (8, 8),
  (9, 1), (9, 6), (9, 7),
  (10, 2), (10, 5), (10, 7),
  (11, 3), (11, 6), (11, 8),
  (12, 1), (12, 4), (12, 7),
  (13, 2), (13, 6), (13, 8),
  (14, 2), (14, 5), (14, 8),
  (15, 1), (15, 4), (15, 7)
)


"""
    Part 1: Reporting Object
You must first build a new dictionary that follows the format below.

Each key in the dictionary should be the name of a make, and its value will be a dictionary.
The keys in the make dictionary will be the models, and the value will be a list of colors in which that the model is available.
"""

car_inventory = dict()

def assign_colors(model_color_id, key_one, key_two):
    for color in colors:
        color_name = color[1]
        color_id = color[0]
        colors_match = model_color_id == color_id
        # print(colors_match)
        if colors_match:
            car_inventory[key_one][key_two] = color_name
        pass
            


def build_car_inventory(makes, model):
        
    """

    """

    for num, make in makes: # Makes Loop
        make_id = num
        make_primary_key = make
        print()
        car_inventory[make_primary_key] = {}
        for num_one, model, num_two in models: # Models Loop
            model_id = num_two
            model_primary_key = model
            model_color_id = num_one
            # print(makes)
            if model_id == make_id:
                car_inventory[make_primary_key][model_primary_key] = list()
            # assign_colors(model_color_id, make_primary_key, model_primary_key)
    return car_inventory
    pass
build_car_inventory(makes, models)
# print(car_inventory)
print(car_inventory)