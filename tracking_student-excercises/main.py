from student import Student
from exercise import Exercise
from cohort import Cohort
from instructor import Instructor

fizzbuzz = Exercise('FizzBuzz', 'JavaScript')
reverse_string = Exercise('Reverse String', 'JavaScript')
party_time = Exercise('Party Time', 'Python')
coins_to_cash = Exercise('Coins to Cash', 'Python')

day_cohort_36 = Cohort('Day Cohort 36')
day_cohort_45 = Cohort('Day Cohort 45')
day_cohort_92 = Cohort('Day Cohort 92')

jisie = Instructor('Jisie', 'David', 'jdavid', '36', 'Awesomeness')
jesie = Student('Jesie', 'Oldenburg', 'jesieOldenburg', '36')
jisie.assign_exercise(jesie, fizzbuzz)
jesie.show_homework()