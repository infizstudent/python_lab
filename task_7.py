import statistics
from itertools import chain


class Student:
    def __init__(self, last_name, first_name, grades_dict):
        self.last_name = last_name
        self.first_name = first_name
        self.grades_dict = grades_dict

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def semester_average(self, semester):
        return statistics.mean(filter(None, self.grades_dict.get(semester))) if self.grades_dict.get(semester) else None

    def overall_average(self):
        all_grades = chain.from_iterable(self.grades_dict.values())
        all_grades = (grade for grade in all_grades if grade is not None)
        return statistics.mean(all_grades)

    def set_semester_grades(self, semester, grades):
        self.grades_dict[semester] = grades

    def get_semester_grades(self, semester):
        return self.grades_dict.get(semester, [])

    def set_semester_grades(self, semester, grades):
        self.grades_dict[semester] = grades


if __name__ == '__main__':
    grades_dict = {
        1: [3, 3, 3, 5],
        2: [3, 3, 4, 5],
        3: [4, 5, 3, 3],
        4: [5, 3, 3, 3]
    }

    student = Student('Kravchuk', 'Artem', grades_dict)

    print(f'Student: {student}')

    semester = 2
    avg = student.semester_average(semester)
    print(f'Avg grade for semester {semester}: {avg}')

    overall_avg = student.overall_average()
    print(f'Avg grade for all semesters: {overall_avg}')

    semester = 5
    grades = [5, 4, 5, 4]
    student.grades_dict = {**student.grades_dict, **{semester: grades}}

    semester_grades = student.get_semester_grades(semester)
    print(f'Grades for semester {semester}: {semester_grades}')
