import pytest

def add(x, y):
   return x + y

def test_add():
   result = add(2, 2)
   assert result == 4

def test_add_negative():
   result = add(-1, -1)
   assert result == -2

def divide(x, y):
   return x / y

def test_divide():
   result = divide(4, 2)
   assert result == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)
