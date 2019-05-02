days_month = [0,30,28,31,30,31,30,31,30,31,30,31,30]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(month, year):

    if not 1<= month <=12:
        print ('invalid Month')
    elif month == 2 and is_leap(year):
        return 29
    else:
        return days_month[month]
print (days_in_month(2,2020))
