import numpy as np

class Person():
    def __init__(self, name, age, height, grades, ssn):
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades
        self.__ssn = ssn 

    def get_ssn(self):
        return self.__ssn
    
    def set_ssn(self, ssn):
        self.__ssn = ssn
    

    def calc_avg_grades(self):
        return np.mean(self.grades)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height

    def get_grades(self):
        return self.grades

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.name = age

    def set_height(self, height):
        self.name = height

    def set_grades(self, grades):
        self.name = grades
    

p1 = Person("lucy", 23, 64, [89, 88, 95], 12341234)
print(p1)
print(p1.get_name)
# print(p1.get_age)
# print(p1.get_height)
# print(p1.get_grades)
# print(p1.calc_avg_grades())

# p1.set_grades([100,100,100])
# print(p1.calc_avg_grades())

p1.set_ssn(12341234)
print(p1.get_ssn())

print(p1.name)
print(p1.__ssn)