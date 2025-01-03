def calcul(length, width: float=None, height: float=None):
    if (width == None) and (height == None):
        square = length * length
    elif (height == None):
        square = length * width
    else:
        square = length * width * height
    return square
