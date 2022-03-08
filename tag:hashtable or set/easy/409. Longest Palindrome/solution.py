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

"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        longest = 0
        odd = False
        for val in s:
            if val not in dic:
                dic[val]=1
            else:
                dic[val]=dic[val]+1
        for key in dic:
            this_val = dic[key]
            if this_val%2==0:
                longest += this_val
            else:
                longest += (this_val-1)
                odd = True
        if odd: return longest+1
        return longest
