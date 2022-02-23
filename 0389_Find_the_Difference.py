"""
Даны две строки. Нужно вернуть единсвенный символ, который в них отличается
s = "abcd"
t = "abcde"   => результат - e
"""
class Solution:
    """
    Интересное решение, основанное на свойствах xor (идемпотентность, коммутативность и самообратимость)
    Для двух одинаковых строк операция xor даст 0, в свою очередь: 
    0 XOR уникальное число =  это число
    """
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for letter in s + t: res^=ord(letter)
        return chr(res)
      
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Вариант с линейной памятью и без collectons.Counter()
        """
        first_str, sec_str = [0]*26, [0]*26
        for l in s:
            first_str[ord(l)-ord('a')] += 1
        for l in t:
            sec_str[ord(l)-ord('a')] += 1
        for i, (f, s) in enumerate(zip(first_str, sec_str)):
            if f != s:
                return chr(ord('a')+i)
