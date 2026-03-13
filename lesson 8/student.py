class Student:
    school_name = "Digital School"

    def __init__(self, name, age, course):
        self.name=name
        self.age=age
        self.course=course


student1 = Student("Sara" , 18, "Python")
student2 = Student("Festa" , 20, "Javascript")

print(student1.course)
print(student2.course)