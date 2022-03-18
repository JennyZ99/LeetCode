"""
data structure: dictionary

What I need for this problem are 
                      -- permutation in mathematics: number of pairs = freq of one number * freq of the other number
                      
**note: because I count twice of the pairs, so I return cnt/2

time: O(n) where n is the size of nums
space: O(n)
"""

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        dic = Counter(nums)
        for key, val in dic.items():
            if key+k in dic:
                cnt += (dic[key+k]*val)
            if key-k in dic:
                cnt += (dic[key-k]*val)
        return int(cnt/2)
