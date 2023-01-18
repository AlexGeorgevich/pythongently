# Exercise #13: Sum & Product

def calculateSum(numbers):
    sumResult = 0
    if numbers == []:
        return sumResult
    else:
        for number in numbers:
            sumResult += number
        return sumResult

def calculateProduct(numbers):
    productResult = 1
    if numbers == []:
        return productResult

    else:
        for number in numbers:
            productResult *= number
        return productResult

assert calculateSum([]) == 0 
assert calculateSum([2, 4, 6, 8, 10]) == 30 
assert calculateProduct([]) == 1 
assert calculateProduct([2, 4, 6, 8, 10]) == 3840