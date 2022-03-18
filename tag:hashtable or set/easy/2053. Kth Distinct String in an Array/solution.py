"""
What I need for this problem are:
                    -- frequency of each string in arr;
                Hence, I use
                                -- a dictionary to record the frequency of each string: string -> freq
                    -- only keep strings with a frequency that is EXACTLY 1;
                Hence, I use 
                                -- a new list to maintain such a list 
                    -- return the kth string in the above list 
                    
Time: O(n) where n is the size of arr
Space: O(n) 

Data Structure: list, dictionary 
"""

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = Counter(arr)
        kth = ""
        newArr=[]
        for char in arr:
            if dic[char]==1:
                newArr.append(char)
        if k>=0 and k<=len(newArr):
            return newArr[k-1]
        else:
            return kth
