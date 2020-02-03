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

# * Assign the instructors to the cohorts
day_cohort_36.add_instructor(jisie)
day_cohort_36.add_instructor(joe)
day_cohort_36.add_instructor(jenna)

# Create new instances of students
jesie = Student('Jesie', 'Oldenburg', 'jesieOldenburg', '36')
john = Student('John', 'Long', 'jlongbrah', '36')
ryan = Student('Ryan', 'Bishop', 'rybish', '36')
guy = Student('Guy', 'Cherkeskey', 'guyChe', '36')

# * Assign students to the cohorts
day_cohort_36.add_student(jesie)
day_cohort_36.add_student(john)
day_cohort_36.add_student(ryan)


# Create new instanaces of exercises
fizzbuzz = Exercise('FizzBuzz', 'JavaScript')
reverse_string = Exercise('Reverse String', 'JavaScript')
party_time = Exercise('Party Time', 'Python')
coins_to_cash = Exercise('Coins to Cash', 'Python')

# TODO: Have each instructor assign 2 exercises to each of the students.
# Assign exercises to students
jisie.assign_exercise(jesie, fizzbuzz)
jisie.assign_exercise(jesie, reverse_string)
jenna.assign_exercise(jesie, party_time)
jenna.assign_exercise(jesie, coins_to_cash)
joe.assign_exercise(jesie, fizzbuzz)
joe.assign_exercise(jesie, coins_to_cash)

jisie.assign_exercise(guy, party_time)
jisie.assign_exercise(guy, coins_to_cash)
jenna.assign_exercise(guy, party_time)
jenna.assign_exercise(guy, reverse_string)
joe.assign_exercise(guy, fizzbuzz)
joe.assign_exercise(guy, coins_to_cash)



# Print the students homework to the console
# jesie.show_homework()

students = list()

students.append(jesie)
students.append(john)
students.append(ryan)

exercises = list()

exercises.append(fizzbuzz)
exercises.append(reverse_string)
exercises.append(party_time)
exercises.append(coins_to_cash)

# ? What is the condition I need to check here?
# I am iterating through the 
for s in students:
    # ! s == to an instance of a student
    student_name  = s.first_name + ' ' + s.last_name
    print(s.current_exercises)
    # print('s =>', student_name)
    for x in exercises:
        print(x.exercise_name)
        # print(f'{student_name} is working on the {x.exercise_name} exercise')
        pass
