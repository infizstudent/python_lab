import os
import re


class StudentDataProcessor:
    def __init__(self):
        self.data_folder = 'data'
        self.output_folder = 'output'
        self.output_file = os.path.join(self.output_folder, 'invalid_data.txt')

    def process_student_data(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        file_names = ['name.txt', 'number_stud.txt', 'date_birth.txt', 'phone_number.txt']
        file_paths = [os.path.join(self.data_folder, file_name) for file_name in file_names]

        student_data = {}

        try:
            with open(file_paths[0], 'r') as f:
                names = f.read().splitlines()

            with open(file_paths[1], 'r') as f:
                numbers = f.read().splitlines()

            with open(file_paths[2], 'r') as f:
                dobs = f.read().splitlines()

            with open(file_paths[3], 'r') as f:
                phones = f.read().splitlines()
        except FileNotFoundError:
            print(f"Error: One or more files not found in '{self.data_folder}' directory.")
            return student_data

        with open(self.output_file, 'a') as f:
            for name, number, dob, phone in zip(names, numbers, dobs, phones):
                student = Student(name, number, dob, phone)

                if not student.is_valid():
                    f.write(f'Invalid data: {student.get_invalid_data()}\n')
                    continue

                student.format_data()
                student_data[student.number] = student.get_data()

        return student_data


def format_date(date):  # in utils
    parts = re.split(r'[-/]', date)
    if len(parts[0]) == 4:
        year, month, day = parts
    else:
        day, month, year = parts

    return '{}.{}.{}'.format(day.zfill(2), month.zfill(2), year)


def format_phone_number(phone):
    digits = re.sub(r'\D', '', phone)
    if not digits.startswith('+'):
        digits = '+380' + digits

    return '{}-{}-{}'.format(digits[:4], digits[4:7], digits[7:])


class Student:
    def __init__(self, name, number, date_of_birth, phone_number):
        self.name = name
        self.number = number
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number

    def is_valid(self):
        return (
                self.is_number_valid() and
                self.is_date_of_birth_valid() and
                self.is_phone_number_valid()
        )

    def is_number_valid(self):
        return re.match(r'^\d{8}$', self.number)

    def is_date_of_birth_valid(self):  # in utils
        parts = re.split(r'[-/]', self.date_of_birth)
        if len(parts[0]) == 4:
            year, month, day = parts
        else:
            day, month, year = parts

        return 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1900 <= int(year) <= 2100

    def is_phone_number_valid(self):
        return re.match(r'^\+?\d{1,3}[-\s]?\d{2,3}[-\s]?\d{3,4}[-\s]?\d{3,4}$', self.phone_number)

    def format_data(self):
        self.phone_number = format_phone_number(self.phone_number)
        self.date_of_birth = format_date(self.date_of_birth)

    def get_data(self):
        return {
            'name': self.name,
            'date_of_birth': self.date_of_birth,
            'phone_number': self.phone_number
        }

    def get_invalid_data(self):
        return {
            'name': self.name,
            'number': self.number,
            'date_of_birth': self.date_of_birth,
            'phone_number': self.phone_number
        }


def main():
    data_processor = StudentDataProcessor()
    students = data_processor.process_student_data()

    for number, data in students.items():
        number_with_prefix = 'XA' + number
        print(f'Number: {number_with_prefix}')
        print(f'Name: {data["name"]}')
        print(f'Date of Birth: {data["date_of_birth"]}')
        print(f'Phone Number: {data["phone_number"]}')
        print('---')


if __name__ == '__main__':
    main()
