import pytest

def test_Check1() :
    assert False

def test_Check2() :
    assert True 

def test_Check3() :
    a = 4
    b = 3
    assert a == b+1
def test_login() :
    assert "admin" == "admin123"