from mysql import connector

def insert_string (literal_string, ascii_decimal_value):

    connection = connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')

    cursor = connection.cursor()

    if (ascii_decimal_value % 2) == 0:
        print('its even', flush=True)
        add_asciivalue = ("INSERT INTO evenasciivalues "
            "(literal_string, ascii_decimal_value) "
            "VALUES (%s, %s)")
    else:
        print('its odd', flush=True)
        add_asciivalue = ("INSERT INTO oddasciivalues "
            "(literal_string, ascii_decimal_value) "
            "VALUES (%s, %s)")

    try:  
        cursor.execute(add_asciivalue, (literal_string, ascii_decimal_value))
    finally:
        connection.commit()
    connection.close()