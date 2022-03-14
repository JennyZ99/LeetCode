"""
time: O(n*m) where n is the number n, and m is the avg number of digits of each number
space: O(n)

data structure: dictionary 
"""

class Solution:
    def countLargestGroup(self, n: int) -> int:
        max_l = 0
        count = 0
        dic = {}
        for i in range(1, n+1):
            s = self.getDigitSum(i)
            if s in dic:
                dic[s] = dic[s]+1
                max_l=max(max_l, dic[s])
            else:
                dic[s] = 1
                max_l=max(max_l, 1)
        
        for val in dic.values():
            if val == max_l:
                count += 1
        
        return count
    
    def getDigitSum(self, n: int) -> int:
        digit_sum = 0
        while not int(n/10)==0:
            digit_sum = digit_sum + n%10
            n = int(n/10)
        digit_sum = digit_sum + n%10
        return digit_sum
