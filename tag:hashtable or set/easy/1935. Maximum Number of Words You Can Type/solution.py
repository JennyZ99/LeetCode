"""
data structure: set

time complexity: O(n*m), where n is the number of words, and m is the avg length of the words. 

The solution of this problem is straightforward. 
          -- add broken letters to a set
          -- check each letter of a word to see whether there is letter in the broken set
"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cnt = 0
        brokenSet = set(brokenLetters)
        for word in re.split(' ', text):
            if self.can_type(word, brokenSet):
                cnt+=1
        return cnt
    
    def can_type(self, word: str, brokenSet: set) -> bool:
        for char in set(word):
            if char in brokenSet:
                return False
        return True
