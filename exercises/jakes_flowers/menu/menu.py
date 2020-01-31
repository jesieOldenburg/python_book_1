import os

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('_-::-_ JAKES FLOWERS _-::-_\n')
    print('Which bouquet would you like?\n\n 1. Mothers Day Bouquet\n 2. Valentines Day Bouquet')
    user_choice = input('> ')
    # print(f'User input is {user_choice} and its type is ::', type(user_choice))
    menu_actions(user_choice)
    
def menu_actions(user_choice):
    if user_choice == '1':
        print('You chose 1')
        add_flowers_menu()
    if user_choice == '2':
        print('You chose 2')
    
def add_flowers_menu():
    print('Ok great! Now choose some flowers to add. Here are your options:')

# i = 0
# while i < user_input:
#   print(i)
#   i += 1