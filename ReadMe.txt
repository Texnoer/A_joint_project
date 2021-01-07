all_lecturer = []  # ������ ���� ��������


class Student:
    def __init__(self, name, surname, gender):
        self.name = name  # ���
        self.surname = surname  # �������
        self.gender = gender  # ���
        self.finished_courses = []  # ������ ����������� ������. ������ = [1, 2, 3, 4...]
        self.co_in_pr = []  # courses_in_progress ������ ������ � ��������. ������ = [1, 2, 3, 4...]
        self.grades = {}  # grades ��� ������. ������� = {'����-1': '��������', '����-2': '��������'}
        
    def rating_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.co_in_pr and course in lecturer.co_att:
            if course in lecturer.rat_gr:
                lecturer.rat_gr[course] += [grade]  # �� �� ����� ��� � rat_gr = {'course': 'grade', 'course2':...
            else:
                lecturer.rat_gr[course] = [grade]
        else:
            return 'Error'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.co_att = []  # courses_attached ������ = [1, 2, 3, 4...]
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rat_gr = {}  # rating_grades ������� = {'����-1': '��������', '����-2': '��������'}
        all_lecturer.append(self)  # ��������� � ���������� ������ ��� ��������. ������ �1

