
class Student:
    def __init__(self, last_name, first_name, grades_dict):
        self.last_name = last_name
        self.first_name = first_name
        self.grades_dict = grades_dict


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def semester_average(self, semester):
        grades = self.grades_dict.get(semester, [])
        if not grades:
            return None
        return sum(grades) / len(grades)


    def overall_average(self):
        all_grades = [grade for grades in self.grades_dict.values() for grade in grades]
        return sum(all_grades) / len(all_grades)


    def set_semester_grades(self, semester, grades):
        self.grades_dict[semester] = grades


    def get_semester_grades(self, semester):
        return self.grades_dict.get(semester, [])


grades_dict = {
    1: [3, 3, 3, 5],
    2: [3, 3, 4, 5],
    3: [4, 5, 3, 3],
    4: [5, 3, 3, 3]
}

student = Student("Кравчук", "Артем", grades_dict)

print(f"Студент: {student}")

semester = 2
avg = student.semester_average(semester)
print(f"Середній бал за {semester}-й семестр: {avg}")

overall_avg = student.overall_average()
print(f"Середній бал за всі роки навчання: {overall_avg}")

semester = 5
grades = [5, 4, 5, 4]
student.set_semester_grades(semester, grades)

semester_grades = student.get_semester_grades(semester)
print(f"Оцінки за {semester}-й семестр: {semester_grades}")
