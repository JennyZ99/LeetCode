"""
data structure: dictionary 
                -- I use the existing python funciton Counter

time: O(n) where n is the number of numbers is arr
space: O(n)

** the hardest part of this problem is to consider the case where there exists 0 in the array because 2*0 = 0
"""


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = Counter(arr)
        for m in arr:
            if 2*m in dic.keys():
                if m == 0 and dic[m]<2: continue
                return True      
        return False
