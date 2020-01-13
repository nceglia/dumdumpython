import sys


def make_a_list():
    """
    make a list object
    the object should have 4 elements
    """
    mylist = [3,6,9,12]
    return mylist



if __name__ == '__main__':
    alist = make_a_list()
    assert type(alist) == list
    assert len(alist) == 4
    print ("PASSED FIRST TEST!!! Congratulations.")
