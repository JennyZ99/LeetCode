"""
**faster, because we only sort the non-duplicated set/list of numbers

data structure: set

"""

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(set(arr))
        dic = {}
        rank = []
        r = 1
        for i in range(1, len(a)+1):
            dic[a[i-1]] = i
        for n in arr:
            rank.append(dic[n])
        return rank
