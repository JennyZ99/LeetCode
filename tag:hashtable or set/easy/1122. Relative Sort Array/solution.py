"""
data structure: dictionary and list/array

time: O(n) where n is the size of arr1
space: O(n)
"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic1 = Counter(arr1)
        sorted_array = []
        for n in arr2:
            times=dic1[n]
            for i in range(0, times):
                sorted_array.append(n)
                arr1.remove(n)                
        arr1.sort()
        return sorted_array+arr1
