"""
time and space complexity is the same as solution1.

data structure: a set

"""



class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        size = len(nums)
        errorNums = []
        myset = set()
        for i, val in enumerate(nums):
            if val not in myset:
                myset.add(val)
            else:
                errorNums.append(val)
        for i in range(1, size+1):
            if i not in myset:
                errorNums.append(i)
        return errorNums
