import statistics
from itertools import chain


class Student:
    def __init__(self, last_name, first_name, grades_dict):
        self.last_name = last_name
        self.first_name = first_name
        self.grades_dict = grades_dict

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def semester_average(self, grades_semester):
        return statistics.mean(self.grades_dict[grades_semester]) if grades_semester in self.grades_dict else None

    def calculate_overall_average(self):
        all_grades = chain.from_iterable(self.grades_dict.values())
        return statistics.mean((grade for grade in all_grades))

    def set_grades_for_semester(self, grades_semester, grades):
        self.grades_dict[grades_semester] = grades

    def get_grades_for_semester(self, grades_semester):
        return self.grades_dict.get(grades_semester, [])


if __name__ == '__main__':
    grades_dict = {
        1: [3, 3, 3, 5],
        2: [3, 3, 4, 5],
        3: [4, 5, 3, 3],
        4: [5, 3, 3, 3]
    }

    student = Student('Kravchuk', 'Artem', grades_dict)

    print(f'Student: {student}')

    grades_semester = 2
    avg = student.semester_average(grades_semester)
    print(f'Avg grade for semester {grades_semester}: {avg}')

    overall_avg = student.calculate_overall_average()
    print(f'Avg grade for all semesters: {overall_avg}')

    grades_semester = 5
    new_grades = [5, 4, 5, 4]
    student.grades_dict = {**student.grades_dict, **{grades_semester: new_grades}}

    semester_grades = student.get_grades_for_semester(grades_semester)
    print(f'Grades for semester {grades_semester}: {semester_grades}')
