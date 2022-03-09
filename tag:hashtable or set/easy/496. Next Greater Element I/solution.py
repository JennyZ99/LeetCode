"""
I refer other people's solution to use a stack to solve this problem. 

time complexity: O(n)
space O(n)

What I need for this problem:                                                     Data Structure:
          - a stack to store the numbers that are in decreasing order;                    - a stack
          - pop all the numbers that are smaller than a newly seen number;                - a dictionary: number-the newly seen greater number
          - those left in the stack have no next greater number                                           remained number - -1
          - creat the output by checking the built dictionary 
          
** note: as I need pop all the numbers that are smaller than a newly seen number, I use a while loop.

"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        next_great = []
        for val in nums2:
            stack_size = len(stack)
            if stack_size==0: stack.append(val)
            else:
                while stack_size>0 and val>stack[stack_size-1]:
                    dic[stack[stack_size-1]] = val
                    stack.pop(stack_size-1)
                    stack_size = len(stack)
                stack.append(val)
        
        for i in range(0, len(stack)):
            dic[stack.pop(0)]=-1
        
        for val in nums1:
            next_great.append(dic[val])
        return next_great
