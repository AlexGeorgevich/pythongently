# Exercise #11: Hours, Minutes, Seconds

def getHoursMinutesSeconds(totalSeconds):
    minutes = 0
    hours = 0
    days = 0
    result = ""

    # Logic
    while totalSeconds != 0 and totalSeconds >= 60:
        totalSeconds -= 60
        minutes += 1
    while minutes != 0 and minutes >= 60:
        minutes -= 60
        hours += 1
    while hours != 0 and hours >= 24:
        hours -= 24
        days += 1
    
    # Display
    if days > 0:
        result += f"{days}d "
    if hours > 0:
        result += f"{hours}h "
    if minutes > 0:
        result += f"{minutes}m "
    if totalSeconds > 0:
        result += f"{totalSeconds}s"
    if [days, hours, minutes, totalSeconds] == [0, 0, 0, 0]:
        result += f"{totalSeconds}s"

    if result[-1] == " ":
        return result[:-1]
    return result

assert getHoursMinutesSeconds(30) == "30s"
assert getHoursMinutesSeconds(60) == "1m"
assert getHoursMinutesSeconds(90) == "1m 30s"
assert getHoursMinutesSeconds(3600) == "1h"
assert getHoursMinutesSeconds(3601) == "1h 1s"
assert getHoursMinutesSeconds(3661) == "1h 1m 1s"
assert getHoursMinutesSeconds(90042) == "25h 42s"
assert getHoursMinutesSeconds(0) == "0s"