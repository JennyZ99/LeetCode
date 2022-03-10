"""
m: length of list1
n: length of list2
time complexity: O(m+n)
space: O(m)

This solution of mine is time and space efficient. 

data structure: dictionary 
                -- dictionary 1: restaurant - index pair
                -- dicitonary 2: common restaurant - index-sum pair
                
** I also use a variable to record the minimum index-sum, which plays a role in filtering the output. 
        
"""


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        dic_common = {}
        common_interest = []
        min_sum = 2000
        for i, val in enumerate(list1):
            if val not in dic:
                dic[val] = i
        
        for i, val in enumerate(list2):
            if val not in dic:
                continue
            else:
                index_sum=dic[val]+i
                dic_common[val] = index_sum
                min_sum = min(min_sum, index_sum)
                
        for key,val in dic_common.items():
            if val == min_sum:
                common_interest.append(key)
        
        return common_interest
