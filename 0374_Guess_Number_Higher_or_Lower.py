"""
Игра с угалыванием числа. 
Задача на классичесикй бинарный поиск.

"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
class Solution:
    """
    Два варианты бинарного поиска. Задачу так же можно решить тернарным поиском за время log3(n)
    """
    def guessNumber(self, n: int) -> int:
        l, h = 1, n
        mid = (l + h) >> 1 #    >> в теории быстрее чем // 2
        while (res := guess(mid)) != 0:
            if res == 1: l = mid + 1
            else: h = mid - 1
            mid = (l + h) >> 1
        return mid
      
    def guessNumber(self, n: int) -> int:
        l, h = 0, n
        while l < h:
            mid = (l + h) // 2
            if guess(mid) == 1: l = mid + 1
            else: h = mid
        return l
