"""
my solution: 
size of ransomNote:  m
size of magazine: n
space: O(n)
time: O(m+n)
workflow: 
    what I need are:                                                    data structure:
        - frequency of each letter in magazine;                       - a dictionary 
        - make sure the frequency of each letter in ransomNote        - a loop to update the dictionary: 
          is within the range of that in magazine;                             a. if the letter is not in the dic, return False
                                                                               b. if the frequency is -1 or <0, return False
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for val in magazine:
            if val not in dic:
                dic[val] = 1
            else:
                dic[val] = dic[val]+1
        for val in ransomNote:
            if val not in dic:
                return False
            else:
                dic[val] = dic[val]-1    
                if(dic[val]<0): return False
        return True
