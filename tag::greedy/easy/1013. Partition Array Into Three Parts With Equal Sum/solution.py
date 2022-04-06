"""
time: O(n)
space: O(1)
I utilize mathematical calculations. Specifically, I consider the corner case [0,0,0,0], and that's why 
p_count > 3.

My idea is as following: 
    - total sum of the numbers in the arr should be divided by 3, otherswise, the arr can not be partitioned in 3 part;
    - as each part of the 3 needs to be continuous, I define a partital sum var - p_sum - to record the sum.
"""

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sm = 0
        for i, num in enumerate(arr):
            sm+=num
        if sm%3!=0: return False
        part = int(sm/3)
        p_sum = 0
        p_count = 0
        for i, num in enumerate(arr):
            p_sum += num
            if (p_sum == part):
                p_sum = 0
                p_count+=1
        return p_count>=3
