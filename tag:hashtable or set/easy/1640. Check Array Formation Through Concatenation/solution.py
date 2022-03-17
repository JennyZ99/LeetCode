"""
By observing, I find that if arr can be formed from pieces, elements in pieces have to 
be next to each other just as they are next to each other in arr. So I can use index 
difference to check if two elements are next to each other. 

Data structure: dictionary 

What I need for this problem are:                                                   Data Structure:
        -- index of each element in arr, because each element is distinct               -- dictionary: number -> index
        -- for elements in each piece, difference of two indexes of near-by elements must be 1 in order that the pieces 
            form the arr
            
time complexity: O(n) where n is the length of arr
space: O(n)
"""

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {}
        for i, val in enumerate(arr):
            dic[val] = i
        for piece in pieces:
            for i, val in enumerate(piece):
                if val not in dic: return False
                if i==0: idx = dic[val]
                else:
                    if dic[val]-idx != 1: return False
                    idx = dic[val]
        return True
