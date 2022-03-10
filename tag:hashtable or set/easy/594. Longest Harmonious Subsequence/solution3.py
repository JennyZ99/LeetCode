"""
refer to the solution of Taha Choura(https://leetcode.com/Taha-C/) on LeetCode.

Used a build-in python function to create a dictionary for finding the length of longest harmonious seqeunce.

Time and Space: O(n)

"""


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        longest = 0
        dic = Counter(nums)
        for key in dic:
            if key+1 in dic:
                longest = max(dic[key]+dic[key+1],longest)
        return longest
