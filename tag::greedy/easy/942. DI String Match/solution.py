"""
This is a relatively simple question, It's just when I see 'I', I add the smallest number in [0, n], and 
when I see 'D', I add the largest number in [0,n].

Time: O(n), where n is the length of the string s
space: O(n) because I use a list
"""

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        arr = [i for i in range(0, len(s)+1)]
        output = []
        for letter in s:
            if letter == 'I':
                char = arr.pop(0)
            else:
                char = arr.pop(len(arr)-1)
            output.append(char)
        output.append(arr[0])
        return output
