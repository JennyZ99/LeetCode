"""
Time: O(nlogn) because I use sort function 
Space: O(n) because I maintain another list with length n, where n is the length/size of nums

**note: 
            -- an original array/list is used for maintainting the order of the output. 
            -- a new list is used for finding the max-subsequence with length k.


"""

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_ = list(nums)
        nums_.sort()
        max_subseq_ = []
        max_subseq = []
        for i in range(len(nums_)-k, len(nums_)):
            max_subseq_.append(nums_[i])
        for num in nums:
            if num in max_subseq_:
                max_subseq.append(num)
                max_subseq_.remove(num)
        return max_subseq
