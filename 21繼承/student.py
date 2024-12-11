from person import Person

class Student(Person):#Student去繼承Person
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school
    '''
    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)繼承後可刪除
    '''
    def print_school(self):
        print(self.school)