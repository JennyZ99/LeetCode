"""
m: length of s
n: length of t
time: O(m+n)
space: O(m)

data structure: set

the letter that is not in the set is the 'difference' -- added letter
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        myset=set()
        for val in s:
            myset.add(val)
        for val in t:
            if val not in myset:
                return val
        return ''
