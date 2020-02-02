class Instructor:
    def __init__(self, first_name, last_name, slack_handle, instructor_cohort, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.instructor_cohort = instructor_cohort
        self.specialty = specialty
        
    def assign_exercise(self, student, exercise):
        # TODO: Duck type to prevent duplicate exercises being added to students exercise list
        student.current_exercises.append(exercise)
        print(exercise.exercise_name)
        

            
        
    def __str__(self):
        return f'Instructor {self.first_name} {self.last_name} is in {self.instructor_cohort}. Their specialty is {self.specialty}'
        