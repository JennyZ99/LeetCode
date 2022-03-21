"""
For this problem, I use two pointers for two sorted list. Every time, I assign the smallest cookie to the kid who asks 
the smallest cookie and make sure that the size of the cookie is at least the size that the kid asks. 

built-in python function: sort() in list

data structure: list

time efficienty: O(n), where n is the sum of the length of g and s
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        p_g = 0
        p_s = 0
        num_kid = len(g)
        num_cookie = len(s)
        cnt = 0
        while p_g<num_kid and p_s<num_cookie:
            if s[p_s] >= g[p_g]:
                cnt+=1
                p_g+=1
                p_s+=1
            else:
                p_s+=1
        return cnt
