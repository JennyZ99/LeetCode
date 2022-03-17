"""
data structure: set

built-in python function: 
                    -- set()
                    -- ord() for transforming asii char to int
                    -- chr() for transforming int to asii char/alphabet letter
                    
space: O(1) because we have at most constant letters (26 lower-case letters).
time: O(n) where n is the length of sentence. Because when we create the set, we have to add each letter to the set.
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        myset = set(sentence)
        sett = set()
        for i in range(ord('a'), ord('z')+1):
            sett.add(chr(i))
        return myset==sett
