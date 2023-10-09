import unittest
import sys
from checks import check_arguments, check_date


class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """
    
    def test_check_arguments(self):
        args_true = [1 , 2 , 3]
        self.assertEqual(check_arguments(args_true), True)

        #extra arguments
        args_False = [1 , 2 , 3 , 4]
        with self.assertRaises(SystemExit) as cm:
            
           self.assertEqual(check_arguments(args_False), cm.exception)
        
        #less arguments
        args_False2 = [1 , 2]
        with self.assertRaises(SystemExit) as ce:
            
           self.assertEqual(check_arguments(args_False2), ce.exception)

class TestCheckDate(unittest.TestCase):
    """ 
    Class used for testing the check_date() function from checks.py

    """
    def test_date(self):
        date_true = "1999-05-02"
        self.assertEqual(check_date(date_true), True)

        #none existing date
        date_false = "1999-34-85"
        with self.assertRaises(SystemExit) as cm:
            
           self.assertEqual(check_date(date_false), cm.exception)

        #wrong date format
        date_wrong = "1999/34/85"
        with self.assertRaises(SystemExit) as cm:
            
           self.assertEqual(check_date(date_wrong), cm.exception)
           
if __name__ == '__main__':
    unittest.main()
    