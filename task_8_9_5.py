import calendar


def print_days_in_month(m_name):
    m_name = m_name.strip().lower()
    month_number = 0

    try:
        month_number = list(calendar.month_name).index(m_name.capitalize())
    except ValueError:
        pass

    if month_number != 0:
        _, days_in_month = calendar.monthrange(1, month_number)
        print(f'Number of days in {m_name}: {days_in_month}')
    else:
        print('Invalid month name')


if __name__ == '__main__':
    month_name = input('Enter month name: ')
    print_days_in_month(month_name)
