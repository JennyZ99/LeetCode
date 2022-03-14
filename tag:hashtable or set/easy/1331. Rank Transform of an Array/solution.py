"""
time: O(n) where n is the size of arr
space: O(n)

data structure:  dictionary, list
"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=list(arr)
        a.sort()
        dic = {}
        rank = []
        r = 1
        for i in range(0, len(a)):
            if i==0: 
                r=1
                dic[a[i]] = r
            else:
                if a[i]==a[i-1]:
                    continue
                else:
                    r+=1
                    dic[a[i]] = r
        for n in arr:
            rank.append(dic[n])
        return rank
