class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attache = []       

    def lect_grade(self, lecturer, course, course_grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attache and course in lecturer.class_being_mentor:
            if course in lecturer.grades_for_lecturer:
                lecturer.grades_for_lecturer[course] +=[course_grade]
            else:
                lecturer.grades_for_lecturer[course] = [course_grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grades_for_some_students}\nКурсы в процессе изучения: {some_s}\nЗавершенные курсы: Введение в программирование'        
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_for_lecturer = {}
        self.class_being_mentor = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grades_for_some_lecturer}'
        
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'        
        return res

some_reviewer =  Reviewer('Some1', 'Buddy1')

some_lecturer = Lecturer('Some2', 'Buddy2')
some_lecturer.class_being_mentor += ['Python']

some_student = Student('Ruoy1', 'Eman1', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']

best_student = Student('best', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Git']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

for course, grade in best_student.grades.items():
    summa = sum(grade)
    quantity = len(grade)
    average = summa / quantity
    average_grades_for_best_students = round(average, 1)

cool_mentor.rate_hw(some_student, 'Python', 9)
cool_mentor.rate_hw(some_student, 'Git', 9)
cool_mentor.rate_hw(some_student, 'Python', 9)
cool_mentor.rate_hw(some_student, 'Git', 9)

for course_learn, grade in some_student.grades.items():
    summa = sum(grade)
    quantity = len(grade)
    average = summa / quantity
    average_grades_for_some_students = round(average, 1)

some_s = ', '.join(f'{k}' for k in some_student.grades.keys())
    
best_lector = Lecturer('Best', 'Buddy')
best_lector.class_being_mentor += ['Python']

cool_student = Student('Ruoy', 'Eman', 'your_gender')
cool_student.courses_attache += ['Python']

cool_student.lect_grade(best_lector, 'Python', 10)
cool_student.lect_grade(best_lector, 'Python', 10)
cool_student.lect_grade(best_lector, 'Python', 10)

for key, value in best_lector.grades_for_lecturer.items():
    summa = sum(value)
    quantity = len(value)
    average = summa / quantity
    average_grades_for_best_lecturer = round(average, 1)

cool_student.lect_grade(some_lecturer, 'Python', 9)
cool_student.lect_grade(some_lecturer, 'Python', 10)
cool_student.lect_grade(some_lecturer, 'Python', 10)

for key, value in some_lecturer.grades_for_lecturer.items():
    summa = sum(value)
    quantity = len(value)
    average = summa / quantity
    average_grades_for_some_lecturer = round(average, 1)

if average_grades_for_some_students > average_grades_for_best_students:
    print(best_student.name, 'освобождает место лучшего студента для', some_student.name)
else:
    print(best_student.name, 'по прежнему лучший студент.')
print('')
if average_grades_for_some_lecturer > average_grades_for_best_lecturer:
    print('Сегодня', some_lecturer.name, 'был лучше, чем лектор', best_lector.name)
else:
    print(best_lector.name, 'остаёться лучшим летором.')
print('')
print(some_reviewer)
print('')
print(some_lecturer)
print('')
print(some_student)
print('')
print(best_student.grades)
print('')
print(best_lector.grades_for_lecturer)