import sqlite3

def connect(name):
    conn = sqlite3.connect(name) #name of database
    c = conn.cursor()

def close(c):
    c.commit()
    c.close()


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


def createEntry():
    pass

def readEntry():
    pass


def updateEntry():
    pass

def deleteEntry():
    pass
