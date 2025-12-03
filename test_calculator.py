from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

def test_multiply():
    assert multiply(2, 4) == 8

def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    try:
        divide(10, 0)
        assert False  # should not reach here
    except ValueError:
        assert True