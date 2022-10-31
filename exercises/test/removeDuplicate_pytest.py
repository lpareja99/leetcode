from removeDuplicate import *

s1 = [1,1,2]
s2 = [0,0,1,1,1,2,2,3,3,4]
s3 = [0,0,0,0]
s4 = [6]

rd = RemoveDuplicates

def test_RDs1():
    assert rd.removeDuplicatesI(s1) == [1,2]

def test_RDs2():
    assert rd.removeDuplicatesI(s2) == [0,1,2,3,4]

def test_RDs3():
    assert rd.removeDuplicatesI(s3) == [0]

def test_RDs4():
    assert rd.removeDuplicatesI(s1) == [6]