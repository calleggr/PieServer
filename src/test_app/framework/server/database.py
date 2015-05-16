import sqlite3

def connect(name):
    conn = sqlite3.connect(name) #name of database
    c = conn.cursor()
    return conn, c

def close(conn):
    conn.commit()
    conn.close()


def createTable(table_name, column_names, c):
    """create a table in the database
       takes 3 params, a table_name, list of column_names,
       and a cursor object"""
    sql_statement = 'CREATE TABLE ' + table_name + '(INT ID PRIMARY KEY NOT NULL, '
    for col in column_names:
        sql_statement += col + ' TEXT NOT NULL, '
    sql_statement = sql_statement[:-2]
    sql_statement += ')'
    c.execute(sql_statement)

#CRUD OPERATIONS!!!!!!!!!!!!


def createEntry(table_name, list_of_params, c):
    """ INSERT
        inserts each element of list_of_params
        into table_name. no error checking, the list
        better have correct number of elements
        c = db cursor"""

    pass

def readEntry(table_name, column_name, value, c):
    """SELECT
        selects from table_name where column_name = value
        c = db cursor"""
    pass


def updateEntry(table_name, column_name, value, update_list_of_params, c):
    """UPDATE
        updates entry in table_name where column_name = value
        with the update_list_of_params. no error checking, the list
        better have correct number of elements
        c = db cursor"""
    pass

def deleteEntry(table_name, column_name, value, c):
    """DELETE
        deletes entry in table_name where column_name = value
        c = db cursor"""
    pass
