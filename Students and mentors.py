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
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

best_lector = Lecturer('Red', 'Man')
best_lector.class_being_mentor += ['Python']

cool_student = Student('lifa', 'Ema', 'your_gender')
cool_student.courses_attache += ['Python']

cool_student.lect_grade(best_lector, 'Python', 9)
cool_student.lect_grade(best_lector, 'Python', 8)
cool_student.lect_grade(best_lector, 'Python', 7)
 
print(best_student.grades)
print(best_lector.grades_for_lecturer)