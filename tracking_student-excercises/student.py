class Student:
    def __init__(self, first_name, last_name, slack_handle, cohort_num):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort_num = cohort_num
        self.current_exercises = list()

    def show_homework(self):
        for x in self.current_exercises:
            print(x.exercise_name)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} is in Cohort {self.cohort_num}'