
class Human(object):
    def __init__(self, human_name):
        self.name = human_name

    def say_name(self):
        print("Hello,I'm %s" % self.name)


class Student(Human):

    def __init__(self, student_name, score):
        Human.__init__(self, human_name=student_name) # 调用父类构造方法
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


bart = Student('Bart Simpson', 59)
bart.say_name()
bart.print_score()
print("Bart's grade is %s" % bart.get_grade())

# print(bart._name) #'Student' object has no attribute '_name'


class Hello(object):
    def __init__(self,name):
        self._name = name

    def say_hello(self):
        print("Hello {0}".format(self._name))


class Hi(Hello):
    def sayHi(self):
        print("Hi {0}".format(self._name))


# h = Hello("WangChuncheng")
# h.say_hello()
# hi = Hi("Jack")
# hi.sayHi()
