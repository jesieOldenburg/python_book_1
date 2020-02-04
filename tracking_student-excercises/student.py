# from exercise import Exercise
class Student:
    def __init__(self, first_name, last_name, slack_handle, cohort_num):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort_num = cohort_num
        self.current_exercises = list()

    def show_homework(self):
        full_name = f'{self.first_name} {self.last_name}'
        ex_names = '\n    - '.join([x_name.exercise_name for x_name in self.current_exercises])
        
        print(f'{full_name} is working on: \n    - {ex_names} \n')
        
    def __str__(self):
        return f'{self.first_name} {self.last_name} is in Cohort {self.cohort_num}'

# jesie = Student('Jesie', 'Oldenburg', 'joldenburg', 24)

# fizz = Exercise('Fizz', 'JS')
# coins = Exercise('Coins to Cash', 'Py')

# jesie.current_exercises.append(fizz)
# jesie.current_exercises.append(coins)

# jesie.show_homework()