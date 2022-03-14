"""
time: O(n*m), where n is the number of words, and m is avg length of each word
space: O(p), where p is the number of chars in chars

data structure: dictionary

**note: I create a new dictionary to record the frequency change.
"""

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = {}
        for c in chars:
            if c in dic:
                dic[c] = dic[c]+1
            else:
                dic[c] = 1
        
        output = 0
        for word in words:
            dic_t = dict(dic)
            if self.can_form(word, dic_t):
                output = output + len(word)
        return output
    
    def can_form(self, word:str, dic: dict) -> bool:
        for c in word:
            if c not in dic:
                return False
            else:
                dic[c] = dic[c]-1
                if dic[c]<0: return False
        return True
