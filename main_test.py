import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    mylist = [10, 20, 30, 40, 50]
    ret = main.halfValue(mylist)
    print(f'Your return value is {ret}')
    assert len(ret) == 5
    assert ret[0] == 5
    assert ret[1] == 10
    assert ret[2] == 15
    assert ret[3] == 20
    assert ret[4] == 25

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    mylist = [1, 2, 3, 4, 5]
    ret = main.halfValue(mylist)
    print(f'Your return value is {ret}')
    assert len(ret) == 5
    assert ret[0] == 0
    assert ret[1] == 1
    assert ret[2] == 1
    assert ret[3] == 2
    assert ret[4] == 2
