import pytest

def test_hello():
    print('hello world!')
    assert 1

@pytest.mark.xfail()
def test_01():
    a = 'hello'
    b = 'hello world'
    assert a == b

@pytest.mark.xfail()
def test_02():
    a = 'hello'
    b = 'hello world'
    assert a != b

if __name__ == '__main__':
    pytest.main(['-v', 'test_xpass.py'])