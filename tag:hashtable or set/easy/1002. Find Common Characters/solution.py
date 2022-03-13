"""
data structure: array/list
time: O(n*m), where n is the number of words, and m is the avg length of each word.
space: O(m)

I want to know the common characters of all words, so I define a list for storing the common characters, and 
for each word, I update the list and only keep the characters that alreay exist in the list.
"""

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        comm = []
        for i, word in enumerate(words):
            if i==0:
                for letter in word:
                    comm.append(letter)
            else:
                temp = []
                for letter in word:
                    if letter in comm:
                        temp.append(letter)
                        comm.remove(letter)
                comm = temp
        return comm
