"""
By observing, I can see that if I sort the nums and make pairs by the sorted order, I can get the maximum sum of min(a_i, b_i).
ex. 1,2,3,4,5,6 -> pair -> (1,2), (3,4), (5,6) -> min and sum -> 1+3+5 should be the maximum sum,
and any other pairings, ex. (1,6),(2,5),(3,4) will not end with the maximum sum. 


built-in function: sort() in list

data structure: list

time complexity: O(n*logn) because of sorting algorithm
space: O(1)
"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        max_sum = 0
        for i in range(0, size, 2):
            max_sum += nums[i]
        return max_sum
