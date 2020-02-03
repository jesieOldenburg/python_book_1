class Cohort:
    def __init__(self, cohort_name):
        self.cohort_name = cohort_name
        self.students_in_cohort = list()
        self.instructors_in_cohort = list()
        
    def add_instructor(self, instructor):
        self.instructors_in_cohort.append(instructor)
        # print(f'{instructor.first_name} {instructor.last_name} was added to {self.cohort_name}')
    
    def add_student(self, student):
        self.students_in_cohort.append(student)
        # print(f'\n{student.first_name} {student.last_name} was added to {self.cohort_name} as a student')
        
    def __str__(self):
        return f'{self.cohort_name}'