"""
By observing, there are a few cases that I can place a flower:
        -- if I am at the index 0 and if this lot is empty and its next lot is also empty; 
                ex. 0 0 1 -> 1 0 1 is valid
        -- if I am at the end of the flowerbed, and if this lot is empty and its previous lot is also empty;
                ex. 1 0 0 -> 1 0 1 is valid
        -- if I am at the middle of the flowerbed, if this lot is empty, and both its next and previous lots are empty: 
                ex. 1 0 0 0 1 - > 1 0 1 0 1 is valid
        -- **note/considerations: remember the corner case when there is only one lot in the flowerbed:
                if the flowerbed is empty - [0] - I can place a flower, otherwise, I cannot 
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        for i in range(0, size):
            if n==0: return True
            if flowerbed[i]==1: continue
            else:
                if (i==0 and i==size-1) or (i==0 and i+1<size and flowerbed[i+1]==0) or (i==size-1 and i-1>=0 and flowerbed[i-1]==0) or (i-1>=0 and i+1<size and flowerbed[i-1] == 0 and flowerbed[i+1]==0):
                    flowerbed[i]=1
                    n-=1
        if n==0: return True
        return False
