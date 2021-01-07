class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        def add_courses(self, course_name):
            self.finished_course.append(course_name)

    def grades_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

#Получать оценки за лекции от студентов :)
# Реализуйте метод выставления оценок лекторам у класса Student
# (оценки по 10-балльной шкале, хранятся в атрибуте-списке).
# Лектор при этом должен быть закреплен за тем курсом, на который записан студент.
# у лектора надо создать список (так написано в ДЗ) для хранения оценок от студента
# у студента создайте метод. в который вы передадите объект лектора и оценку за курс
# в методе делаете сравнение: у каждого студента есть список courses_in_progress, а у
# каждого лектора есть список courses_attached, следовательно, сопоставляя элементы в этих
# двух списках мы можем найти общее название курса у двух объектов класса Student и
# Lector соответственно.
# Если общее название курса не нашлось, значит студент не может этому лектору поставить
# оценку и возвращаем сообщение об ошибке, например метод вернет False
# Если же общее название курса нашлось, то можно сказать что студент может выставить
# оценку лектору, и добавляем в список оценок Лектора (созданный на шаге 1)
# оценку от студента
# Внимание! Данный подод не идеален, и допускает добавление неограниченного
# количества оценок одним студентом, но судя по условию задачи на данном уровне
# обучения не требуется усложнять алгоритм. Также данный подход не позволяет отделить
# оценки за один курс от оценки за другой. В дальнейшем вы научитесь делать более сложные
# системы взаимодействй классов.
class Lecturer(Mentor):
     def __init__(self):
         self.grades = []
         self.courses_in_progress = []



# выставлять студентам оценки за домашние задания
class Reviewer(Mentor):
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

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)





print(best_student.grades)
print(cool_mentor)
