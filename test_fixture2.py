import pytest

@pytest.fixture()
def user():
    print('获取用户名')
    a = 'yoyo'
    return a

def test_1(user):
    assert user == 'yoyo111'

@pytest.fixture()
def user1():
    print('获取用户名')
    a = 'yoyo'
    assert a == 'yoyo123'
    return a

def test_2(user1):
    assert user == 'yoyo'

if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture2.py'])