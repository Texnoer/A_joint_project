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

    def __repr__(self):  # это как и __str__ для вывода
        return self.name + ' ' + self.surname + ' Курс: ' + repr(self.courses_attached)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating_grades = {}

    def __str__(self):
        information = '\nЛектор' + '\nИмя: ' + self.name + '\nФамилия: ' + self.surname
        information += '\nСредняя оценка за лекцию: ' + average_grade(self.rating_grades)
        return information

    def __lt__(self, other):
        if average_grade(self.rating_grades) < average_grade(other.rating_grades):
            return 'Лучший результат  ' + other.name + ' ' + other.surname + ' с рейтингом ' +\
                   average_grade(other.rating_grades)
        elif average_grade(self.rating_grades) == average_grade(other.rating_grades):
            return 'the same result'
        else:
            return 'The best result is ' + self.name + ' ' + self.surname + ' with a rating ' + \
                   average_grade(self.rating_grades)

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

def average_grade(about_grades):
    """ Поиск среднего значения оценки """
    all_grades = []  # добавляем пустое хранилище для записи всех всех всех оценок одного студента
    for subject, grades in about_grades.items():  # это разбиение словаря на ключ - значение.
        for grade in grades:  # для ключа из словаря (в нашем случае ключ это название курса)
            all_grades.append(grade)  # добавляем в хранилище все оценки
    if len(all_grades) == 0:  # ищем длину хранилища. Если 0, то вернем ноль без дальнейших действий
        av_grade = 0
        return str(av_grade)
    elif len(all_grades) > 0:  # если больше, то разделим сумму оценок (sum(all_grades) на длину len(all_grades))
        # из математики  1+2+3+7 / 4 = 3,25
        av_grade = round((sum(all_grades) / len(all_grades)), 1)  # round округляет результат до (сколько скажешь после
        # запятой. В нашем случае до 1 знака после запятой. Иначе можем получить 7.3333333333333...
        return str(av_grade)
    else:
        return "Ошибка"


best_student = Student('Ruoy', 'Eman', 'm')
some_student = Student('Gena', 'Ivanov', 'm')
best_lecturer = Lecturer('Petr', 'Krugov')
some_lecturer = Lecturer('Dmitry', 'Zhuk')
cool_reviewer = Reviewer('Some', 'Buddy')
some_reviewer = Reviewer('Chack', 'Firsov')

some_student.courses_in_progress += ['Python', 'C#', 'GIT', 'Java','HTML']
some_student.courses_in_progress += ['Python', 'HTML', 'C++', 'GIT']

some_lecturer.courses_attached += ['Python', 'Git', 'C#', 'HTML']
best_lecturer.courses_attached += ['Python', 'Git', 'CSS']
some_reviewer.courses_attached += ['Python', 'Git', 'CSS']
cool_reviewer.courses_attached += ['Python', 'CSS']

some_student.rating_lecturer(some_lecturer, 'Python', 9)
some_student.rating_lecturer(best_lecturer, 'Python', 10)
best_student.rating_lecturer(some_lecturer, 'Python', 10)
best_student.rating_lecturer(some_lecturer, 'Git', 9)
some_student.rating_lecturer(best_lecturer, 'HTML', 7)

some_student.finished_courses += ['HTML', 'c++', 'notepad']
best_student.finished_courses += ['HTML', 'C++', 'SQL']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 8)
cool_reviewer.rate_hw(some_student, 'HTML', 5)
cool_reviewer.rate_hw(some_student, 'C++', 7)
some_reviewer.rate_hw(some_student, 'C++', 9)
some_reviewer.rate_hw(best_student, 'Git', 7)



print(best_student.grades)
print(cool_reviewer.courses_attached)
