import unittest
from fizz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_affiche(self):
        fizzbuzz = FizzBuzz()
        
        self.assertEqual(fizzbuzz.affiche(5, 10), "BuzzFizz78FizzBuzz")
        
        self.assertEqual(fizzbuzz.affiche(10, 16), "Buzz11Fizz1314FrisBee16")

if __name__ == '__main__':
    unittest.main()




