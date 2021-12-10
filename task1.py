class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.rates_lktr = {}

    def rate_lktr(self, lektr, course, rates_lktr):
        if isinstance(lektr, Lecturer) and course in self.courses_attached and course in lektr.courses_in_progress:
            if course in lektr.grades:
                self.rates_lktr[course] += [rates_lktr]
            else:
                self.rates_lktr[course] = [rates_lktr]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []        
  

class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname) 
 
class Reviewer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_reviewer = Reviewer('Bill', 'Gates') 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)

