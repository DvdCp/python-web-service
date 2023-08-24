def calculateDecimalValue(literalString):
    # Calculatinf ASCII value for the received string 
    asciiValue = 0
    for char in literalString:
        asciiValue += ord(char)
    return asciiValue

def calculateOctValue(literalString):
    decimalValue = calculateDecimalValue(literalString)
    return oct(decimalValue)

def calculateHexValue(literalString):
    decimalValue = calculateDecimalValue(literalString)
    return hex(decimalValue)

def calculateBinValue(literalString):
    decimalValue = calculateDecimalValue(literalString)
    return bin(decimalValue)