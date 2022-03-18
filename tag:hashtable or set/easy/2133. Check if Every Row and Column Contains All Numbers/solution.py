"""
Data structure: set, list

Time: O(n**2), where n is the dimension of the matrix

This problem is relatively straightforward. Just check each row and each column with a customized set. 
"""

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        if n==1: return True
        myList = [i+1 for i in range(0, n)]
        if not self.are_valid_rows(myList, matrix):
            return False
        if not self.are_valid_cols(n, myList, matrix):
            return False
        return True
    
    def are_valid_rows(self, myList: list,  matrix: List[List[int]]) -> bool:
        for row in matrix:
            if set(row)!=set(myList):
                return False
        return True
    
    def are_valid_cols(self, n:int, myList: list, matrix: List[List[int]]) -> bool:
        for i in range(0, n):
            if set([matrix[j][i] for j in range(0, n)]) !=set(myList):
                return False
        return True
