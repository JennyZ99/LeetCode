"""
This problem is relatively straightforward.

time: O(n**2), where n is the number of numbers in nums
"""

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        final = original
        while original in nums:
            final = original*2
            original = final
        return final
