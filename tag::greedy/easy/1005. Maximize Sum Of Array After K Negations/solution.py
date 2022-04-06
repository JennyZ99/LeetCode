"""
Time: O(knlgn), where n is the size of nums. 
Space: O(1)

"""

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        sm = 0
        for i in range(0, k):
            nums.sort()
            nums[0] = - nums[0]
        for i, n in enumerate(nums):
            sm+=n
        return sm
