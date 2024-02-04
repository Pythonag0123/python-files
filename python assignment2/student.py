#Student Management system
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        return f'Name:{self.name}\nRoll Number:{self.roll}'
stud1=Student("Ravi",40)
print(stud1.display())
    
        
