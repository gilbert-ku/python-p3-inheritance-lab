#!/usr/bin/env python

from user import User

# import random

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

# class Teacher(User):
#     def __init__(self, first_name, last_name, knowledge=None):
#         super().__init__(first_name, last_name)
#         self.knowledge = knowledge if knowledge is not None else []

#     def teach(self):
#         if self.knowledge:
#             return random.choice(self.knowledge)
#         else:
#             return "No knowledge available"
# knowledge = [
#     "str is a data type in Python",
#     "programming is hard, but it's worth it",
#     "JavaScript async web request",
#     "Python function call definition",
#     "object-oriented teacher instance",
#     "programming computers hacking learning terminal",
#     "pipenv install pipenv shell",
#     "pytest -x flag to fail fast",
# ]

# my_teacher = Teacher("My", "Teacher", knowledge=knowledge)
# print(my_teacher.first_name)   # Should print "My"
# print(my_teacher.last_name)    # Should print "Teacher"
# print(my_teacher.knowledge)    # Should print the list of knowledge


# import random

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

# class Teacher(User):
#     def __init__(self, first_name, last_name, knowledge=None):
#         super().__init__(first_name, last_name)
#         self.knowledge = knowledge if knowledge is not None else []

#     def teach(self):
#         if self.knowledge:
#             return random.choice(self.knowledge)  # Return a random element from knowledge
#         else:
#             return "No knowledge available"

# knowledge = [
#     "str is a data type in Python",
#     "programming is hard, but it's worth it",
#     "JavaScript async web request",
#     "Python function call definition",
#     "object-oriented teacher instance",
#     "programming computers hacking learning terminal",
#     "pipenv install pipenv shell",
#     "pytest -x flag to fail fast",
# ]

# my_teacher = Teacher("My", "Teacher", knowledge=knowledge)
# print(my_teacher.first_name)   # Should print "My"
# print(my_teacher.last_name)    # Should print "Teacher"
# print(my_teacher.knowledge)    # Should print the list of knowledge

# random_knowledge = my_teacher.teach()  # Get a random piece of knowledge
# print(random_knowledge)

import random

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge if knowledge is not None else []

    def teach(self):
        if self.knowledge:
            return random.choice(self.knowledge)  # Return a random element from knowledge
        else:
            return "No knowledge available"

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

my_teacher = Teacher("My", "Teacher", knowledge=knowledge)
print(my_teacher.first_name)   # Should print "My"
print(my_teacher.last_name)    # Should print "Teacher"
print(my_teacher.knowledge)    # Should print the list of knowledge

random_knowledge = my_teacher.teach()  # Get a random piece of knowledge
print(random_knowledge)

