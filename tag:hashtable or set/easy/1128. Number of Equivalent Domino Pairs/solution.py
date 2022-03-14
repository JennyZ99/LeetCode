"""
time: O(n) where n is the total number dominos is the donimos
space: O(n)

data structure: 
        -- dictionary
        -- tuple
        
** note that the set is unhashable, we need use some data structure that is immutable and hashable for multiple values.
"""

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = {}
        for pair in dominoes:
            a = pair[0]
            b = pair[1]
            if (a,b) in dic:
                dic[(a,b)] = dic[(a,b)]+1
            elif (b,a) in dic:
                dic[(b,a)] = dic[(b,a)]+1
            else:
                dic[(a,b)] = 1
        
        num = 0
        for val in dic.values():
            num = num + int(val*(val-1)/2)
        return num
