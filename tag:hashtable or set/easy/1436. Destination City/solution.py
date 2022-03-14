"""
data structure: dictionary 
time and space: O(n) where n is the size of paths

"""

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = {}
        for path in paths:
            dic[path[0]] = path[1]
        
        for path in paths:
            if path[1] not in dic:
                return path[1]
