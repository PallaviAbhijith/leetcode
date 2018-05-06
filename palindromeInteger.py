num = 1234
num = int(abs(num))
print(num)

print(str(num)[::-1])
print(str(num) == str(num)[::-1])


'''import unittest

class TestStringMethods(unittest.TestCase):

    def test_input(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
    
'''