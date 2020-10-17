'''
Created on 2020年10月16日

@author: chenx
'''

def day_difference(day1: int, day2: int) -> int:
    ''' 计算一年的第 day1 天和第 diay2 天之间有多少天，并返回。
    
    day1 和 day2 都在 1~365 之间。
    
    >>> day_difference(200, 204)
    4
    >>> day_difference(50, 50)
    0
    >>> day_difference(100, 99)
    -1
    '''
    
    return day2 - day1

# 给定星期几（x），经过 n 天后，是星期几？
# x，n，y
# 1, 1, 2
# 7, 1, 1
# 4, 2, 6
# 5, 7, 5
# 1, 0, 1
# 5, -1, 4
# 6, 1, 7
def get_weekday(current_weekday: int, days_ahead: int) -> int:
    ''' 星期 current_weekday 经过 day_ahead 天之后，是星期几？返回它。
    
    星期日到星期六依次对应 1，2，3，……，7
    
    
    '''
    
    return (current_weekday + days_ahead - 1) % 7 + 1


# 一年的第n天是星期x，则该年的第m天是星期几呀？
# 设 n，m 都在 1~365 之间，x 是 1~7，星期日（1），星期一（2），……，星期六（7）
# n, x, m, y
# 100,1, 101, 2
# 101,2, 100, 1
# 1, 6, 2, 7
# 2, 1, 1, 7
# 10, 1, 111, 4

def get_birthday_weekday(current_weekday: int, current_day: int, 
                         birthday: int) -> int:
    ''' 假设一年的第 current_day 是 星期 current_weekday, 那么这一年的第 birthday 
    天是星期几？
    
    用整数 1~7 对应表示星期日~星期六
    一年中的天数是 1 ~ 365
    '''
    
    day_diff = day_difference(current_day, birthday)
    return get_weekday(current_weekday, day_diff)
    



    