class Exercise:
    def __init__(self, exercise_name, exercise_language):
        self.exercise_name = exercise_name
        self.exercise_language = exercise_language
        
    def __str__(self):
        return f'{self.exercise_name} is done in the {self.exercise_language} language'