"""
This module creates all words from corpora library
"""


def generator() -> list:
    """
    get all english words
    :return: list
    """

    file = open('D:\Work\TypesWHOIS\DictOfEnglishWords\corpora\words\en', 'r')
    dict_list = [line for line in file]
    return dict_list
