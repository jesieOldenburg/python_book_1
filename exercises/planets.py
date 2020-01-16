import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 11)
# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False
    # Iterate your random number list here
    for random_number in my_randoms:
        if random_number == number:
            print(f'{number} is in the random list')
            

planet_list = ["Mercury", "Mars"]
last_planets = ['Uranus', 'Neptune']

planet_list.append('Jupiter')
planet_list.append('Saturn')

planet_list.extend(last_planets)

planet_list.insert(1, 'Venus')
planet_list.insert(2, 'Earth')

planet_list.append('Pluto')

del planet_list[8]

# # Iterate over the list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.

spacecraft = [
    ("Cassini", "Saturn"), 
    ("Viking", "Mars"),
    ("Satboy",'Venus'),
    ('Ranger', 'Jupiter'),
    ('Hubble', 'Earth'),
    ('Angel', 'Neptune'),
    ('Sentinel', 'Uranus')
]

for planet in planet_list:
    for sat_planet_pair in spacecraft:
        x = planet in sat_planet_pair
        if x:
            print(sat_planet_pair[0])