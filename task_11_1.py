from datetime import datetime


def convert_date_format(date_str):
    try:
        date = datetime.strptime(date_str, '%d.%m.%Y')
        return date.strftime('%d.%m.%Y')
    except ValueError:
        try:
            date = datetime.strptime(date_str, '%Y/%m/%d')
            return date.strftime('%d.%m.%Y')
        except ValueError:
            return None


def process_file(file_path):
    new_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            date = line.strip()
            converted_date = convert_date_format(date)
            if converted_date:
                new_lines.append(converted_date)
            else:
                new_lines.append(date)

    with open(file_path, 'w') as file:
        file.write('\n'.join(new_lines))


if __name__ == '__main__':
    process_file('dats.txt')
