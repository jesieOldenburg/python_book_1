from student import Student
from exercise import Exercise
from cohort import Cohort
from instructor import Instructor

# Create new instanaces of exercises
fizzbuzz = Exercise('FizzBuzz', 'JavaScript')
reverse_string = Exercise('Reverse String', 'JavaScript')
party_time = Exercise('Party Time', 'Python')
coins_to_cash = Exercise('Coins to Cash', 'Python')

# Create new instances of Cohorts
day_cohort_36 = Cohort('Day Cohort 36')
day_cohort_45 = Cohort('Day Cohort 45')
day_cohort_92 = Cohort('Day Cohort 92')

# Create new instances of instructors
jisie = Instructor('Jisie', 'David', 'jdavid', '36', 'Awesomeness')
joe = Instructor('Joe', 'Shepard', 'JoeShep', '36', 'Cracking Jokes')
joe = Instructor('Brenda', 'Long', 'bjlong', '37', 'Creativity')

# Create new instances of students
jesie = Student('Jesie', 'Oldenburg', 'jesieOldenburg', '36')

# Assign exercises to students
jisie.assign_exercise(jesie, fizzbuzz)

# Print the students homework to the console
jesie.show_homework()