"""
data structure: set, list

built-in python function: union() in set

time: O(n*m*r) where n, m and r are the sizes of nums1, nums2 and num3 resbectively.
space: O(n+m+r)

"""
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        at_least_two = []
        joinSet = set()
        js = joinSet.union(set1).union(set2).union(set3)
        for number in js:
            if (number in set1 and number in set2) or (number in set2 and number in set3) or (number in set1 and number in set3):
                at_least_two.append(number)
        return at_least_two
