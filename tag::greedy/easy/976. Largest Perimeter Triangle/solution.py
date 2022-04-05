"""
As I use sort algorithm ... 

Time complexity: O(nlgn), where n is the number of numbers in list;
Space: O(1)
"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        max_peri = 0
        for i in reversed(range(2, size)):
            if nums[i] < nums[i-1]+nums[i-2]:
                max_peri = max(max_peri, nums[i-2]+nums[i-1]+nums[i])
        return max_peri
