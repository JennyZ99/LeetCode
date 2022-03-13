"""
time: O(n) where n is the number of trust relationship in trust list
space: O(n)

data structure: dictionary 

I use two dictionaries:
        -- one for store the number of people who believe a person: person -> # of believers 
        -- one for store the trust relationship 
       
The town judge must be a person who has n-1 believers and do not trust anybody. 
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0 and n==1: return 1
        dic_trust_by, dic_trust = self.buildDics(trust)
        for key, val in dic_trust_by.items():
            if val==(n-1) and key not in dic_trust:
                return key
        return -1
        
    def buildDics(self, trust: List[List[int]]):
        dic_trust_by = {}
        dic_trust = {}
        for pair in trust:
            dic_trust[pair[0]] = pair[1]
            if pair[1] in dic_trust_by:
                dic_trust_by[pair[1]] = dic_trust_by[pair[1]]+1
            else:
                dic_trust_by[pair[1]] = 1
        return dic_trust_by, dic_trust
