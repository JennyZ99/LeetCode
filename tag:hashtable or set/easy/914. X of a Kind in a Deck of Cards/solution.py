"""
get divisors and get common divisors.

space: O(n)
time: O(n)

data structure: dictionary and set

** I like the solution from Taha Choura 
-- https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/discuss/1836524/4-Lines-Python-Solution-oror-50-Faster-oror-Memory-less-than-60
"""

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        frequencies = Counter(deck).values()  
        common_div = set()
        for val in frequencies:
            if val<2: return False
            elif len(common_div)==0:
                common_div = self.getCommDiv(val)
            else:
                this_common_div = self.getCommDiv(val)
                intersect = set()
                for val in this_common_div:
                    if val in common_div:
                        intersect.add(val)
                common_div = intersect
                if len(intersect)==0:
                    return False
        return True
    
    def getCommDiv(self, n: int) -> int:
        common_div = set()
        for i in range(2, n+1):
            if n%i==0:
                common_div.add(i)
        return common_div
