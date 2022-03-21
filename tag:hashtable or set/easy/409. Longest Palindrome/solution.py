"""
time complexity: O(n)
space: O(n)

What I need for this problem:                         Data Structure:
        - frequency of each letter                            - a dictionary: letter-frequency pair

* observation: 
    a. each pair of letters can be added to the head and tail of a string to form a palindrome 
    b. one letter can be added to the middle of the string to form a palindrome

workflow:
  I define a flag variable - odd - to record whether there exists a letter with odd frequency. 
        - If Yes, ths length of longest palindrome should be added by 1
        - If No, do nothing 
  I define the output variable - longest - to record the number of 'pair-wisable' letters.
  
In summary, this problem asks that me to build the longest palindrome with a set of letters. 

data structure: dictionary

Once the number of letters are even, the letters can form a palindrome. ex. "aabb" -> "abba"
However, I also should consider the case when there exists odd number letter. ex. "aabbb" -> "abbba"
                    Hence, I use
                            -- a dictionary: char -> frequency pair
                            
                    ,and I calculate the longest length with the frequency 
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        longest = 0
        odd = False
        for char in s:
            if char not in dic:
                dic[char]=1
            else:
                dic[char]=dic[char]+1
        for char in dic:
            freq = dic[char]
            if freq%2==0:
                longest += freq
            else:
                longest += (freq-1)
                odd = True
        if odd: return longest+1
        return longest
