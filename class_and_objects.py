class Student:
    perc_rise = 1.05 
    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first+'.'+last+'@school.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_rise(self):
        return int(self.marks*self.perc_rise)

std_1 = Student('Swapna','Shruthi',90)
print(std_1.fullname())
print(std_1.apply_rise())
print(std_1.perc_rise)
print(std_1.marks)
