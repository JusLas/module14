import pytest

def get_fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return get_fibonacci_number(n-1)+get_fibonacci_number(n-2)

@pytest.mark.parametrize('n, result', (
   (0, 0),
   (1, 1),
   (2, 1),
   (3, 2),
   (10, 55),
   (15, 610)
))
def test_fibonacci(n, result):
   assert get_fibonacci_number(n) == result
