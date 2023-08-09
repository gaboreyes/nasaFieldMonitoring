import unittest
from unittest.mock import patch
from main import read_csv

class TestStringMethods(unittest.TestCase):

  @patch("builtins.open", create=True)
  def test_read_csv(self, mocked_open):
    mocked_open.return_value = 'mocked file data'
    output = read_csv()
    self.assertEqual(output, 'mocked file data')
    

if __name__ == '__main__':
  unittest.main()