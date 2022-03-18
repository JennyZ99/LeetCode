"""
data structure: dictionary, set

What I need for this problem are 
                      -- check whether on a rod, there are rings with ALL three colors;
                      -- count the number of the rods that qualify the above conditions;
                Hence, I use
                      -- a dictionary: rod number -> color set
                Finally, I use
                      -- a for loop to check whether the size of the set is three. 
                      
Time: O(n), where n is the length of rings. 
Space: O(1), because there are only 10 rods (10 keys in the dictionary), and each set has size at most three. 

"""

class Solution:
    def countPoints(self, rings: str) -> int:
        cnt = 0
        dic = {}
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i+1]
            if rod not in dic:
                dic[rod] = set(color)
            else:
                temp_set = dic[rod]
                temp_set.add(color)
                dic[rod] = temp_set
                
        for val in dic.values():
            if len(val)==3:
                cnt+=1
        return cnt
