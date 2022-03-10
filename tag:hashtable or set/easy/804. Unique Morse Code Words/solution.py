"""
time: O(m*n), where n is number of words, and m is the avg length of each word.
space: O(n)

data structure: dictionary, set
    -- a dictionary: letter - morse_code pair, built for checking the morse code
    -- a set: use to store the unique transformations

output: the size of the set, because the set stores the unique transformations 
"""

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_dic = self.get_morse_dic(morse)
        my_set = set()
        for word in words:
            tran = ""
            for letter in word:
                tran = tran + morse_dic[letter]
            my_set.add(tran)
        return len(my_set)
        
    def get_morse_dic(self, morse: List[str]) -> dict:
        dic = {}
        a = ord('a')
        for i in range(0, 26):
            dic[chr(a+i)] = morse[i]
        return dic
