"""
For this problem, I use two pointers and a self-defined recursion function. 

time complexity: O(n), because call the recursion funcitons about 2n times.


"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        cnt_deleted = 0
        return self.helper(s, cnt_deleted)
    
    def helper(self, s:str, cnt_deleted: int) -> bool:
        i = 0
        j = len(s)-1
        if cnt_deleted>1: return False
        if i==j: return True
        if i<j:
            if s[i]==s[j]:
                if i+1==j:
                    return True
                else:
                    return self.helper(s[i+1:j], cnt_deleted)
            else:
                return self.helper(s[i+1:j+1], cnt_deleted+1) or self.helper(s[i:j], cnt_deleted+1) 
