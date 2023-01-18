# Exercise #14: Average

def average(numbers):
    if numbers == None:
        return None
    else:
        total = 0
        for number in numbers:
            total += number
        return total / len(numbers)

# Alternative, using calculateSum function from my sumProduct module
# import sumProduct
# def average(numbers):
#     return (sumProduct.calculateSum(numbers) / len(numbers)) if numbers != None else None 

assert average([1, 2, 3]) == 2 
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2 
assert average([12, 20, 37]) == 23 
assert average([0, 0, 0, 0, 0]) == 0
import random 
random.seed(42) 
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3] 
for i in range(1000):
    random.shuffle(testData) 
    assert average(testData) == 2