"""
n: length of the list - nums
time complexity: O(n)
space compexity: O(n)

what I need for this problem:                                                                         Data Structure:
        flag the appeared number with 1 and non-appeared number with 0 in an array or a list              a new list in case of python
        
my workflow:
        a. initialize a new zero-array with the same length/size as the input nums
        b. see the number-1 as index of the new array, and set the numbers in thses indexes to 1
        c. check the new array:
                - if the number is 0, index+1 should be append to the result list
                - if the number is 1, do nothing. because 1 means that the number in the (1,size) range exists. 
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)
        mylist = [0]*size
        disappeared = []
        for val in nums:
            mylist[val-1] = 1
        for i, val in enumerate(mylist):
            if val == 0:
                disappeared.append(i+1)
        return disappeared
