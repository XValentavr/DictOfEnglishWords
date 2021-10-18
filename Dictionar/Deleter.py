from MySQLConnector import SelectToDelete


def delete_from_file() -> None:
    delete = SelectToDelete.get_data()
    file = open('D:\Work\TypesWHOIS\DictOfEnglishWords\corpora\words\en', 'r+')
    rows = file.readlines()
    file.seek(0)
    for line in rows:
        line = line.strip()
        if line not in delete:
            file.write(line + '\n')
    file.truncate()
    pass
