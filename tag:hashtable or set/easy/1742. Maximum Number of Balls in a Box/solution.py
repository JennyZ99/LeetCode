"""
data structure: dictionary

time: O(m*n) where n is the highLimit-lowLimit+1 and m is the avg number of digits of each number is the range.

"""


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # dic: box number -> count
        dic = {}
        max_count = 0
        for i in range(lowLimit, highLimit+1):
            box_num = self.get_digit_sum(i)
            if box_num not in dic:
                dic[box_num] = 1
                max_count = max(max_count, 1)
            else:
                dic[box_num] = dic[box_num] + 1
                max_count = max(max_count, dic[box_num])
        return max_count
    
    def get_digit_sum(self, n:int) -> int:
        sm = 0
        while int(n/10)>0:
            sm += (n%10)
            n = int(n/10)
        sm += n
        return sm
