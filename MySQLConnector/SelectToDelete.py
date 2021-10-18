from MySQLConnector import Connect
from itertools import chain


def get_data() -> list:
    conn = Connect.connect()
    mycursor = conn.cursor()
    mycursor.execute("SELECT DomainName FROM an_error_data")
    myresult = mycursor.fetchall()
    myresult = map(list, myresult)
    flatten_list = list(chain.from_iterable(myresult))
    lst = [value for value in flatten_list]
    return lst
