"""
time: O(m+n) where m is the number of boxes of Alice and n is the number of boxes that Bob has.
space: O(n)

data structure: set

**note: I use some mathematics for this problem, because after swapping, the following function should be satisfied:
        total_number_of_candies_Alice - number_of_candies_in_this_box_Alice + number_of_candies_in_that_box_Bob = avg, where avg is 1/2*(total_number_of_candies)
        
"""

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        avg = 0
        bob = set()
        alice_t = 0
        bob_t = 0
        for val in aliceSizes:
            alice_t = alice_t+val
        for val in bobSizes:
            bob_t = bob_t+val
            bob.add(val)
        avg = int((alice_t+bob_t)/2)
        
        for val in aliceSizes:
            if avg+val-alice_t in bob:
                return [val, avg+val-alice_t]
