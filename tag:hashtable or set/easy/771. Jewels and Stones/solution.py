"""
Data structure: set 
      -- for storing the types of jewels

I need:
      -- a counter variable, num_j, to count the jewels I have;
      -- loop the stones, and check whether a stone is jewel, and if Yes, num_j + 1
      
space: O(n), where n = number of types of jewels;
time: O(m), where m is the length of string - stones or the number of stones. 
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_type = set()
        num_j = 0
        for val in jewels:
            jewels_type.add(val)
        
        for val in stones:
            if val in jewels_type:
                num_j += 1
        return num_j
