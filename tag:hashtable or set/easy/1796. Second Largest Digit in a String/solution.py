"""
data structure: set

used built-in function: sort() for list

time complexity: O(nlgn) because of the sort funciton

space: O(n) where n is the length of the string s

"""
class Solution:
    def secondHighest(self, s: str) -> int:
        l = []
        sec = -1
        for c in set(s):
            if c.isnumeric():
                l.append(c)
        if(len(l)<=1): return sec
        l.sort()
        return l[len(l)-2]
