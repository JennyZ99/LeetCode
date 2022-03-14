"""
time and space: O(n)

data structure: dictionary 

"""
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = Counter(arr)
        largest = -1
        for key,value in dic.items():
            if key==value:
                largest = max(largest, key)
        return largest
