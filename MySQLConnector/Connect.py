"""
This module creates local database connection
"""

# local imports
import mysql
from mysql.connector import MySQLConnection, Error


def connect():
    """
    create database connect
    :return: database connection
    """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='domainsengdict',
                                       user='root',
                                       password='root')

    except Error as e:
        print('Error:', e)

    finally:
        return conn
