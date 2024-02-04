#Employee Managemnet System
class Employee:
    def __init__(self,name,employee_id,wages):
        self.name=name
        self.employee_id=employee_id
        self.wages=wages
    def calc_salary(self,working_hours):
        print('$' + str(self.wages*working_hours))
    def display(self):
        print(f'Name:{self.name}\nID:{self.employee_id}')
E1=Employee("Rohan",23678,40)
E1.display()
E1.calc_salary(100)

    
