# Exercise #7: ASCII Table

def printASCIItable():
    for number in range(32, 127):
        print("{} {}".format(number, chr(number)))

printASCIItable()