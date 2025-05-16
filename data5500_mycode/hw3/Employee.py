#2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    #function that increases salary
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

employee = Employee(name="John", salary=5000)
employee.increase_salary(10) #increase by 10%

print("The updated salary for", employee.name + "is:", employee.salary)


#Create a class called Employee with attributes name and salary. Implement a method within the class that increases the salary of the employee by a given percentage. Instantiate an object of the Employee class with name = "John" and salary = 5000, increase the salary by 10%, and print the updated salary.

