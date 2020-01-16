my_family = {
    'sister': {
        'name': 'Nikki',
        'age': 19,
        'gender': 'f'
    },
    'mother': {
        'name': 'Kathy',
        'age': 56,
        'gender': 'f'
    },
    'father': {
        'name': 'Donald',
        'age': 66,
        'gender': 'm'
    },
    'myself': {
        'name': 'Jesie',
        'age': 31,
        'gender': 'm'
    },
    'son': {
        'name': 'Owen',
        'age': 6,
        'gender': 'm'
    }
}

# for the key in the my_family dict do [...]
for fam_member in my_family:
    male_or_female = ''
    gender = my_family[fam_member]['gender']

    if gender == 'f':
        male_or_female = 'she'
    else:
        male_or_female = 'he'
        
    """
    declare two variables by accessing the nested values of my_family (parents, siblings etc...)which are assigned to fam_member in the for loop, then access the nested keys of name and age
    """
    
    relationship = fam_member.title()
    name = my_family[fam_member]['name']
    age = my_family[fam_member]['age']
    
    print(f'{name} is my {relationship} and {male_or_female} is {age} years old.')