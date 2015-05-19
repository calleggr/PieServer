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
    sql_statement = 'CREATE TABLE ' + table_name + '(ID INTEGER PRIMARY KEY, '
    for col in column_names:
        sql_statement += col + ' TEXT NOT NULL, '
    sql_statement = sql_statement[:-2]
    sql_statement += ');'
    c.execute(sql_statement)

#CRUD OPERATIONS!!!!!!!!!!!!


def createEntry(table_name, list_of_cols, list_of_params, c):
    """INSERT
    inserts each element of list_of_params
    into table_name. no error checking, the list
    better have correct number of elements
    c = db cursor"""
    sql_statement = 'INSERT INTO ' + table_name + ' (ID, '
    for val in list_of_cols:
        sql_statement +=val + ", "
    sql_statement = sql_statement[:-2]
    sql_statement += ') VALUES (NULL, '
    for val in list_of_params:
        sql_statement +="'" + val + "'" + ", "
    sql_statement = sql_statement[:-2]
    sql_statement += ');'
    #print sql_statement
    c.execute(sql_statement)
    for row in c:
        print row

def readEntry(table_name, column_name, search, c):
    """SELECT
        selects row from table_name where column_name = search
        c = db cursor"""
    sql_statement = "SELECT * FROM " + table_name + " WHERE " + column_name + "=" + "'" + str(search) + "'" + ";"
    print sql_statement
    c.execute(sql_statement)
    return_str = []
    i = 0;
    for row in c:
        return_str.append([])
        for val in row:
            return_str[i].append(str(val))
        i+=1
    return return_str


def readAll(table_name, c):
    """SELECT
        selects all rows from table_name
        c = db cursor"""
    sql_statement = "SELECT * FROM " + table_name + ";"
    c.execute(sql_statement)
    return_str = []
    i = 0;
    for row in c:
        return_str.append([])
        for val in row:
            return_str[i].append(str(val))
        i+=1
    return return_str



def updateEntry(table_name, column_name, update_value, look_up_col, look_up_val, c):
    """UPDATE
        updates an entrys value in column_name to update_value
         in table_name where look_up_col = look_up_val
        with the update_value.
        c = db cursor"""
    sql_statement = "UPDATE " + table_name + " SET " + column_name + "=" + "'" + str(update_value) +"'"+ " WHERE " + look_up_col + "=" + "'" + str(look_up_val) +"'"+ ";"
    c.execute(sql_statement)


def deleteEntry(table_name, column_name, value, c):
    """DELETE
        deletes entry in table_name where column_name = value
        c = db cursor"""
    sql_statement = "DELETE FROM " + table_name + " WHERE " + column_name + "=" + "'" + str(value) + "'" + ";"
    c.execute(sql_statement)
