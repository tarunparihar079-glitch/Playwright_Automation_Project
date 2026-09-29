import pytest

def test_Check1() :
    assert False

def test_Check2() :
    assert True 

@pytest.mark.login
def test_Check3() :
    a = 4
    b = 3
    assert a == b+1
    assert a == b 

@pytest.mark.login
def test_Check4() :
    T = "tarun"
    assert T.upper() == "TARUN"   

def test_login_insta() :
    assert "admin" == "admin"