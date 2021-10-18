from MySQLConnector import Connect
from itertools import chain


def selector_to_check() -> list:
    conn = Connect.connect()
    mycursor = conn.cursor()
    mycursor.execute("SELECT DomainName FROM com_eng_zone")
    myresult = mycursor.fetchall()
    myresult = map(list, myresult)
    flatten_list = list(chain.from_iterable(myresult))
    lst = [value for value in flatten_list]
    return lst
