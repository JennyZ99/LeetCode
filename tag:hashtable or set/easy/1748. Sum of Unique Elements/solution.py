"""
This is an easy problem. The only thing I should pay attention to is each number must appear 'exactly once'. 
"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = Counter(nums)
        sm = 0
        for num, freq in dic.items():
            if freq==1:
                sm+=num
        return sm
