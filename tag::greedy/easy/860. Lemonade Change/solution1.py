"""
I use a dicitonary to count the bills and update the changes. 

Pros: space efficient

Cons: runtime O(n), but slow
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {}
        for bill in bills:
            if bill in dic:
                dic[bill] = dic[bill]+1
            else:
                dic[bill] = 1
            if bill == 10:
                if 5 in dic and dic[5]>=1:
                    dic[5] = dic[5]-1
                else: 
                    return False
            elif bill == 20:
                if 10 in dic and dic[10]>=1 and 5 in dic and dic[5]>=1:
                    dic[10] = dic[10]-1
                    dic[5] = dic[5]-1
                elif 5 in dic and dic[5]>=3:
                    dic[5] = dic[5]-3
                else:
                    return False
        return True
