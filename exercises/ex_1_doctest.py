def add(x, y):
   """Return the sum of x and y
   
   >>> add(2, 2)
   4
   >>> add(1, 1)
   2
   """

   return x + y


def square(x):
   """Return the square of x
   
   >>> square(2)
   4
   >>> square(1)
   1
   >>> square(0)
   0
   """

   return x**2

if __name__ == '__main__':
   import doctest
   doctest.testmod()
