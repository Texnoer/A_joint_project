all_lecturer = []  # список всех лекторов


class Student:
    def __init__(self, name, surname, gender):
        self.name = name  # имя
        self.surname = surname  # фамилия
        self.gender = gender  # пол
        self.finished_courses = []  # список завершенных курсов. СПИСОК = [1, 2, 3, 4...]
        self.co_in_pr = []  # courses_in_progress список курсов в процессе. СПИСОК = [1, 2, 3, 4...]
        self.grades = {}  # grades все оценки. СЛОВАРЬ = {'ключ-1': 'значение', 'ключ-2': 'значение'}
        
    def rating_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.co_in_pr and course in lecturer.co_att:
            if course in lecturer.rat_gr:
                lecturer.rat_gr[course] += [grade]  # то же самое что и rat_gr = {'course': 'grade', 'course2':...
            else:
                lecturer.rat_gr[course] = [grade]
        else:
            return 'Error'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.co_att = []  # courses_attached СПИСОК = [1, 2, 3, 4...]
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rat_gr = {}  # rating_grades СЛОВАРЬ = {'ключ-1': 'значение', 'ключ-2': 'значение'}
        all_lecturer.append(self)  # добавляем в глобальный список все лекторов. строка №1

