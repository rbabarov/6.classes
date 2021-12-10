class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        

    def rate_lktr(self, lektr, course, rates_lktr):
        
        if isinstance(lektr, Lecturer) and course in self.courses_in_progress:           
            if course in lektr.rates_lktr:               
                lektr.rates_lktr[course] += [rates_lktr]
            else:               
                lektr.rates_lktr[course] = [rates_lktr]
        else:
            return 'Ошибка'

    def get_middle_grade(self):
        sum_grades = 0
        len_grades = 0
        for grades in self.grades.values():
            for grade in grades:
                sum_grades += grade
                len_grades += 1
        if len_grades == 0:
            result_grades = 'Нет оценок'
        else:
            result_grades = sum_grades/len_grades
        return result_grades

    def __str__(self):
        
        result_grades = self.get_middle_grade()

        namestr = f'Имя: {self.name}\n' 
        surnamestr = f'Фамилия: {self.surname}\n' 
        gradesstr = f'Средняя оценка за домашние задания: {result_grades}\n'
        courses_in_progress_str = f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
        finished_courses_str = f'Завершенные курсы: {",".join(self.finished_courses)}'
        return namestr+surnamestr+gradesstr+courses_in_progress_str+finished_courses_str

    def __eq__(self, other):
        result_grades = self.get_middle_grade()
        other_grades = other.get_middle_grade()
        return result_grades == other_grades 
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []        
  

class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname) 
        self.rates_lktr = {}

    def get_middle_rate(self):
        summ_rate = 0
        len_rate = 0
        for rates in self.rates_lktr.values():
            for rate in rates:
                len_rate += 1
                summ_rate += rate

        if len(self.rates_lktr) == 0:
            middlerate = 'У лектора еще нет оценок' 
        else:                
            middlerate = summ_rate/len_rate  
        return middlerate

    def __str__(self):
       
        middlerate = self.get_middle_rate()

        namestr = f'Имя: {self.name}\n' 
        surnamestr = f'Фамилия: {self.surname}\n'
        average = f'Средняя оценка за лекции:{middlerate}' 
        return namestr+surnamestr+average

    def __eq__(self, other):
        result_middlerate = self.get_middle_rate()
        other_middlerate = other.get_middle_rate()
        return result_middlerate == other_middlerate 
 
class Reviewer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student)  and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        namestr = f'Имя: {self.name}\n' 
        surnamestr = f'Фамилия: {self.surname}' 
        return namestr+surnamestr

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['1с']
lektor = Lecturer('Bruce','Wilis')
lektor.courses_attached += ['Python']
best_student.rate_lktr(lektor,'Python',25)
best_student.rate_lktr(lektor,'Python',30)
best_student.rate_lktr(lektor,'Python',35)

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_reviewer = Reviewer('Bill', 'Gates') 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 20)
cool_reviewer.rate_hw(best_student, 'Python', 30)
print(best_student) 
#print(best_student.grades)

