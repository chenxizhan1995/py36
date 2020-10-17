'''
Created on 2020年10月16日

@author: chenx
'''
import unittest
import weekday

class Test(unittest.TestCase):


    def test_day_difference(self):
        ''' 测试 day_difference 函数
        ''' 
        
        self.assertEqual(weekday.day_difference(200, 204), 4)
        self.assertEqual(weekday.day_difference(50, 50), 0)
        self.assertEqual(weekday.day_difference(100, 99), -1)

        

    def test_get_current_weekday(self):
        
        tests = [
            (1, 1, 2 ),
            (7, 1, 1 ),
            (4, 2, 6 ),
            (5, 7, 5 ),
            (1, 0, 1 ),
            (5, -1, 4),
            (6, 1, 7)
        ]
        for current_weekday, days_ahead, ret in tests:
            with self.subTest(current_weekday=current_weekday, days_ahead=days_ahead, ret = ret):
                self.assertEqual(weekday.get_weekday(current_weekday, days_ahead), ret)
                
    
    def test_get_birthday_weekday(self):
        self.assertEqual(weekday.get_birthday_weekday(1, 100, 101), 2)
        self.assertEqual(weekday.get_birthday_weekday(2, 101, 100), 1)
        self.assertEqual(weekday.get_birthday_weekday(6, 1, 2), 7)
        self.assertEqual(weekday.get_birthday_weekday(7, 2, 1), 6)
        self.assertEqual(weekday.get_birthday_weekday(1, 2, 1), 7)
        self.assertEqual(weekday.get_birthday_weekday(1, 10, 111), 4)        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()