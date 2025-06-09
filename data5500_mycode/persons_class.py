import numpy as np
person_dct = {}
person_dct["name"] = "lucy"
person_dct["age"] = 23
person_dct["height"] = 64
person_dct["grades"] = [85, 89, 93]


print(person_dct)


class Person():
    def __init__(self, name, age, height, grades):
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades

    def calc_avg_grades(self):
        return np.mean(self.grades)

p1 = Person("lucy", 23, 64, [89, 88, 95])
print(p1)
print(p1.name)
print(p1.age)
print(p1.height)
print(p1.grades)
print(p1.calc_avg_grades())