# Exercise #20: Leap Year

def isLeapYear(year):
    # My initial solution:
    # if year % 4 == 0:
    #     if year % 100 == 0:
    #         if year % 400 == 0:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return True
    # else:
    #     return False

    # Secondary, more readable solution:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

assert isLeapYear(1999) == False 
assert isLeapYear(2000) == True 
assert isLeapYear(2001) == False 
assert isLeapYear(2004) == True 
assert isLeapYear(2100) == False 
assert isLeapYear(2400) == True