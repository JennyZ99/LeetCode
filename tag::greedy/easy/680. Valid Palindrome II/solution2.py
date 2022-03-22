"""
This solution is the same as solution1, only I don't get the substring of s - s[i:j]
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        cnt_deleted = 0
        return self.helper(s, 0, len(s)-1, cnt_deleted)
    
    def helper(self, s:str, p1:int, p2:int, cnt_deleted: int) -> bool:
        if cnt_deleted>1: return False
        if p1==p2: return True
        if p1<p2:
            if s[p1]==s[p2]:
                if p1+1==p2:
                    return True
                else:
                    return self.helper(s, p1+1, p2-1, cnt_deleted)
            else:
                return self.helper(s, p1+1, p2, cnt_deleted+1) or self.helper(s, p1, p2-1, cnt_deleted+1) 
