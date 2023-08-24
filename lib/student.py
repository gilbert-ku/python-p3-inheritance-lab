#!/usr/bin/env python

from user import User

# class Student(User):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.knowledge = []
#     def learn(self):
#         print(self.first_name)

# my_student = Student("My", "Student")
# print(my_student)


class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, information):
        self.knowledge.append(information)

# Creating a Student instance
my_student = Student("My", "Student")

# Calling the learn() method with an argument
my_student.learn("New information")

# Printing the student's knowledge
print(my_student.knowledge)

