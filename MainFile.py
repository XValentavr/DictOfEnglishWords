"""
start point
"""
if __name__ == '__main__':
    # local imports
    from WHOISChecker import Getter
    from Dictionar import Deleter

    # Deleter.delete_from_file()
    Getter.get_single('.biz')
