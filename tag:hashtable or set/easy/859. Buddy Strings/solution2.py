"""
I use set instead of dictionary for this solution. The idea is the same as solution.py

"""


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        size_a = len(s)
        size_b = len(goal)
        index_sum_s = 0
        index_sum_goal = 0
        set_s = set()
        set_goal = set()
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
                set_s.add(s[i])
                set_goal.add(goal[i])
                index_sum_s = index_sum_s + i
                index_sum_goal = index_sum_goal + i
        if diff_count == 0:
            for key,val in dic_same.items():
                if val>=2: return True
        elif diff_count==2 and index_sum_s==index_sum_goal and len(set_s-set_goal)==0:
            return True
        else:
            return False
