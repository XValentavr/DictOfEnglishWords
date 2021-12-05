"""This module helps to get info about domains frow whois service"""

# local imports
import whois
from MySQLConnector.Connect import connect

CHECKER = None


def get_single(dot: str) -> None:
    """
    get domain from whois service
    :param dot:str
    :return: None
    """
    conn = connect()
    n = -1
    while (n := n + 1) <= 10:
        file = open('D:\Work\TypesWHOIS\DictOfEnglishWords\DomainsIsSet\domainsengdict_org_eng_zone.tsv', 'r')
        for name in file.readlines():
            try:
                new_name = name.replace('\n', '').strip() + dot
                # check income data
                av_domain = whois.whois(f"{new_name}")
                for key in av_domain.keys():
                    # if data is TRUE then insert into table
                    if key == "status":
                        if av_domain[key] != CHECKER:
                            list_domain = [(new_name.lower(), 'available')]
                            query = "INSERT INTO biz_eng_zone (DomainName,SelfStatus) VALUES(%s,%s)"
                            cursor = conn.cursor()
                            cursor.executemany(query, list_domain)
                            conn.commit()
            except whois.parser.PywhoisError:
                # if en exception occured insert into other table to check using another API
                list_domain = [(name.strip().lower() + dot, 'errored')]
                query = "INSERT INTO an_error_data (DomainName,SelfStatus) VALUES(%s,%s)"
                cursor = conn.cursor()
                cursor.executemany(query, list_domain)
                conn.commit()
