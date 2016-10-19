import unittest

class testUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_firstNameSame(self):
        self.assertEqual('kenny','kenny')

    def test_lastNameSame(self):
        self.assertEqual('batista','batista')

    def test_middleName(self):
        self.assertEqual('jesus','jesus')

if __name__ == '__main__':
    unittest.main()
