"""
I use python built-in function - Counter to build a dictionary

** note: to calculate the number of pairs, I should use the mathematic technique - combination: C(n,2) = n*(n-1)/(2*1)

time: O(n) where n is the size of nums / number of numbers in num

"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = Counter(nums)
        num_gp = 0
        for val in dic.values():
            num_gp += int(val*(val-1)/2)
        return num_gp
