"""
time: O(n), where n is the number of number in nums
space: O(n)

data structure: dictionary 
"""

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        size = len(nums)
        n = int(size/2)
        dic = {}
        for val in nums:
            if val in dic:
                dic[val] = dic[val]+1
                if dic[val] == n: return val
            else:
                dic[val] = 1
        
        return 0
