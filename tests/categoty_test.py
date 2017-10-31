import unittest
from .models import category
Category = category.Category

class CategoryTest(unittest.TestCase):


    def setUp(self):
        self.new_category = Category

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

if __name__ == '__main__':
    unittest.main()
