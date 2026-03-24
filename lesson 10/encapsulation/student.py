class Student:
    def __init__(self, name, age):
        #Initialize private attribute
        self.__name = name
        self.__age=age

        def get_name(self):
            return self.__name

        def set_name(self, name):
            self.__name=name