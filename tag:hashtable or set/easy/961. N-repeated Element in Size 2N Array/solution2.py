"""
This is a more compact solution using existing python function - Counter(). 
"""

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = int(len(nums)/2)
        dic = Counter(nums)
        for key, val in dic.items():
            if val == n: return key        
        return 0
