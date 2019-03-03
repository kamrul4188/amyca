import datetime


def format_to_datetime(date):
    date_format = '%d/%m/%Y'
    try:
        date_obj = datetime.datetime.strptime(date, date_format).date()
        return date_obj
    except ValueError:
        print("Incorrect data format, should be dd/mm/yyyy")


while True:
    date = input('Date: ')
    print(format_to_datetime(date))


