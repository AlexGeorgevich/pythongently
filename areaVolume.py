# Exercise #4: Area & Volume

def area(length, width):
    if length < 0 or width < 0:
        raise Exception('Dimensions must be positive number')
    else:
        return length * width
def perimeter(length, width):
    if length < 0 or width < 0:
        raise Exception('Dimensions must be positive numbers')
    else:
        return length + width + length + width
def volume(length, width, height):
    if length < 0 or width < 0 or height < 0:
        raise Exception('Dimensions must be positive numbers')
    else:
        return length * width * height
def surfaceArea(length, width, height):
    if length < 0 or width < 0 or height < 0:
        raise Exception('Dimensions must be positive numbers')
    else:
        return (length * width * 2) + (length * height * 2) + (width * height * 2)

assert area(10, 10) == 100 
assert area(0, 9999) == 0 
assert area(5, 8) == 40 
assert perimeter(10, 10) == 40 
assert perimeter(0, 9999) == 19998 
assert perimeter(5, 8) == 26 
assert volume(10, 10, 10) == 1000 
assert volume(9999, 0, 9999) == 0 
assert volume(5, 8, 10) == 400 
assert surfaceArea(10, 10, 10) == 600 
assert surfaceArea(9999, 0, 9999) == 199960002 
assert surfaceArea(5, 8, 10) == 340