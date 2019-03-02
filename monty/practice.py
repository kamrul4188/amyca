import datetime


def confirm_date(date):
    date_format = '%d/%m/%Y'
    try:
        date_obj = datetime.datetime.strptime(date, date_format)
        return True
    except ValueError:
        print("Incorrect data format, should be dd/mm/yyyy")


while True:
    date = input('Date: ')
    confirm_date(date)


