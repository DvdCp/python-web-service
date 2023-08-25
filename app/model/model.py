from mysql import connector
from utils.utils import *

def connectToDb(user='root', password='root', host='mysql', port="3306", database='db'):
    try:
        connection = connector.connect( 
            user=user, password=password, host=host, port=port, database=database )
        print('Connected to DB', flush=True)
    except Exception as err:
        print('connectToDb: ', err, flush=True)

    return connection;
    
def insertStringIntoDb(literalString):

    connection = connectToDb()  

    cursor = connection.cursor()

    decimalValue = calculateDecimalValue(literalString)
    evenOrOddRowId, isOdd = insertEvenOrOddValueIntoDb(decimalValue)

    octValue = calculateOctValue(literalString)
    octRowId = insertOctValueIntoDb(octValue)

    hexValue = calculateHexValue(literalString)
    hexRowId = insertHexValueIntoDb(hexValue)

    binValue = calculateBinValue(literalString)
    binRowId = insertBinValueIntoDb(binValue)

    if isOdd:
        add_asciivalue = ("INSERT INTO alphastrings "
            "(alphaValue, oddValueId, octValueId, hexValueId, binValueId) "
            "VALUES (%s, %s, %s, %s, %s)")
    else:
        add_asciivalue = ("INSERT INTO alphastrings "
            "(alphaValue, evenValueId, octValueId, hexValueId, binValueId) "
            "VALUES (%s, %s, %s, %s, %s)")

    try:  
        cursor.execute(add_asciivalue, (literalString, evenOrOddRowId, octRowId, hexRowId, binRowId))

    except Exception as err:
        print('insertStringIntoDb: ', err, flush=True)
    
    finally:
        connection.commit()
        connection.close()


def insertEvenOrOddValueIntoDb (decimalValue):

    connection = connectToDb()

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
    
def insertOctValueIntoDb (octValue):

    connection = connectToDb()
    cursor = connection.cursor()

    query = ("INSERT INTO octvalues "
        "(octValue) "
        "VALUES (%s)")

    try:  
        cursor.execute(query, (octValue,))
        lastId = cursor.lastrowid
    
    except Exception as err:
        print('insertOctValueIntoDb: ', err, flush=True)

    finally:
        connection.commit()
        connection.close()
    
        return lastId

def insertHexValueIntoDb (hexValue):

    connection = connectToDb()
    cursor = connection.cursor()

    query = ("INSERT INTO hexvalues "
        "(hexValue) "
        "VALUES (%s)")

    try:  
        cursor.execute(query, (hexValue,))
        lastId = cursor.lastrowid
    
    except Exception as err:
        print('insertHexValueIntoDb: ', err, flush=True)

    finally:
        connection.commit()
        connection.close()
    
        return lastId

def insertBinValueIntoDb (binValue):

    connection = connectToDb()
    cursor = connection.cursor()

    query = ("INSERT INTO binvalues "
        "(binValue) "
        "VALUES (%s)")

    try:  
        cursor.execute(query, (binValue,))
        lastId = cursor.lastrowid
    
    except Exception as err:
        print('insertBinValueIntoDb: ', err, flush=True)

    finally:
        connection.commit()
        connection.close()
    
        return lastId
