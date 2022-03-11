"""
time: O(n) where n is the number of words in the paragraph.
space: O(n)

data structure: set and dictionary 

I need:
      -- a banned set;
      -- a dicitonary to store the frequency of each word; 
      -- return the unique word that has the max frequency. 
      
** I need to split the paragraph by all punctuations. Refer how to use re.split() at https://docs.python.org/3/library/re.html
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # as the paragraph are case-insensitive
        p = paragraph.lower()
        ban_set = set()
        dic = {}
        max_freq = 0
        most_comm_word = ''
        for val in banned:
            ban_set.add(val)
        for val in re.split( r'\W+',p):
            if val in ban_set:
                continue
            else:
                if val in dic :
                    dic[val] = dic[val]+1
                else:
                    dic[val] = 1
                if dic[val] > max_freq:
                    most_comm_word = val
                    max_freq = dic[val]
        return most_comm_word
            
