from mysql import connector
from utils.utils import *

def insertString (literalString):

    connection = connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')

    cursor = connection.cursor()

    decimalValue = calculateDecimalValue(literalString)
    evenOrOddRowId, isOdd = insertEvenOrOddValue(decimalValue)

    # octValue = calculateOctValue(literalString)
    # hexValue = calculateHexValue(literalString)
    # binValue = calculateBinValue(literalString)

    if isOdd:
        add_asciivalue = ("INSERT INTO alphastrings "
            "(alphaValue, oddValueId) "
            "VALUES (%s, %s)")
    else:
        add_asciivalue = ("INSERT INTO alphastrings "
            "(alphaValue, evenValueId) "
            "VALUES (%s, %s)")

    try:  
        cursor.execute(add_asciivalue, (literalString, evenOrOddRowId))
    except Exception as err:
        print('insertString: ', err, flush=True)
    finally:
        connection.commit()
    connection.close()

def insertEvenOrOddValue (decimalValue):

    connection = connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')

    cursor = connection.cursor()
    isOdd = False;

    if (decimalValue % 2) == 0:
        add_asciivalue = ("INSERT INTO evenvalues "
            "(decimalEvenValue) "
            "VALUES (%s)")
    else:
        add_asciivalue = ("INSERT INTO oddvalues "
            "(decimalOddValue) "
            "VALUES (%s)")
        isOdd = True

    try:  
        cursor.execute(add_asciivalue, (decimalValue,))
        lastId = cursor.lastrowid
    except Exception as err:
        print('insertEvenOrOddValue: ', err, flush=True)
    finally:
        connection.commit()
    
    connection.close()
    return (lastId, isOdd)
