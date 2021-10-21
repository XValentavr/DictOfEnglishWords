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


def check_from_file():
    delete = selector_to_check()
    file = open('D:\Work\TypesWHOIS\DictOfEnglishWords\DomainsIsSet\\netZone.txt', 'r+')
    rows = file.readlines()
    rows = [rows.replace('\n', '').strip() for rows in rows]
    file.seek(0)
    for line in delete:
        if line not in rows:
            file.write(line + '\n')
    file.truncate()
    pass


