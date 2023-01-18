# Exercise #12: Smallest & Biggest

def getSmallest(numbers):
    if numbers == []:
        return None
    else:
        smallest = numbers[0]
        for number in numbers:
            if number <= smallest:
                smallest = number
        return smallest

assert getSmallest([1, 2, 3]) == 1 
assert getSmallest([3, 2, 1]) == 1 
assert getSmallest([28, 25, 42, 2, 28]) == 2 
assert getSmallest([1]) == 1 
assert getSmallest([]) == None

def getBiggest(numbers):
    if numbers == []:
        return None
    else:
        biggest = numbers[0]
        for number in numbers:
            if number >= biggest:
                biggest = number
        return biggest

assert getBiggest([1, 2, 3]) == 3
assert getBiggest([3, 2, 1]) == 3 
assert getBiggest([28, 25, 42, 2, 28]) == 42 
assert getBiggest([1]) == 1 
assert getBiggest([]) == None