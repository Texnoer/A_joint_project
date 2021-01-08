students = []
courses = []
list_lecturer = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grades_hw(self, lecturer, course, grade):
        """Метод выставления оценок от студентов"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rating_grades:
                lecturer.rating_grades[course] += [grade]
            else:
                lecturer.rating_grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        information = '\nStudent ' + '\nИмя: ' + self.name + '\nФамилия: ' + self.surname
        information += '\nСредняя оценка за домашние задания: ' + average_grade(self.grades)
        information += '\nКурсы в процессе изучения: ' + (','.join(self.courses_in_progress))
        information += '\nЗавершенные курсы: ' + (', '.join(self.finished_courses))
        return information


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_in_progress = []
        self.rating_grades = {}

    def __str__(self):
        information = '\nЛектор' + '\nИмя: ' + self.name + '\nФамилия: ' + self.surname
        information += '\nСредняя оценка за лекцию: ' + average_grade(self.rating_grades)
        return information


class Reviewer(Mentor):
    # выставлять студентам оценки за домашние задания
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        information = '\nПроверяющий' + '\nИмя: ' + self.name + '\nФамилия: ' + self.surname
        return information





best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'C#', 'GIT']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 8)





print(best_student.grades)
print(cool_mentor.courses_attached)
