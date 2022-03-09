"""
this solution is more compact. 

space: O(n)
time: O(n)

what I need for this problem:                                               data structure: 
  -- frequency of each number                                                 - a dictionary 
  -- sum of the frequency of two numbers that have difference as 1            - a var

"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for val in nums:
            if val in dic:
                dic[val] = dic[val]+1
            else:
                dic[val] = 1
        longest = 0
        for k in dic:
            if k+1 in dic:
                longest = max(dic[k]+dic[k+1], longest)
        return longest
