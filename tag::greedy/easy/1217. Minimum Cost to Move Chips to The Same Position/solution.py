"""
I refer to the idea of official solution on leetcode:
  - move all chips on an odd-indexed position to 1 with 0 cost;
  - move all chips on an even-indexed position to 2 with 0 cost;
  - finally, move from the position with less chips to the position with more chips; 
  

Space: O(1)
Time: O(n)
"""

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        position_1 = 0
        position_2 = 0
        for i, num in enumerate(position):
            if num%2==1:
                position_1 += 1
            else:
                position_2 += 1
        return min(position_1, position_2)
