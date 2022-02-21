class Solution:
    """
    Дан массив анаграм. Задача - сгрупировать их.
    
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Интуитивное решение через хеш-таблицу. ?? Сложность O(n * m * log(m)) ??
        """
        res = defaultdict(list)
        for s in strs:   # Сложность O(n)
            res[tuple(sorted(s))].append(s) # Сложность сортировки O(m*log(m)), где m - длинна слова.
        return res.values()
      
    def groupAnagrams(self, strs):
        """
        Интересный вариант с O(om) временем и памятью. 
        Согласно условию задачи в словах могут быть только маленькие латинские буквы.
        Заведём в качестве ключа массив из 26 нулей интерпретируемых как счётчики букв:
        "aaaasdx"  ->   [4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
        """
        hmap = defaultdict(list)
        for st in strs:
            array = [0] * 26
            for l in st:
                array[ord(l) - ord('a')] += 1
            hmap[tuple(array)].append(st)
        return hmap.values()
