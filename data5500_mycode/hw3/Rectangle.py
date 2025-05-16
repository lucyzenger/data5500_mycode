#1
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
my_rectangle = Rectangle(length=5, width=3)

print("The area of the rectangle is:", my_rectangle.area())


#Create a class called Rectangle with attributes length and width. Implement a method within the class to calculate the area of the rectangle. Instantiate an object of the Rectangle class with length = 5 and width = 3, and print its area.


#Where is the error in my code?  class Rectangle:
#     def__init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width
    
# my_rectangle = Rectangle(length=5, width=3)

# print("The area of the rectangle is:", my_rectangle.area())                                                (myenv) root@ip-172-31-1-39:/home/ubuntu# /home/ubuntu/myenv/bin/python /home/ubuntu/hw3/pet.py
#   File "/home/ubuntu/hw3/pet.py", line 3
#     def__init__(self, length, width):

