"""
this module delete recurring data from file and database
"""

# local imports
from MySQLConnector import Connect
from itertools import chain


def selector_to_check() -> list:
    """
    get data from database to delete
    :return: list
    """
    conn = Connect.connect()
    mycursor = conn.cursor()
    mycursor.execute("SELECT distinct  DomainName FROM  an_error_data")
    myresult = mycursor.fetchall()
    myresult = map(list, myresult)
    flatten_list = list(chain.from_iterable(myresult))
    lst = [value for value in flatten_list]
    return lst


def check_from_file() -> None:
    """
    get data from file and compare with data from database and delete if true
    :return: None
    """
    delete = selector_to_check()
    file = open('D:\Work\TypesWHOIS\DictOfEnglishWords\DomainsIsSet\\domainsengdict_biz_eng_zone.tsv', 'r+')
    rows = file.readlines()
    rows = [rows.replace('\n', '').strip() for rows in rows]
    file.seek(0)
    for line in rows:
        if line not in delete:
            file.write(line + '\n')
    file.truncate()


# start in local
check_from_file()
