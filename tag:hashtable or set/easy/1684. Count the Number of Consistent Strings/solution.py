"""
I use python built-in function to convert string to char set.

I also define a boolean variable - is_consis - to indicate whether a word is consistent. 

data structure: set

time: O(n*m), where n is the number of words, and m is the avg length of each word
space: O(n*m)
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        all_set = set(allowed)
        count = 0
        for word in words:
            w_set = set(word)
            is_consis = True
            for char in w_set:
                if char not in all_set:
                    is_consis = False
                    break
            if is_consis:
                count+=1
        return count
