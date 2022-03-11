"""

time: O(n*m), where n is the number of words and m is the average length
space: O(n*m), as for every word I create a dictionary, and each dictionary use O(m) space

data structure: dictionary

"""


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dic_lp = {}
        lp = licensePlate.lower()
        min_len = 1000
        shortest_comp_word = ''
        for val in lp:
            if not val.isalpha():
                continue
            else:
                if val in dic_lp:
                    dic_lp[val] = dic_lp[val]+1
                else:
                    dic_lp[val] = 1
                    
        for word in words:
            is_complete = self.is_completing(word, dic_lp)
            if is_complete: 
                shortest_comp_word = word if len(word)<min_len else shortest_comp_word
                min_len = min(min_len, len(word))
                
        return shortest_comp_word
    
    def is_completing(self, word: str, dic_lp: dict) -> bool:
        dic_this = {}
        for val in word:
            if val not in dic_this:
                dic_this[val]=1
            else:
                dic_this[val]=dic_this[val]+1
        
        for key,val in dic_lp.items():
            if key not in dic_this: return False
            elif val < dic_this[key]: return False
        return True
