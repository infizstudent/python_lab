import pytest

from task_7 import Student
@pytest.fixture
def student():
    grades_dict = {
        1: [3, 3, 3, 5],
        2: [3, 3, 4, 5],
        3: [4, 5, 3, 3],
        4: [5, 3, 3, 3]
    }
    return Student('Kravchuk', 'Artem', grades_dict)


@pytest.mark.parametrize("semester, expected_average", [
    (2, 3.75),
    (3, 3.75),
    (5, None)
])
def test_semester_average(student, semester, expected_average):
    assert student.semester_average(semester) == expected_average


def test_calculate_overall_average(student):
    expected_average = 3.625
    assert student.calculate_overall_average() == expected_average


def test_set_grades_for_semester(student):
    semester = 5
    new_grades = [5, 4, 5, 4]
    student.set_grades_for_semester(semester, new_grades)
    assert student.get_grades_for_semester(semester) == new_grades


@pytest.mark.parametrize("semester, expected_grades", [
    (1, [3, 3, 3, 5]),
    (4, [5, 3, 3, 3]),
    (5, [])
])
def test_get_grades_for_semester(student, semester, expected_grades):
    assert student.get_grades_for_semester(semester) == expected_grades

