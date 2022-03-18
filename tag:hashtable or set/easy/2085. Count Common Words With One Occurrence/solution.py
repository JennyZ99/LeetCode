"""
data structure: dictionary 

time: O(n), where n is the size of words1
space: O(n+m), where m is the size of words2

**note: 
          -- we should focus on counting words appearing EXACTLY ONCE in both list.
"""
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt = 0
        d1 = Counter(words1)
        d2 = Counter(words2)
        for key, val in d1.items():
            if val==1 and (key in d2) and d2[key]==1:
                cnt+=1
        return cnt
