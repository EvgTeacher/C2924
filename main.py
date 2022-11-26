class Student:
    education = "Step"
    group = "C2924"
    subject = "OOP Python"
    def __init__(self):
        print(id(self))


st1 = Student()
print(id(st1))


# print(st1.group)
# print(st1.education)
# st2 = Student()
# print(st2.group)
# st2.group = "C2925"
# print(st2.group)
# print(st1.group)