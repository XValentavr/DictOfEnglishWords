import whois
from MySQLConnector.Connect import connect
from Dictionar import Handler
from Zones import SelectToCheck
CHECKER = None


def get_single(dot) -> None:
    # get connection
    conn = connect()
    #read from file
    #for name in Handler.generator():
    #read from DB
    for name in SelectToCheck.selector_to_check():
        try:
            new_name = name.strip() + dot
            # check income data
            av_domain = whois.whois(f"{new_name}")
            for key in av_domain.keys():
                # if data is TRUE then insert into table
                if key == "status":
                    if av_domain[key] != CHECKER:
                        list_domain = [(new_name.lower(), 'available')]
                        query = "INSERT INTO net_eng_zone (DomainName,SelfStatus) VALUES(%s,%s)"
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
