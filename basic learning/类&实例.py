class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.print_score(), lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())




class Student(object):
    def init(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in set(['male', 'female']):
            self.__gender = gender
        else:
            raise TypeError('wrong sex')


lisa.set_gender(female)
print(lisa.get_gender())