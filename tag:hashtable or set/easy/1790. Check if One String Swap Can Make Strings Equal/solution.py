"""
If two strings are 'swappable', there are two and only two positions/index have differences, and the two positions must have same
set of letters. 

data structure: set, dictionary

dictionary: index->letter

time complexity: O(n) where n is size of s1 or s2.
space: O(1)
"""

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2: return True
        size_1 = len(s1)
        size_2 = len(s2)
        if size_1 != size_2: return False
        d1={}
        d2={}
        for i in range(0, size_1):
            if s1[i]!=s2[i]:
                d1[i] = s1[i]
                d2[i] = s2[i]
            if len(d1)>2: return False
        if len(d1)==1: return False
        if set(d1.values())!=set(d2.values()): return False
        return True
