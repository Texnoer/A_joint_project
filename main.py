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
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)  # добавили метод super для связки с родителем
        self.grades = []
        self.courses_in_progress = []
        self.rating_grades = {}  # создали словарь для записи оценок. Именно словарь! {'key', 'value'} дальше будем
        # искать нужные данные по ключу из словаря.


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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)


print(best_student.grades)
print(cool_mentor)
