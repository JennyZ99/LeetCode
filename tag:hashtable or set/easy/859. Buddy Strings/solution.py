"""

** considerations:
        -- I consider the corner case that if the lengths of s and goal are not the same, the two strings must not be buddies.
        
By observations, I find:
        -- if two strings are buddies, either of the following conditions must be met:
                -- there are only two unmatched letters in two different locations; 
                        ...ab...
                        ...ba...
                -- the letters are all matched and there are duplications.
                        ...aa...
                        ...bb...

space: O(n)
time: O(n) where n is the length of s or the number of letter in s

data structure: dictionary

** I also use a variable - diff_count - to count the unmatched letters, if the var>2, the two string cannot be buddies.

In summary, what I need for this problem are:
      -- two dictionaries to store the unmatched letters and their indexes: letter->index pair
                -- one dictionary for string s;
                -- the other dictionary for string goal;
                -- because in order to be buddies, the index sum of two unmatched letters must be the same.
      -- one dictionary to store the frequency of the matched letters: letter -> frequency
                -- because in order to be buddies, the frequency must >2 if the two strings are totally the same.
    

"""


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        size_a = len(s)
        size_b = len(goal)
        dic_s_diff = {}
        dic_goal_diff = {}
        dic_same = {}
        diff_count = 0
        if size_a != size_b:
            return False
        for i in range(0, size_a):
            if s[i]==goal[i]:
                if s[i] not in dic_same:
                    dic_same[s[i]] = 1
                else:
                    dic_same[s[i]] = dic_same[s[i]]+1
            else:
                diff_count += 1
                if(diff_count>2): return False
                dic_s_diff[s[i]] = i
                dic_goal_diff[goal[i]] = i
        if diff_count == 0:
            for key,val in dic_same.items():
                if val>=2: return True
        elif diff_count<2: 
            return False
        elif diff_count==2:
            s_i_sum=0
            goal_i_sum=0
            for key,val in dic_s_diff.items():
                if key not in dic_goal_diff:
                    return False
                s_i_sum+=val
                goal_i_sum+=dic_goal_diff[key]
            if s_i_sum==goal_i_sum: return True
            else: return False
        
    
        
        
