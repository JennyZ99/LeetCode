"""
time and space complexity: O(n)

data structure: set 
        -- the number that is alreay in set is the duplicated number. 

** I also use some mathematics: 1+2+3+...+n = (1+n)*n/2
        the total sum - the sum without duplicated number = the loss number 

"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        size = len(nums)
        errorNums = []
        myset = set()
        my_sum = 0
        for i, val in enumerate(nums):
            if val not in myset:
                myset.add(val)
                my_sum += val
            else:
                errorNums.append(val)
        loss = int((1+size)*size/2)-my_sum
        errorNums.append(loss)
        return errorNums
