# Exercise #16: Mode

def mode(numbers):
    if len(numbers) == 0:
        return None
    numberCount = {}
    mostFreqNumber = None
    mostFreqNumberCount = 0

    for number in numbers:
        if number not in numberCount:
            numberCount[number] = 0
        numberCount[number] += 1
        if numberCount[number] > mostFreqNumberCount:
            mostFreqNumber = number
            mostFreqNumberCount = numberCount[number]
    return mostFreqNumber

assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4