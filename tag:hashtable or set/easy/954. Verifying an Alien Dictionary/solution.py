"""
space: O(1)  -  I use a dictionary with constant space 
time: O(n*m), where n is the number of words, and m is the avg length of each word

data structure: dictionary

This problem is very straightforward. 

What I need for this problem are:
          -- index/position of each letter in the new alien language
                  -- a dictionary with letter -> index pair, where index is from 0 to 25. 
          -- for each two words, I compare the index of each letter to check if it is in a lexigraphical order
                  -- a funcion return boolean var
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic_order = self.getNewDic(order)
        for i in range(1, len(words)):
            if not self.is_lexi(words[i-1], words[i], dic_order): return False
        return True
        
    def getNewDic(self, order: str) -> dict:
        dic = {}
        for i, letter in enumerate(order):
            dic[letter] = i
        return dic
    
    def is_lexi(self, s1: str, s2:str, dic_order: dict) -> bool:
        size1 = len(s1)
        size2 = len(s2)
        it = size1 if size1<=size2 else size2
        for i in range(0, it):
            if dic_order[s1[i]] < dic_order[s2[i]]: return True
            elif dic_order[s1[i]] > dic_order[s2[i]]: return False
        if size1 <= size2: 
            return True
        else:
            return False
