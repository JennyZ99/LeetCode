"""
What I need for this problem is to update the local name based on two rules, and meanwhile, make other parts of the address stay unchanged. 

time: O(m*n), where n is the number of emails, and m is the average length of local name.
space: O(n)

data structure: set

"""


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueE = set()
        for e in emails:
            local = e.split('@')[0]
            domain = e.split('@')[1]
            local = self.updateLocal(local)
            uniqueE.add(local+'@'+domain)
        return len(uniqueE)
    
    def updateLocal(self, s: str) -> str:
        u = ''
        for val in s:
            if val=='.':
                continue
            elif val == '+':
                return u
            else:
                u = u+val
        return u
