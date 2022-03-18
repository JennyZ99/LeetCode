"""
my solution: count the frequency and check if the frequencies are the same using a set. 
"""

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        mylist = list(s)
        dic = Counter(mylist)
        if len(set(dic.values()))==1: return True
        return False
