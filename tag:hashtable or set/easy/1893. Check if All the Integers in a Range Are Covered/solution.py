"""
This problem requires me to know how to create a valid set for checking if all the integers in a range are covered

data structure: set

time complexity: O(max(right-left+1, range_sum in ranges))
space complexity: O(range_sum in ranges)
"""

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        myset = set()
        for ran in ranges:
            for i in range(ran[0], ran[1]+1):
                myset.add(i)
        for i in range(left, right+1):
            if i not in myset:
                return False
        return True
