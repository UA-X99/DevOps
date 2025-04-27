import unittest
import act7_1_numeros

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        #crear classe
        self.assertEqual('foo'.upper(), 'FOO')

class TestRacionales(unittest.TestCase):
    def test_print_hello(self):
        m = 0
        racionales = act7_1_numeros.Racionales(m)
        self.assertEqual(racionales.print_hello(), "Hello Alejandro")

if __name__ == '__main__':
    unittest.main()