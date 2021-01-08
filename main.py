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

# зачем тебе такая функция? Ее нет в задании. Мы вручную заполняем список курсов.
    def add_courses(self, course_name):
        self.finished_course.append(course_name)

# твоя функция для выставления оценок
    def grades_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# моя функция для выставления оценок лекторам.
    def rating_lecturer(self, lecturer, course, grade):
        """ Implement the method for the grading of the lecturers """
        if 0 <= grade <= 10:  # необязательное условие - можно удалить этот блок if/else
            # if isinstance проверка на соответствие: lecturer, Lecturer просто проверяет есть ли вообще такой лектор
            # course in self.courses_in_progress есть ли курс у студента. Progress в смысле не завершено.
            # course in lecturer.courses_attached есть ли у лектора такой предмет для чтения.
            if isinstance(lecturer,
                          Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                # есть ли курс
                if course in lecturer.rating_grades:  # lecturer. <-- это обращение к классу. Словарь искать там.
                    lecturer.rating_grades[course] += [grade]  # тут понятно? Это добавление в словарь. Поищи как
                    # правильно добавить ['ключ', 'значение'] и сразу текст обретет смысл.
                    # lecturer. <-- это ссылка на хранилище словаря. В класс Lecturer. rating_grade - название
                    # [course] это 'key' += [grade] это наша новая оценка лектору от студента (от 1 до 10).
                else:
                    lecturer.rating_grades[course] = [grade]  # инициализация первой оценки т.к. в самом начале оценок
                    # нет. Первая оценка проскакивает мимо if (пусто) сразу на else. Затем if сверяет со списком а
                    #  += [grade] добавляет к существующему.
            else:
                return 'Error'
        else:
            return 'Wrong grade, only 0 to 10'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # общий список курсов lecturer и reviewer

    def __repr__(self):  # это как и __str__ для вывода
        return self.name + ' ' + self.surname + ' courses attached: ' + repr(self.courses_attached)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)  # добавили метод super для связки с родителем
        # self.grades = []  # не используем
        # self.courses_in_progress = []  # не используем
        self.rating_grades = {}  # создали словарь для записи оценок. Именно словарь! {'key', 'value'} дальше будем
        # искать нужные данные по ключу из словаря.

    def __lt__(self, other):  # магический метод сравнения. Нужно написать функцию поиска среднего значения
        # ниже average_grade - это название функции для поиска
        if average_grade(self.rating_grades) < average_grade(other.rating_grades):
            return 'The best result is ' + other.name + ' ' + other.surname + ' with a rating ' +\
                   average_grade(other.rating_grades)
        elif average_grade(self.rating_grades) == average_grade(other.rating_grades):
            return 'the same result'
        else:
            return 'The best result is ' + self.name + ' ' + self.surname + ' with a rating ' +\
                   average_grade(self.rating_grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """ выставлять студентам оценки за домашние задания """  # так положено, для обьяснения действий внутри
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_grade(some_grades):  # some_grades можешь заменить на любое другое слово
    """ Поиск среднего значения оценки """
    all_grades = []  # добавляем пустое хранилище для записи всех всех всех оценок одного студента
    for subject, grades in some_grades.items():  # это разбиение словаря на ключ - значение.
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
        return "error"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)


print(best_student.grades)
print(cool_mentor)
