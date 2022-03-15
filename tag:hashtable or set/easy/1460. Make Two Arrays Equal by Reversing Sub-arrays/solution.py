"""
If two array can be equal after reversing sub-arrays, they must contain the same number of each letter. 

data structure: dictionary

time: O(n) where n is the size of arr
space: O(m) where m is the size of target

"""

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dic = Counter(target)
        for number in arr:
            if number not in dic:
                return False
            else:
                dic[number] = dic[number]-1
                if(dic[number]==0): dic.pop(number)
        return True
