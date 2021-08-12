class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attache = []
        self.student_list = []       

    def lect_grade(self, lecturer, course, course_grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attache and course in lecturer.class_being_mentor:
            if course in lecturer.grades_for_lecturer:
                lecturer.grades_for_lecturer[course] +=[course_grade]
            else:
                lecturer.grades_for_lecturer[course] = [course_grade]
        else:
            return 'Ошибка'
    
    def average(self):
        if not self.grades:
            print('Нет оценки!')
        else:
            grade = []
            for i in self.grades.values():
                grade += i
            return round((sum(grade) / len(grade)), 1)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'        
        return res

    def __lt__(self, some_students):
        if not isinstance(some_students, Student):
            print('Студента не существует!')
            return
        else:
            better_student = self.average() < some_students.average()
            if better_student:
                print(f'{self.name} учится хуже, чем {some_students.name}')
            else:
                print(f'{self.name} учится лучше, чем {some_students.name}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_for_lecturer = {}
        self.class_being_mentor = []

    def average(self):
        if not self.grades_for_lecturer:
            print('Нет оценки!')
        else:
            grade = []
            for i in self.grades_for_lecturer.values():
                grade += i
            return round((sum(grade) / len(grade)), 1)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}'
        return res

    def __lt__(self, some_lectors):
        if not isinstance(some_lectors, Lecturer):
            print('Лектора не существует!')
            return
        else:
            better_lecturer = self.average() < some_lectors.average()
            if better_lecturer:
                print(f'{self.name} читает лекции хуже, чем {some_lectors.name}')
            else:
                print(f'{self.name} читает лекции лучше, чем {some_lectors.name}')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
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
some_lecturer.class_being_mentor += ['Git']

some_student = Student('Ruoy1', 'Eman1', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

best_student = Student('best', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)

cool_mentor.rate_hw(some_student, 'Python', 9)
cool_mentor.rate_hw(some_student, 'Git', 9)
cool_mentor.rate_hw(some_student, 'Python', 9)
cool_mentor.rate_hw(some_student, 'Git', 9)
    
best_lector = Lecturer('Best', 'Buddy')
best_lector.class_being_mentor += ['Python']
best_lector.class_being_mentor += ['Git']

cool_student = Student('Ruoy', 'Eman', 'your_gender')
cool_student.courses_attache += ['Python']
cool_student.courses_attache += ['Git']

cool_student.lect_grade(best_lector, 'Python', 10)
cool_student.lect_grade(best_lector, 'Python', 10)
cool_student.lect_grade(best_lector, 'Python', 10)

cool_student.lect_grade(some_lecturer, 'Python', 9)
cool_student.lect_grade(some_lecturer, 'Python', 10)
cool_student.lect_grade(some_lecturer, 'Python', 10)

# if average_grades_for_some_students > average_grades_for_best_students:
#     print(best_student.name, 'освобождает место лучшего студента для', some_student.name)
# else:
#     print(best_student.name, 'по прежнему лучший студент.')
# print('')
# if average_grades_for_some_lecturer > average_grades_for_best_lecturer:
#     print('Сегодня', some_lecturer.name, 'был лучше, чем лектор', best_lector.name)
# else:
#     print(best_lector.name, 'остаёться лучшим летором.')
print(some_reviewer)
print('')
print(some_lecturer)
print('')
print(some_student)
print('')
some_student < best_student
print('')
some_lecturer > best_lector
print('')

# print('')
# print(best_lector.grades_for_lecturer)