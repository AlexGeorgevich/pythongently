# Exercise #8: Read Write File

def writeToFile(filename, text):
    # Open the file in write mode 'w'
    with open(filename, 'w') as fileObj:
        fileObj.write(text)

def appendToFile(filename, text):
    # Open the file in append mode 'a'
    with open(filename, 'a') as fileObj:
        fileObj.write(text)
        
def readFromFile(filename):
    # Open the file in read mode 'r'
    with open(filename, 'r') as fileObj:
        # Read all of the text in the file and RETURN* it as a string:
        return fileObj.read()

writeToFile('greet.txt', 'Hello!\n') 
appendToFile('greet.txt', 'Goodbye!\n') 
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'