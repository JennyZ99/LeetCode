"""
This problem requires me to use a 'sliding window'. 

time: O(n) where n is the length of s
space: O(n) because we have n-3 set and each set has size at most 3

data structure: set, string
"""

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = 0
        size = len(s)
        if(size<3): return cnt
        for i in range(0, size-2):
            subs = s[i:i+3]
            if len(set(subs)) == len(subs):
                cnt+=1
        return cnt
