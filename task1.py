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

def average_grade_students(students,course):
    middle_grade = 0
    count_students = 0
    for student in students:
        if course in student.courses_in_progress:
            middle_grade += Student.get_middle_grade(student)
            count_students +=1

        if count_students == 0:
            result = 'На этом курсе у студентов еще нет оценок'
        else:
            result = middle_grade/count_students
        
    return result

def average_grade_lektors(lektors,course):
    middle_grade = 0
    count_lektors = 0
    for lektor in lektors:
        if course in lektor.courses_attached:
            middle_grade += Lecturer.get_middle_rate(lektor)
            count_lektors +=1

        if count_lektors == 0:
            result = 'На этом курсе у лекторов еще нет оценок'
        else:
            result = middle_grade/count_lektors
        
    return result

ruoy_student = Student('Ruoy', 'Eman', 'male')
ruoy_student.courses_in_progress += ['Python']
ruoy_student.finished_courses += ['1С программирование']

tina_student = Student('Tina','Kandelaki','female')
tina_student.courses_in_progress += ['Python']
tina_student.finished_courses += ['Web программирование']

bruce_lektor = Lecturer('Bruce','Willis')
bruce_lektor.courses_attached += ['Python']
ruoy_student.rate_lktr(bruce_lektor,'Python',25)
ruoy_student.rate_lktr(bruce_lektor,'Python',30)
ruoy_student.rate_lktr(bruce_lektor,'Python',35)

arnold_lektor = Lecturer('Arnold','Schwarzenegger')
arnold_lektor.courses_attached += ['Python']
tina_student.rate_lktr(arnold_lektor,'Python',45)
tina_student.rate_lktr(arnold_lektor,'Python',60)
tina_student.rate_lktr(arnold_lektor,'Python',70)

same_mentor = Mentor('Some', 'Buddy')
same_mentor.courses_attached += ['Python']

kirill_mentor = Mentor('Kirill', 'Smirnov')
kirill_mentor.courses_attached += ['Python']

bill_reviewer = Reviewer('Bill', 'Gates') 
bill_reviewer.rate_hw(ruoy_student, 'Python', 10)
bill_reviewer.rate_hw(ruoy_student, 'Python', 20)
bill_reviewer.rate_hw(ruoy_student, 'Python', 30)

steven_reviewer = Reviewer('Steven','Jobs')
steven_reviewer.rate_hw(tina_student, 'Python', 90)
steven_reviewer.rate_hw(tina_student, 'Python', 90)
steven_reviewer.rate_hw(tina_student, 'Python', 60)

students = []
students += [ruoy_student]
students += [tina_student]

lektors = []
lektors += [bruce_lektor]
lektors += [arnold_lektor]

#средние оценки студентов и лекторов
print('Средняя оценка студентов на курсе Python: ', average_grade_students(students,'Python'))
print('Средняя оценка лекторов на курсе Python: ', average_grade_lektors(lektors,'Python'))
#принтуем проверку str методов
print()
print(tina_student)
print()
print(bruce_lektor)
print()
print(steven_reviewer)
print()
#принтуем проверку сравнения
print(tina_student==ruoy_student)
print(bruce_lektor==arnold_lektor)

