"""
this is a solution that is not suggested:

I first merge sort the list, and loop the sorted array to count the frequency of each number, 
and only add up the frequency for numbers with difference as 1

time: O(n) but slower than other solutions
space: O(n)
"""

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        size = len(nums)
        self.merge_sort(nums, 0, size-1)
        freq1=0
        freq2=0
        temp = 0
        longest = 0
        for i,val in enumerate(nums):
            if(i==0): 
                freq1=1
                val_ = val
            else:
                if(val==val_): freq1+=1
                elif abs(val-val_)==1:
                    if temp == 0:
                        temp = freq1
                    else:
                        temp = temp+freq1
                        longest = max(longest,  temp)
                        temp = freq1
                    freq1 = 1
                    val_ = val
                else:
                    if(temp!=0):
                        temp = temp+freq1
                        longest = max(longest,  temp)
                    temp = 0
                    val_ = val
                    freq1 = 1
        if(temp!=0):
            temp = temp+freq1
            longest = max(longest,  temp)
        return longest
    
    def merge_sort(self, nums: List[int], p: int, r: int) -> None:
        if p<r:
            q = int((p+r)/2)
            self.merge_sort(nums, p, q)
            self.merge_sort(nums, q+1, r)
            self.merge(nums, p, q, r)
            #print(nums)
        #return nums
     
    def merge(self, nums: List[int], p:int, q:int, r:int) -> None:
        n1 = q-p+1
        n2 = r-(q+1)+1
        left = [0]*(n1+1)
        right = [0]*(n2+1)
        for i in range(0, n1):
            left[i] = nums[p+i]
        for i in range(0, n2):
            right[i] = nums[q+1+i]
        left[n1] = 10**9+1
        right[n2] = 10**9+1
        i = 0
        j = 0
        for k in range(p,r+1):
            if left[i]<=right[j]:
                nums[k]=left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
        
