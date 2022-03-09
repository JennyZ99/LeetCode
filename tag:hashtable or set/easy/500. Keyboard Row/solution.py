"""
n: number of words
m: average length of each word
time complexity: O(m*n)
space: O(1)

    I need
          - a dictionary to store the row number of each letter: letter - row_number (key-value pair);
          - for each word, I need check if the row number of each letter is the same;
          - I need a boolean var to indicate whether the row number is the same or not, and we only append 
            the words to output if the boolean var is_same_row is True;
    
    ** note/considerations: 
          - I need lower the case of each word for checking the built dictionary, and I dont want to change the case of each letter in the final result. 

"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        dic = {}
        dic=self.build_dic(first_row, dic, 1)
        dic=self.build_dic(second_row, dic, 2)
        dic=self.build_dic(third_row, dic, 3)
        found_words = []
        for word in words:
            row = 0
            is_same_row = True
            word_ = word.lower()
            for i, val in enumerate(word_):
                if i==0: row=dic[val]
                else:
                    if dic[val]!=row: 
                      is_same_row = False
                      break
            if(is_same_row):
                found_words.append(word)
        return found_words
    
    def build_dic(self, letters: str, dic: dict, row: int) -> dict:
        for l in letters:
            dic[l] = row
        return dic
