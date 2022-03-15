"""
I need to record and update indexes of two equal characters so that I can calculate the length of substring through (index2-index1-1).

So I use the following data structures: dictionary, list

time: O(n) where n is the length of the string
space: O(n)
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = {}
        max_l = -1
        for i, val in enumerate(s):
            if val not in dic:
                dic[val] = [i, i]
            else:
                l = dic[val]
                l[1] = i
                dic[val] = l
        for val in dic.values():
            max_l = max(max_l, val[1]-val[0]-1)
        return max_l
