# Exercise #9: Chess Square Color

def getChessSquareColor(column, row):
    if column not in range(0, 8) or row not in range(0, 8):
        return ''

    # My version
    if (column + row) % 2 == 0:
        return 'white'
    elif (column + row) % 2 != 0:
        return 'black'
    else:
        return ''
    # Alternative
    if column % 2 == row % 2:
        return 'white'
    else:
        return 'black'

assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == ''
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''