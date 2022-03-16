"""
Reference: 
          -- built-in sort function in applying to dictionary with lambda: https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/
          -- built-in sort in python3: https://docs.python.org/3/howto/sorting.html
          -- solution from gasohel336 on LeetCode.
          
Data Structure: dictionary

Built-in Func: Sorted, Counter

time: O(nlogn)

space: O(n)

What I need for this problem are:
        -- frequency of each number;
        -- sort the dictionary by item's frequency in the first priority;
        -- sort the dictionary by item's value - number - in a reverse order in the 2nd priority;
"""

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        arr_by_freq = []
        for val, freq in sorted(dic.items(), key = lambda item: (item[1],-item[0])): arr_by_freq.extend([val]*freq)
        return arr_by_freq
