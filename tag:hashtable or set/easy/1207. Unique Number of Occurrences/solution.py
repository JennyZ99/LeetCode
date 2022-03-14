"""
compact solution with python built-in funciton Counter()
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = Counter(arr)
        return len(dic.values())==len(Counter(dic.values()))
