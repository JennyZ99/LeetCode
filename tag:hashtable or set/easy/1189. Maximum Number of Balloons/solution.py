"""
This problem is straightforward. 

data structure: dictionary

time: O(n) where n is the number of chars in text
space: O(n)
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {}
        for char in text:
            if char in dic:
                dic[char] = dic[char] + 1
            else:
                dic[char] = 1
        s = "balloon"
        n=0
        while True:
            for char in s:
                if char in dic:
                    dic[char] = dic[char] - 1
                    if dic[char]<0: return n
                else:
                    return n
            n +=1
        return n
