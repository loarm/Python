# program to display calendar of given month of the year


import calendar

def mycal():
    yy = int(input('Enter year: '))
    mm = int(input('Enter month: '))
    return print(calendar.month(yy, mm))


mycal()
