"""
built-in python function:
                        -- split() in re
                                            -- reference: https://docs.python.org/3/library/re.html
                                            -- use to split the string by alphabet letters
                        -- isnumeric()
                                            -- for checking if a string/char is number 

** considerations: I need to consider the case when strings are '01', '001', '1'. Hence, I need to use int() to convert all 
the strings to number before count 
"""

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        arr = re.split('[a-z]+', word)
        myset= set()
        for num in arr:
            if num.isnumeric():
                myset.add(int(num))
        return len(myset)
