import unittest
import pandas as pd
from src.preprocess import preprocess_data

class TestPreprocess(unittest.TestCase):
    def test_preprocess_data(self):
        scaled_data, _ = preprocess_data('../data/customer_data.csv')
        self.assertEqual(scaled_data.shape[1], 2)  # Example: 2 features

if __name__ == '__main__':
    unittest.main()
