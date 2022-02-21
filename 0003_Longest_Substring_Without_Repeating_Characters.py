class Solution:
    """
    Необходимо вернуть длинну самой длинной непрерывной подстроки не содержащей повторяющихся символов
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = "" 
        ans = 0
        for l in s:
            if l not in window: # если символа нет в в текущем результате, добавим его
                window += l
                ans = max(ans, len(window)) # длинна равна либо длинне текущей подстоки, либо наибольшей из найденной
            else:
                window = window[window.index(l)+1:] + l # Если символ есть в подстроке, обрезаем подстроку до следующего элемента после данного и добавляем новый
                # window == "abcd" ; l == "b"   =>   window = "cd" + "b" 
        return ans
