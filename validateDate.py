from leapYear import isLeapYear

non_leap_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
leap_year = non_leap_year.copy()
leap_year.update({2: 29})

def isValidDate(year, month, day):
    if day not in range(1, 32) or month not in range(1, 13):
        return False
    elif isLeapYear(year):
        return True if day <= leap_year[month] else False
    else:
        return True if day <= non_leap_year[month] else False


assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False

import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay
