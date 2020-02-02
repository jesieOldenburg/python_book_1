from student import Student
from exercise import Exercise
from cohort import Cohort
from instructor import Instructor

# Create new instances of Cohorts
day_cohort_36 = Cohort('Day Cohort 36')
day_cohort_45 = Cohort('Day Cohort 45')
day_cohort_92 = Cohort('Day Cohort 92')

# Create new instances of instructors
jisie = Instructor('Jisie', 'David', 'jdavid', '36', 'Awesomeness')
joe = Instructor('Joe', 'Shepard', 'JoeShep', '36', 'Cracking jokes')
jenna = Instructor('Jenna', 'Sollis', 'Jsollis', '36', 'Eating my gum')
brenda = Instructor('Brenda', 'Long', 'bjlong', '37', 'creativity')

# * Assign the instructors to the cohorts
day_cohort_36.add_instructor(jisie)
day_cohort_36.add_instructor(joe)
day_cohort_36.add_instructor(jenna)

# Create new instances of students
jesie = Student('Jesie', 'Oldenburg', 'jesieOldenburg', '36')
john = Student('John', 'Long', 'jlongbrah', '36')
ryan = Student('Ryan', 'Bishop', 'rybish', '36')

# * Assign students to the cohorts
day_cohort_36.add_student(jesie)
day_cohort_36.add_student(john)
day_cohort_36.add_student(ryan)


# Create new instanaces of exercises
fizzbuzz = Exercise('FizzBuzz', 'JavaScript')
reverse_string = Exercise('Reverse String', 'JavaScript')
party_time = Exercise('Party Time', 'Python')
coins_to_cash = Exercise('Coins to Cash', 'Python')

# Assign exercises to students
jisie.assign_exercise(jesie, fizzbuzz)
jisie.assign_exercise(jesie, reverse_string)
jisie.assign_exercise(jesie, party_time)
jisie.assign_exercise(jesie, coins_to_cash)

# Print the students homework to the console
jesie.show_homework()