"""
time and space: O(n)

data structure: dictionary 

what I need for this problem are:
          Degree/ max-frequency 
                -- frequency of each number: I use the built-in python function - Counter() - to build a dictionary (number - frequency pair)
                -- max_frequency: a variable for storing the max-frequency
                -- an elements array: storing the elements that have the max-freqeuncy 
                
          min- and max-index of the number with max-frequency
                -- with the help of frequency dictionary, I use one other dictionary to store the minimum 
                   length of subarray for each number: number - (max_index - min_index + 1) pair
                -- for loop the dictionary to find the shortest length of subarray. 

"""

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree, elements, dic = self.findDegree(nums)
        dic_min_length = {}
        min_length = 5*(10**4)
        for i,val in enumerate(nums):
            if val in elements:
                if dic[val]==degree:
                    dic_min_length[val] = i
                dic[val] = dic[val]-1
                if dic[val] == 0:
                    dic_min_length[val] = i-dic_min_length[val]+1
        
        for key, val in dic_min_length.items():
            min_length = min(min_length, val)
        return min_length
        
        
    def findDegree(self, nums: List[int]):
        dic = Counter(nums)
        max_freq = 0
        elements = []
        for k in dic:
            max_freq = max(max_freq, dic[k])
        for k in dic:
            if dic[k] == max_freq: 
                elements.append(k)
        return max_freq, elements, dic
