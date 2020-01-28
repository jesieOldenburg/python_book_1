import datetime

class Employee:
    def __init__(self, employee_name, job_title):
      self.employee_name = employee_name
      self.job_title = job_title
      self.start_date = datetime.datetime.now().date()
      
class Company:
    def __init__(self, company_name, company_address, industry):
        self.company_name = company_name
        self.company_address = company_address
        self.industry = industry
        self.employees = list()

google = Company('Google', '123 Googy Rd, Googsville GO, 12345', 'Technology')
lamborghini = Company('Lamborghini', '456 Fast Way, Somewhere IT, 56789', 'Automobile')

craig = Employee('Craig Meng', 'HVAC Technician')
scotty = Employee('Scotty Fudrucker', 'Automotive Audio Installer')
doug = Employee('Dougy Young', 'Tire Tech')
randy = Employee('Randy Gee', 'Software Engineer')
hector = Employee('Hector Barnes', 'Penetration Tester')

google.employees.append(craig)
google.employees.append(randy)
google.employees.append(hector)

lamborghini.employees.append(scotty)
lamborghini.employees.append(doug)

def print_companies_employees():
    pass
    co_name = google.company_name
    industry = google.industry
    
    for employee in google.employees:
        pass
        emp_name = employee.employee_name
        if emp_name in google.employees:
            print(f'{co_name} is in the {industry} industry and has the following employees:\n *{emp_name}')


print_companies_employees()