import unittest

def add(x, y):
   return x + y

class TestAdd(unittest.TestCase):

   def test_add_two_numbers(self):
       result = add(2, 2)
       self.assertEqual(result, 4)

   def test_adding_negative_numbers(self):
       result = add(-1, -1)
       self.assertEqual(result, -2)

if __name__ == '__main__':
   unittest.main()
