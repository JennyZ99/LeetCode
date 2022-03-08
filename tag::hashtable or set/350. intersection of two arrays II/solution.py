"""

pros: 
this solution is short and easy to understand;
space: O(1)

cons: 
time complexity: O(m*n) in the worst case;

**note: m is the size of nums1, and n is the size of nums2

"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        for val in nums1:
            if val in nums2:
                intersect.append(val)
        return intersect
