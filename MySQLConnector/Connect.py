import mysql
from mysql.connector import MySQLConnection, Error


# create database connect
def connect():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='domainsengdict',
                                       user='root',
                                       password='root')

    except Error as e:
        print('Error:', e)

    finally:
        return conn
