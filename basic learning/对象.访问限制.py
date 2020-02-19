class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = self.set_gender(gender)

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ('male', 'female'):
            self.__gender = gender
        else:
            raise ValueError('illegal parameter')

bart = Student('Bart', 'male')
bart.set_gender('female')
print(bart.get_gender())