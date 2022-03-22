"""
I define a list for this problem. I define the index as (dollar-amount/5-1) to shorten the array used for counting the bills.

time: O(n)
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        arr = [0]*4
        for bill in bills:
            index = int(bill/5)-1
            arr[index] +=1
            if bill == 10:
                if arr[0]>=1: arr[0]-=1
                else: return False
            elif bill == 20:
                if arr[1]>=1 and arr[0]>=1:
                    arr[1]-=1
                    arr[0]-=1
                elif arr[0]>=3:
                    arr[0]-=3
                else:
                    return False
        return True
