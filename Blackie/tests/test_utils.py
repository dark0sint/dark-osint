import unittest
from core import utils

class TestUtils(unittest.TestCase):
    def test_load_payloads(self):
        payloads = utils.load_payloads()
        self.assertIsInstance(payloads, list)
        self.assertTrue(all(isinstance(p, str) for p in payloads))

if __name__ == '__main__':
    unittest.main()
