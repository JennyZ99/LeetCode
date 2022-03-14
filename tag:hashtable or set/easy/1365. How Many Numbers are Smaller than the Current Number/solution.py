"""
time: O(nlogn) where n is the size of nums, and because we use sort. 
space: O(n)

data structure: dictionary, list

** we update the number of smaller numbers only if the current number is different from the former one in the sorted list
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_ = list(nums)
        nums_.sort()
        dic={}
        for i in range(0, len(nums_)):
            if i==0: 
                dic[nums_[i]] = i
            elif nums_[i]!=nums_[i-1]:
                dic[nums_[i]] = i
        smallers = []
        for number in nums:
            smallers.append(dic[number])
        return smallers
