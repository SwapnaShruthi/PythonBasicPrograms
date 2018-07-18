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

class Dumb(Student):
   perc_rise = 1.10

   def __init__(self,first,last,marks,lang):
       super().__init__(first,last,marks)
       self.lang = lang

stdDumb = Dumb('Dumb','Dumb',40,'Python')
print(stdDumb.first)
print(stdDumb.lang)
print(stdDumb.apply_rise())