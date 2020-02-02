class Cohort:
    def __init__(self, cohort_name):
        self.cohort_name = cohort_name
        self.students_in_cohort = list()
        self.instructors_in_cohort = list()
        
    def __str__(self):
        return f'{self.cohort_name}'