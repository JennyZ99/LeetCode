"""
time, space: O(n)
What I need for this problem:                           Data Structure:
          - all the indexes of the unique letter.             - a dictionary: record index of the unique letter, and as -1 for the non-unique letter
          - the smallest index of the unique letter           - loop the dictionary to find the smallest index. 
**note: (considerations)
     -1: 
            -1 should not be considered when doing comparison for smallest index
     all the letters have duplications or are non-unique: 
            the smallest index will be the initialized value, which in my case is 10**5-1, and we need to return -1 
     instead of the initialized value.  
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        min_index = 10**5-1
        for i, val in enumerate(s):
            if val not in dic:
                dic[val] = i
            else:
                dic[val] = -1
        
        for key in dic:
            index = dic[key]
            if index==-1: continue
            min_index = min(min_index, dic[key])
        if min_index == 10**5-1: return -1
        return min_index
