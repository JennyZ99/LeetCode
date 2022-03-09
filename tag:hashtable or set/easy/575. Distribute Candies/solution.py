"""
space: O(n)
time: O(n)
data structure: 
        a hashset to record the type of candies;
        a var to store the number of candies the patient can eat;
        
the most type of candies the person can eat should be min(the number of types, the number of candies the person can eat)

"""


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        n = int(n/2)
        type_set = set()
        for val in candyType:
            type_set.add(val)
        return min(len(type_set), n)
