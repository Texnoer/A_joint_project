students = []
courses = []
all_lecturer = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        students.append(self)
        self.grades = {}
        courses.append(self.finished_courses)
        courses.append(self.courses_in_progress)

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
    def __lt__(self, other):
        if average_grade(self.grades) < average_grade(other.grades):
            return 'Лучший результат ' + other.name + ' ' + other.surname + ' с рейтингом ' +\
                   average_grade(other.grades)
        elif average_grade(self.grades) == average_grade(other.grades):
            return 'Такой же результат'
        else:
            return 'Лучший результат ' + self.name + ' ' + self.surname + ' с рейтингом ' +\
                   average_grade(self.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __repr__(self):  # это как и __str__ для вывода
        return self.name + ' ' + self.surname + ' Курс: ' + repr(self.courses_attached)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating_grades = {}
        all_lecturer.append(self)

    def __str__(self):
        information = '\nЛектор' + '\nИмя: ' + self.name + '\nФамилия: ' + self.surname
        information += '\nСредняя оценка за лекцию: ' + average_grade(self.rating_grades)
        return information

    def __lt__(self, other):
        if average_grade(self.rating_grades) < average_grade(other.rating_grades):
            return 'Лучший результат  ' + other.name + ' ' + other.surname + ' с рейтингом ' +\
                   average_grade(other.rating_grades)
        elif average_grade(self.rating_grades) == average_grade(other.rating_grades):
            return 'Такой же результат'
        else:
            return 'Лучший результат ' + self.name + ' ' + self.surname + ' с рейтингом ' + \
                   average_grade(self.rating_grades)

class Reviewer(Mentor):
    """выставлять студентам оценки за домашние задания"""
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

def average_grade(about_grades):
    """ Поиск среднего значения оценки """
    all_grades = []
    for subject, grades in about_grades.items():
        for grade in grades:
            all_grades.append(grade)
    if len(all_grades) == 0:
        av_grade = 0
        return str(av_grade)
    elif len(all_grades) > 0:
        av_grade = round((sum(all_grades) / len(all_grades)), 1)
        return str(av_grade)
    else:
        return "Ошибка"

def average_course(course, lists):
    """среднюю оценку всех студентов по выбранному курсу"""
    grade = []
    for value in lists:
        if course in (sum(courses, [])):
            if course in value.grades:
                for x, y in value.grades.items():
                    if course == x:
                        grade.extend(y)
                    elif course != x:
                        continue
        else:
            return f"Курса {course} нет"
    if len(grade) != 0:
        result = round((sum(grade) / len(grade)), 1)
        return f"Средняя оценка по курсу {course}: {str(result)}"
    elif len(grade) == 0:
        return f"По курсу {course} нет оценок"
    else:
        return 'Неверное значение'


def lecturer_average_grade(course, lists):
    lect_av_grade = []
    for value in lists:
        if course in (sum(courses, [])):
            if course in value.rating_grades:
                for x, y in value.rating_grades.items():
                    if course == x:
                        lect_av_grade.append(y)
                    elif course != x:
                        continue
        else:
            return f"Курса {course} нет"
    if len(lect_av_grade) != 0:
        result = round((sum(sum(lect_av_grade, [])) / len(sum(lect_av_grade, []))), 1)
        return f"Средняя оценка по курсу {course}: {str(result)}"
    elif len(lect_av_grade) == 0:
        return f"По курсу {course} нет оценок"
    else:
        return 'Неверное значение'

best_student = Student('Ruoy', 'Eman', 'm')
some_student = Student('Gena', 'Ivanov', 'm')
best_lecturer = Lecturer('Petr', 'Krugov')
some_lecturer = Lecturer('Dmitry', 'Zhuk')
cool_reviewer = Reviewer('Some', 'Buddy')
some_reviewer = Reviewer('Chack', 'Firsov')

best_student.courses_in_progress += ['Python', 'GIT', 'Java', 'HTML']
some_student.courses_in_progress += ['Python', 'GIT', 'C++', 'HTML']

some_lecturer.courses_attached += ['Python', 'GIT', 'C#', 'HTML']
best_lecturer.courses_attached += ['Python', 'GIT', 'CSS', 'C++', 'HTML']
some_reviewer.courses_attached += ['Python', 'GIT', 'CSS', 'C++']
cool_reviewer.courses_attached += ['Python', 'CSS', 'HTML']

some_student.grades_hw(some_lecturer, 'Python', 9)
some_student.grades_hw(best_lecturer, 'Python', 10)
best_student.grades_hw(some_lecturer, 'Python', 10)
best_student.grades_hw(some_lecturer, 'C++', 10)
best_student.grades_hw(some_lecturer, 'GIT', 9)
some_student.grades_hw(best_lecturer, 'HTML', 7)

some_student.finished_courses += ['HTML', 'notepad']
best_student.finished_courses += ['HTML', 'C++', 'SQL']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 8)
cool_reviewer.rate_hw(some_student, 'HTML', 5)
cool_reviewer.rate_hw(best_student, 'HTML', 6)
cool_reviewer.rate_hw(some_student, 'C++', 7)
some_reviewer.rate_hw(some_student, 'C++', 9)
some_reviewer.rate_hw(best_student, 'GIT', 7)


print(f"{some_lecturer.name} {some_lecturer.surname} рейтинг: ", average_grade(some_lecturer.rating_grades))
print(cool_reviewer)
print(repr(cool_reviewer))
print(some_lecturer)
print(some_lecturer.rating_grades)
print(best_student)
print(some_student)
print(average_course('HTML', students))
print(average_course('Python', students))
print(average_course('1C', students))
print(average_course('GIT', students))
print(average_course('C++', students))
print(lecturer_average_grade('HTML', all_lecturer))
print(lecturer_average_grade('Python', all_lecturer))
print(lecturer_average_grade('CSS', all_lecturer))
print(lecturer_average_grade('C++', all_lecturer))
print(repr(cool_reviewer))
print(cool_reviewer)
print(best_student.__lt__(some_student))
print(best_lecturer.__lt__(best_lecturer))
print(best_lecturer.__lt__(some_lecturer))
print(best_student > some_student)
print(best_lecturer < some_lecturer)
print(best_lecturer > some_lecturer)