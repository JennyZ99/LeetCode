"""
data structure: dictionary, list

time: O(m+n) where m,n are the length of word1 and word2 respectively;
space: O(1) because there are at most 26 alphabetic letters

What I need for this problem are:
                -- the frequency of each letter in each word - word1 and word2
                -- compare the difference of the frequencies of the same letter in the two words.
             Hence, I use
                -- a dictionary to record the frequency of each letter: letter -> frequency 

"""

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d1 = Counter(list(word1))
        d2 = Counter(list(word2))
        for key,val in d1.items():
            if key in d2:
                if abs(d2[key]-val)>3: return False
            else:
                if val>3: return False
            
        for key, val in d2.items():
            if key not in d1 and val>3:
                return False
        return True
