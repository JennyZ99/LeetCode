"""
If the path will cross, it means that the updated cordinate was seen before. 
So what I should do is to check if the updated cordninate was seen before, and 
just use a set, I can do it. 

Data structure: tuple, set

time complexity: O(n), where n is the length of path
space: O(n)


"""

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        myset = set()
        x = 0
        y = 0
        myset.add((x,y))
        for c in re.split('', path):
            if c=='N':
                y += 1
            elif c=='S':
                y -= 1
            elif c=='E':
                x += 1
            elif c=='W':
                x -= 1
            else:
                continue
            if (x,y) in myset:
                return True
            myset.add((x, y))
        return False
