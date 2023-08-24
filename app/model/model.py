from mysql import connector
from utils.utils import *

def insertString (literalString):

    connection = connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')

    cursor = connection.cursor()

    decimalValue = calculateDecimalValue(literalString)
    insertEvenOrOddValue(decimalValue)

    # octValue = calculateOctValue(literalString)
    # hexValue = calculateHexValue(literalString)
    # binValue = calculateBinValue(literalString)

    add_asciivalue = ("INSERT INTO alphastrings "
    "(alphaValue) "
    "VALUES (%s)")

    try:  
        cursor.execute(add_asciivalue, (literalString,))
    except Exception as err:
        print('insertString: ', err, flush=True)
    finally:
        connection.commit()
    connection.close()

def insertEvenOrOddValue (decimalValue):

    connection = connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')

    cursor = connection.cursor()

    if (decimalValue % 2) == 0:
        add_asciivalue = ("INSERT INTO evenvalues "
            "(decimalEvenValue) "
            "VALUES (%s)")
    else:
        add_asciivalue = ("INSERT INTO oddvalues "
            "(decimalOddValue) "
            "VALUES (%s)")

    try:  
        item = cursor.execute(add_asciivalue, (decimalValue,))
        print(item, flush=True)
    except Exception as err:
        print('insertEvenOrOddValue: ', err, flush=True)
    finally:
        connection.commit()
    connection.close()