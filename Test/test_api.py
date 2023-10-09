import unittest
from api import call_get

class TestAPI(unittest.TestCase):
    """
    Class used for testing the call_get() function in api.py
    """
    def test_call_get(self):
        #valid URL
        test_url = "https://api.frankfurter.app/2000-01-03?from=AUD&to=USD"
        test_expected_status_code = 200
        self.assertEqual(call_get(test_url).status_code, test_expected_status_code)

        #Bad URL
        test_url_false = "https://api.frankfurter.app/2000-01-03&from=USD&to=USD"
        with self.assertRaises(SystemExit) as cm:
            
           self.assertEqual(call_get(test_url_false).status_code, cm.exception)

if __name__ == '__main__':
    unittest.main()
